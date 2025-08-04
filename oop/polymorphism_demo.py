import math

class Shape:
    """Base class for shapes that defines the interface for area calculation."""
    
    def area(self):
        """
        Calculate the area of the shape.
        
        This method should be overridden by derived classes.
        
        Raises:
            NotImplementedError: This method must be implemented by subclasses
        """
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""
    
    def __init__(self, length, width):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """Circle class that inherits from Shape."""
    
    def __init__(self, radius):
        """
        Initialize a Circle instance.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π × radius²)
        """
        return math.pi * (self.radius ** 2)
