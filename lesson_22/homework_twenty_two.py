from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random


Base = declarative_base()


student_course_association = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)


class Student(Base):
    """
    Represent a student in the system.

    Attributes:
        id (int): The unique identifier for the student.
        name (str): The name of the student.
        courses (relationship): A many-to-many relationship with the Course model.
    """
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    courses = relationship('Course', secondary=student_course_association, back_populates='students')

    def __repr__(self):
        return f'<Student(id={self.id}, name={self.name})>'


class Course(Base):
    """
    Represent a course in the system.

    Attributes:
        id (int): The unique identifier for the course.
        name (str): The name of the course.
        students (relationship): A many-to-many relationship with the Student model.
    """
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship('Student', secondary=student_course_association, back_populates='courses')

    def __repr__(self):
        return f'<Course(id={self.id}, name={self.name})>'


engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


course_names = ["Math", "Physics", "Chemistry", "Biology", "History"]
courses = [Course(name=name) for name in course_names]
session.add_all(courses)
session.commit()


students = [Student(name=f"Student_{i + 1}") for i in range(20)]
session.add_all(students)
session.commit()


for student in students:
    assigned_courses = random.sample(courses, k=random.randint(1, 3))
    student.courses.extend(assigned_courses)
session.commit()


def add_student_to_course(student_name, course_name):
    """
    Add a new student to a specified course.

    Args:
        student_name (str): The name of the student to be added.
        course_name (str): The name of the course the student will be enrolled in.

    Returns:
        None
    """
    new_student = Student(name=student_name)
    course = session.query(Course).filter_by(name=course_name).first()

    if not course:
        print(f"Course '{course_name}' not found.")
        return

    new_student.courses.append(course)
    session.add(new_student)
    session.commit()
    print(f"Added student '{student_name}' to course '{course_name}'.")


def get_students_in_course(course_name):
    """
    Retrieve a list of students enrolled in a specific course.

    Args:
        course_name (str): The name of the course.

    Returns:
        list: A list of student names enrolled in the course.
    """
    course = session.query(Course).filter_by(name=course_name).first()

    if not course:
        print(f"Course '{course_name}' not found.")
        return []

    return [student.name for student in course.students]


def get_courses_of_student(student_name):
    """
    Retrieve a list of courses that a specific student is enrolled in.

    Args:
        student_name (str): The name of the student.

    Returns:
        list: A list of course names that the student is enrolled in.
    """
    student = session.query(Student).filter_by(name=student_name).first()

    if not student:
        print(f"Student '{student_name}' not found.")
        return []

    return [course.name for course in student.courses]


def update_student_name(old_name, new_name):
    """
    Update a student's name in the database.

    Args:
        old_name (str): The current name of the student.
        new_name (str): The new name to assign to the student.

    Returns:
        None
    """
    student = session.query(Student).filter_by(name=old_name).first()

    if student:
        student.name = new_name
        session.commit()
        print(f"Updated student name from '{old_name}' to '{new_name}'.")
    else:
        print(f"Student '{old_name}' not found.")


def delete_student(student_name):
    """
    Delete a student from the database.

    Args:
        student_name (str): The name of the student to be deleted.

    Returns:
        None
    """
    student = session.query(Student).filter_by(name=student_name).first()

    if student:
        session.delete(student)
        session.commit()
        print(f"Deleted student '{student_name}' from the database.")
    else:
        print(f"Student '{student_name}' not found.")


add_student_to_course('John Doe', 'Math')
print("Students in 'Math':", get_students_in_course('Math'))
print("Courses of 'John Doe':", get_courses_of_student('John Doe'))
update_student_name('John Doe', 'John Smith')
delete_student('John Smith')
