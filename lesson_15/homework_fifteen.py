"""This module contains the Rombus class."""


"""Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:
Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__."""


class Rombus:
    """A class representing a Rhombus."""
    def __init__(self, side_a, angle_a):
        """Initialize a Rhombus with a side length and an angle."""
        self.angle_b = None
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        """Set attributes with validation."""
        if name == 'side_a':
            if value <= 0:
                raise ValueError('The side value must be greater than 0')
        elif name == 'angle_a':
            if not (0 < value < 180):
                raise ValueError('The angle must be within (0, 180) degrees')
            super().__setattr__('angle_b', 180 - value)
        super().__setattr__(name, value)

    def __repr__(self):
        """Return a string representation of the Rhombus."""
        return (
            f'Rhombus(side_a={self.side_a}, '
            f'angle_a={self.angle_a}, angle_b={self.angle_b})'
        )


try:
    r = Rombus(10, 60)
    print(r)

    r.angle_a = 45
    print(r)

    r.side_a = -5
except ValueError as e:
    print(e)
