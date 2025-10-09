import math


class Shape:
    """Base class for all shapes."""
    
    def area(self):
        """Calculate the area of the shape.
        
        This method should be overridden in derived classes.
        Raises NotImplementedError if called directly on Shape instance.
        """
        raise NotImplementedError("Subclasses must implement the area() method")


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""
    
    def __init__(self, length, width):
        """Initialize a rectangle with given length and width.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """Circle class that inherits from Shape."""
    
    def __init__(self, radius):
        """Initialize a circle with given radius.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π × radius²)
        """
        return math.pi * (self.radius ** 2)
