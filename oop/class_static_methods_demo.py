class Calculator:
    """
    A Calculator class that demonstrates the use of static methods and class methods.
    
    This class illustrates the differences between @staticmethod and @classmethod decorators:
    - Static methods don't need access to class or instance data
    - Class methods can access class attributes and methods via the 'cls' parameter
    """
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Static methods don't have access to class or instance data.
        They are used for utility functions that are logically related to the class
        but don't need to access class-specific data.
        
        Args:
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        
        Class methods have access to class attributes and methods via the 'cls' parameter.
        They are used when you need to access class-level data or create alternative constructors.
        
        Args:
            cls: Reference to the class (Calculator)
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
