"""This module creates a Student class and modifies its attributes."""


class Student:
    """A class representing a student."""

    def __init__(self, name, surname, avg_score, age):
        """
        Initialize a new Student instance.

        Args:
            name (str): The student's first name.
            surname (str): The student's last name.
            avg_score (float): The student's average score.
            age (int): The student's age.
        """
        self.name = name
        self.surname = surname
        self.avg_score = avg_score
        self.age = age

    def scorer(self, new_score):
        """
        Update the student's average score.

        Args:
            new_score (float): The new average score to set.
        """
        self.avg_score = new_score
        print(f'{self.name}, {self.surname}, {self.avg_score}, {self.age}')


student = Student(name='FirstName', surname='LastName', avg_score=0, age=43)
student.scorer(5)
