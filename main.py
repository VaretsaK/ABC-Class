from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """
    @abstractmethod
    def area(self) -> None:
        """
        Abstract method to compute the area of the shape.
        This method must be implemented by subclasses.
        """
        pass


class Rectangle(Shape):
    """
    Represents a rectangle, a subclass of Shape.
    """
    def __init__(self, width: int, length: int) -> None:
        """
        Initializes a new Rectangle object with the given width and length.

        Args:
        - width (int): The width of the rectangle.
        - length (int): The length of the rectangle.
        """
        self.width = width
        self.length = length

    def area(self) -> int:
        """
        Computes the area of the rectangle.

        Returns:
        - int: The area of the rectangle.
        """
        result = self.width * self.length
        return result


class Circle(Shape):
    """
    Represents a circle, a subclass of Shape.
    """
    def __init__(self, radius: int) -> None:
        """
        Initializes a new Circle object with the given radius.

        Args:
        - radius (int): The radius of the circle.
        """
        self.radius = radius

    def area(self) -> int:
        """
        Computes the area of the circle.

        Returns:
        - int: The area of the circle.
        """
        result = 3.14 * self.radius ** 2
        return result


def main() -> None:
    """
    Main function to demonstrate the usage of Rectangle and Circle classes.
    """
    rec = Rectangle(5, 5)
    cir = Circle(11)
    print(rec.area())
    print(cir.area())


if __name__ == "__main__":
    main()
