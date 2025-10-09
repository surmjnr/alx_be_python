from class_static_methods_demo import Calculator

def main():
    """
    Main function to demonstrate the usage of static and class methods.
    
    This function shows how to call both static methods and class methods,
    highlighting the differences in their usage and behavior.
    """
    print("=== Calculator Class Methods Demo ===\n")
    
    # Using the static method
    # Static methods can be called directly on the class without creating an instance
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")
    
    print()  # Empty line for better output formatting
    
    # Using the class method
    # Class methods can access class attributes and are called on the class
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
    
    print("\n=== Additional Examples ===")
    
    # More examples to demonstrate the methods
    print(f"Static method - Subtraction equivalent: {Calculator.add(20, -5)}")
    print(f"Class method - Another multiplication: ", end="")
    result = Calculator.multiply(7, 8)
    print(f"Result: {result}")
    
    # Demonstrating that you can also call these methods on instances
    calc = Calculator()
    print(f"\nCalled on instance - Sum: {calc.add(15, 25)}")
    print("Called on instance - Product: ", end="")
    result = calc.multiply(15, 25)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()