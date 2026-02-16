"""
app/operation.py

Class 'Operation' encapsulates mathematical methods:
    - addition
    - subtraction
    - multiplication
    - division
    - power

Special Handling:
    - Includes the LBYL Principle (Look Before You Leap).
    - Handles division by zero gracefully by raising a ZeroDivisionError.
"""

class Operation:
    """Encapsulates mathematical operations for two float operands."""
    
    @staticmethod
    def addition(a: float, b: float) -> float:
        """Returns the sum of two operands."""
        return a + b
    
    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """Returns the difference of two operands."""
        return a - b
    
    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """Returns the product of two operands."""
        return a * b
    
    @staticmethod
    def division(a: float, b: float) -> float:
        """Returns the quotient of two operands."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
        
    @staticmethod    
    def power(a: float, b: float) -> float:
        """Returns operand 'a' raised to the power of operand 'b'."""
        return a ** b
    
    @staticmethod    
    def modulus(a: float, b: float) -> float:
        """Returns the remainder of operand 'a' and operand 'b'."""
        if b == 0:
            raise ZeroDivisionError("Modulus: Cannot divide by zero.")
        return a % b

    