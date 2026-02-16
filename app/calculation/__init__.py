"""
app/calculation.py

This module implements a flexible calculator system using:
    - Abstract base class pattern for extensibility.
    - Factory pattern for dynamic operator registration.
    - Decorator pattern for clean operator-to-subclass mapping.
    - Concrete class for implementation of operations.
"""

from abc import ABC, abstractmethod
from typing import Dict, Type
from app.operation import Operation

#--------------------------------------------------------
# Abstract Base Class: Calculation (Parent Class)
#--------------------------------------------------------

class Calculation(ABC):
    """
    Abstract base class for all calculations.
    
    Defines the interface (execute) and shared behavior (__str__ and __repr__).

    Defines what a calculation should do.
    """

    # Subclasses will overwrite this with the proper operator.
    operator: str = " "
    
    def __init__(self, a: float, b: float) -> None:
        """
        Initializing concrete classes (subclasses).

        Stores operands:
            a: float = First operand.
            b: float = Second operand.
        """
        self.a: float = a
        self.b: float = b
        
    @abstractmethod
    def execute(self) -> float:
        """
        Performs the calculation using the operands 'a' and 'b'.

        This method must be implemented by all concrete classes (subclasses).

        Returns:
            float: Result of the calculation.
        """
        pass    # pragma: no cover

    def __str__(self) -> str:
        """
        User-friendly string representation of the mathematical operation.

        Return example:
            'AddCalculation: a + b': str
        """

        result = self.execute()
        return f"{self.__class__.__name__}: {self.a} {self.operator} {self.b} = {result}"
    
    def __repr__(self) -> str:
        """
        Developer-friendly string representation of the mathematical operation.

        Return example:
            'AddCalculation(a=2.0, b=5.0)': str
        """
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"
    
#--------------------------------------------------------
# Factory Class: CalculationFactory
#--------------------------------------------------------

class CalculationFactory:
    """
    Stores key-value pairs into a dictionary.

    Decorator used to dynamically assign new sublasses to operators.

    Defines which subclass to use based on the operator.
    """

    _calculations: Dict[str, Type[Calculation]] = {}

    @classmethod
    def register_calculation(cls, calculation_type: str):
        """
        Prevent duplicate calculation type registration. 
        
        Assign a subclass value to an calculation type key.
        """

        def decorator(subclass: Type[Calculation]) -> Type[Calculation]:
            if calculation_type in cls._calculations:
                raise ValueError(
                    f"Calculation type '{calculation_type}' is already registered."
                    )
            cls._calculations[calculation_type] = subclass
            return subclass
        return decorator

    @classmethod
    def create_calculation(cls, a: float, calculation_type: str, b: float) -> Calculation:
        """
        Validates if calculation type provided by the user is valid.
        
        Provides user with valid calculation type.
        """

        calculation_class = cls._calculations.get(calculation_type)

        if not calculation_class:
            available_calculations = ', '.join(cls._calculations.keys())  # +, -, *, /, **
            raise ValueError(
                f"Unsupported calculation type: '{calculation_type}'. Available calculation types: '{available_calculations}'"
            )
        return calculation_class(a, b)

#--------------------------------------------------------
# Calculation Concrete Classes (Subclasses)
#--------------------------------------------------------

"""
Defines how the calculation is performed.

Implements the specific mathematical operation.
"""

@CalculationFactory.register_calculation('+')
class AddCalculation(Calculation): # addition concrete/subclass
    """Performs addition operation of a + b."""

    operator: str = '+'

    def execute(self) -> float:
        return Operation.addition(self.a, self.b)

@CalculationFactory.register_calculation('-')
class SubtractCalculation(Calculation): # subtraction concrete/subclass
    """Performs subtraction operation of a - b."""

    operator: str = '-'

    def execute(self) -> float:
        return Operation.subtraction(self.a, self.b)

@CalculationFactory.register_calculation('*')
class MultiplyCalculation(Calculation): # multiplication concrete/subclass
    """Performs multiplication operation of a * b."""

    operator: str = '*'

    def execute(self) -> float:
        return Operation.multiplication(self.a, self.b)

@CalculationFactory.register_calculation('/')
class DivideCalculation(Calculation): # division concrete/subclass
    """Performs division operation of a / b."""

    operator: str = '/'

    def execute(self) -> float:
        return Operation.division(self.a, self.b)
       

@CalculationFactory.register_calculation('**')
class PowerCalculation(Calculation): # power concrete/subclass
    """Performs power operation of a ** b."""

    operator: str = '**'

    def execute(self) -> float:
        return Operation.power(self.a, self.b)
    
@CalculationFactory.register_calculation('%')
class ModulusCalculation(Calculation): # modulus concrete/subclass
    """Performs modulus operation of a % b."""
    
    operator: str = '%'

    def execute(self) -> float:
        return Operation.modulus(self.a, self.b)

        

        

        









