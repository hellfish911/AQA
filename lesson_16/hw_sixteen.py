"""This module contains classes."""

import math
from abc import ABC, abstractmethod

"""
Створіть клас Employee, який має атрибути name та salary. 
Далі створіть два класи, Manager та Developer, які успадковуються від Employee. 
Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. 
Цей клас представляє керівника з команди розробників. 
Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), 
а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.
Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
"""

class Employee:
    """Represent an employee with a name and a salary."""

    def __init__(self, name, salary):
        """
        Initialize an employee with the given name and salary.

        Args:
            name (str): The name of the employee.
            salary (float): The salary of the employee.
        """
        self.name = name
        self.salary = salary


class Manager(Employee):
    """Represent a manager."""

    def __init__(self, name, salary, department):
        """
        Initialize a manager with the given name, salary, and department.

        Args:
            name (str): The name of the manager.
            salary (float): The salary of the manager.
            department (str): The department the manager oversees.
        """
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    """Represent a developer."""

    def __init__(self, name, salary, programming_language):
        """
        Initialize a developer.

        Args:
            name (str): The name of the developer.
            salary (float): The salary of the developer.
            programming_language (str): The programming
            language the developer uses.
        """
        super().__init__(name, salary)
        self.programming_language = programming_language


class TeamLead(Employee):
    """Represent a team lead."""

    def __init__(
        self, name, salary, department,
        programming_language, team_size,
    ):
        """
        Initialize a team lead.

        Args:
            name (str): The name of the team lead.
            salary (float): The salary of the team lead.
            department (str): The department the team lead manages.
            programming_language (str): The programming language.
            team_size (int): The size of the team lead manages.
        """
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size


"""
Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні
для них методи для площі та периметру. Властивості по типу “довжина сторони” й т.д.
повинні бути приватними, та ініціалізуватись через конструктор. 
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть 
в консоль площу та периметр кожної.
"""
class Shape(ABC):
    """
    Abstract base class for geometric shapes.

    All shapes must implement
    methods for calculating area and perimeter.
    """

    @abstractmethod
    def get_area(self):
        """
        Abstract method for calculating the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def get_perimeter(self):
        """
        Abstract method for calculating the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Rectangle(Shape):
    """Represent a rectangle, which is a type of shape."""

    def __init__(self, width, height):
        """
        Initialize a rectangle with the given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self._width = width
        self._height = height

    def get_area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self._width * self._height

    def get_perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self._width + self._height)


class Circle(Shape):
    """Represent a circle, which is a type of shape."""

    def __init__(self, radius):
        """
        Initialize a circle with the given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self._radius = radius

    def get_area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self._radius ** 2

    def get_perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self._radius


class Triangle(Shape):
    """Represent a triangle, which is a type of shape."""

    def __init__(self, side_a, side_b, side_c):
        """
        Initialize a triangle with the given sides.

        Args:
            side_a (float): The length of the first side of the triangle.
            side_b (float): The length of the second side of the triangle.
            side_c (float): The length of the third side of the triangle.
        """
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    def get_area(self):
        """
        Calculate the area of the triangle using Heron's formula.

        Returns:
            float: The area of the triangle.
        """
        s = self.get_perimeter() / 2
        return (
            (s * (s - self._side_a)
             * (s - self._side_b)
             * (s - self._side_c)
             ) ** 0.5
        )

    def get_perimeter(self):
        """
        Calculate the perimeter of the triangle.

        Returns:
            float: The perimeter of the triangle.
        """
        return self._side_a + self._side_b + self._side_c


# Creating shapes for testing
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(3, 4, 5),
]

# Display area and perimeter of each shape
for index, fig in enumerate(shapes, start=1):
    print(f'Shape {index}:')
    print(f'Area: {fig.get_area():.2f}')
    print(f'Perimeter: {fig.get_perimeter():.2f}\n')
