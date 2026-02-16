"""
tests/test_calculations.py

Tests both positive and negative scenarios for the Calculation classes and CalculationFactory.

Ensures that calculations execute correctly, factory creates appropriate instances, and error handling behaves as expected.
"""

import pytest
from unittest.mock import patch
from app.operation import Operation
from app.calculation import (
    CalculationFactory, 
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    PowerCalculation,
    ModulusCalculation,
    Calculation
)

#-------------------------------------------
# Test Concrete Classes
#-------------------------------------------

# Addition calcalation

@patch.object(Operation, 'addition')
def test_add_calculation_execute_positive(mock_addition):
    """
    Tests the execute method of AddCalculation for a positive scenario.

    Verifies that the AddCalculation correctly calls the addition method in the Operation class
    with the provided operands and result.
    """

    # Arrange
    a = 8.0
    b = 2.0
    expected_result = 10.0
    mock_addition.return_value = expected_result # Mock the addition method's return value.
    add_calc = AddCalculation(a, b) # Instantiate AddCalculation with operands.

    # Act
    result = add_calc.execute() # Execute the addition calculation.

    # Assert
    mock_addition.assert_called_once_with(a, b) # Ensure addition was called with correct operands.
    assert result == expected_result # Verify the result matches the expected value.

@patch.object(Operation, 'addition')
def test_add_calculation_execute_negative(mock_addition):
    """
    Tests the execute method of AddCalculation for a negative scenario.

    Ensures that if Operation.addition method raises an exception, 
    the AddCalculation.execute method propagates it correctly.
    """

    # Arrange
    a = 8.0
    b = 2.0
    mock_addition.side_effect = Exception("Addition error") # Simulate an exception in addition
    add_calc = AddCalculation(a, b)

    # Act and Assert
    with pytest.raises(Exception) as exc_info:
        add_calc.execute() # Attempt to execute addition, expecting an exception

    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Addition error"

# Subtraction calcalation

@patch.object(Operation, 'subtraction')
def test_subtract_calculation_execute_positive(mock_subtraction):
    """
    Tests the execute method of SubtractCalculation for a positive scenario.

    Verifies that the SubtractCalculation correctly calls the subtraction method in the Operation class
    with the provided operands and result.
    """

    # Arrange
    a = 8.0
    b = 2.0
    expected_result = 6.0
    mock_subtraction.return_value = expected_result
    subtract_calc = SubtractCalculation(a, b)

    # Act
    result = subtract_calc.execute()

    # Assert
    mock_subtraction.assert_called_once_with(a, b)
    assert result == expected_result

@patch.object(Operation, 'subtraction')
def test_subtract_calculation_execute_negative(mock_subtraction):
    """
    Tests the execute method of SubtractCalculation for a negative scenario.

    Ensures that if Operation.subtraction method raises an exception, 
    the SubtractCalculation.execute method propagates it correctly.
    """

    # Arrange
    a = 8.0
    b = 2.0
    mock_subtraction.side_effect = Exception("Subtraction error")
    subtract_calc = SubtractCalculation(a, b)

    # Act and Assert
    with pytest.raises(Exception) as exc_info:
        subtract_calc.execute()

    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Subtraction error"

# Multiplication calcalation

@patch.object(Operation, 'multiplication')
def test_multiplication_calculation_execute_positive(mock_multiplication):
    """
    Tests the execute method of MultiplyCalculation for a positive scenario.

    Verifies that the MultiplyCalculation correctly calls the multiplication method in the Operation class
    with the provided operands and result.
    """

    # Arrange
    a = 8.0
    b = 2.0
    expected_result = 16.0
    mock_multiplication.return_value = expected_result
    multiply_calc = MultiplyCalculation(a, b)

    # Act
    result = multiply_calc.execute()

    # Assert
    mock_multiplication.assert_called_once_with(a, b)
    assert result == expected_result

@patch.object(Operation, 'multiplication')
def test_multiply_calculation_execute_negative(mock_multiplication):
    """
    Tests the execute method of MultiplyCalculation for a negative scenario.

    Ensures that if Operation.multiplication method raises an exception, 
    the MultiplyCalculation.execute method propagates it correctly.
    """

    # Arrange
    a = 8.0
    b = 2.0
    mock_multiplication.side_effect = Exception("Multiplication error")
    multiply_calc = MultiplyCalculation(a, b)

    # Act and Assert
    with pytest.raises(Exception) as exc_info:
        multiply_calc.execute()

    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Multiplication error"

# Division calcalation

@patch.object(Operation, 'division')
def test_division_calculation_execute_positive(mock_division):
    """
    Tests the execute method of DivideCalculation for a positive scenario.

    Verifies that the DivideCalculation correctly calls the division method in the Operation class
    with the provided operands and result.
    """

    # Arrange
    a = 8.0
    b = 2.0
    expected_result = 4.0
    mock_division.return_value = expected_result
    divide_calc = DivideCalculation(a, b)

    # Act
    result = divide_calc.execute()

    # Assert
    mock_division.assert_called_once_with(a, b)
    assert result == expected_result

@patch.object(Operation, 'division')
def test_division_calculation_execute_negative(mock_division):
    """
    Tests the execute method of DivideCalculation for a negative scenario.

    Ensures that if Operation.division method raises an exception, 
    the DivideCalculation.execute method propagates it correctly.
    """

    # Arrange
    a = 8.0
    b = 2.0
    mock_division.side_effect = Exception("Division error")
    divide_calc = DivideCalculation(a, b)

    # Act and Assert
    with pytest.raises(Exception) as exc_info:
        divide_calc.execute()

    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Division error"

def test_divide_calculation_execute_zero():
    """
    Test that DivideCalculation.execute raises ZeroDivisionError when dividing by zero.

    This test verifies that attempting to divide by zero using DivideCalculation
    correctly raises a ZeroDivisionError with an appropriate error message.
    """
    
    # Arrange
    a = 8.0
    b = 0.0
    divide_calc = DivideCalculation(a, b)

    # Act and Assert
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide_calc.execute()

    # Verify the exception message is as expected
    assert str(exc_info.value) == "Cannot divide by zero."


# Power calcalation

@patch.object(Operation, 'power')
def test_power_calculation_execute_positive(mock_power):
    """
    Tests the execute method of PowerCalculation for a positive scenario.

    Verifies that the PowerCalculation correctly calls the power method in the Operation class
    with the provided operands and result.
    """

    # Arrange
    a = 8.0
    b = 2.0
    expected_result = 64.0
    mock_power.return_value = expected_result
    power_calc = PowerCalculation(a, b)

    # Act
    result = power_calc.execute()

    # Assert
    mock_power.assert_called_once_with(a, b)
    assert result == expected_result

@patch.object(Operation, 'power')
def test_power_calculation_execute_negative(mock_power):
    """
    Tests the execute method of PowerCalculation for a negative scenario.

    Ensures that if Operation.power method raises an exception, 
    the PowerCalculation.execute method propagates it correctly.
    """ 

    # Arrange
    a = 8.0
    b = 2.0
    mock_power.side_effect = Exception("Power error")
    power_calc = PowerCalculation(a, b)

    # Act and Assert
    with pytest.raises(Exception) as exc_info:
        power_calc.execute()
    
    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Power error"

# Modulus calcalation

@patch.object(Operation, 'modulus')
def test_modulus_calculation_execute_positive(mock_modulus):
    """
    Tests the execute method of ModulusCalculation for a positive scenario.

    Verifies that the ModulusCalculation correctly calls the modulus method in the Operation class
    with the provided operands and result.
    """

    # Arrange
    a = 8.0
    b = 2.0
    expected_result = 0.0
    mock_modulus.return_value = expected_result
    mod_calc = ModulusCalculation(a, b)

    # Act
    result = mod_calc.execute()

    # Assert
    mock_modulus.assert_called_once_with(a, b)
    assert result == expected_result

@patch.object(Operation, 'modulus')
def test_modulus_calculation_execute_negative(mock_modulus):
    """
    Tests the execute method of ModulusCalculation for a negative scenario.

    Ensures that if Operation.modulus method raises an exception, 
    the ModulusCalculation.execute method propagates it correctly.
    """ 
    
    # Arrange
    a = 8.0
    b = 2.0
    mock_modulus.side_effect = Exception("Modulus error")
    mod_calc = ModulusCalculation(a, b)

    # Act and Assert
    with pytest.raises(Exception) as exc_info:
        mod_calc.execute()

    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Modulus error"

def test_modulus_calculation_execute_zero():
    """
    Test that ModulusCalculation.execute raises ZeroDivisionError when dividing by zero.

    This test verifies that attempting to divide by zero using ModulusCalculation
    correctly raises a ZeroDivisionError with an appropriate error message.
    """
    
    # Arrange
    a = 8.0
    b = 0.0
    mod_calc = ModulusCalculation(a, b)

    # Act and Assert
    with pytest.raises(ZeroDivisionError) as exc_info:
        mod_calc.execute()

    # Verify the exception message is as expected
    assert str(exc_info.value) == "Modulus: Cannot divide by zero."

#-------------------------------------------
# Test CalculationFactory
#-------------------------------------------

def test_factory_creates_add_calculation():
    """
    Test that CalculationFactory creates an AddCalculation instance.

    Ensures that the factory correctly instantiates the AddCalculation
    class when the '+' calculation type is requested.
    """

    # Arrange
    a = 8.0
    b = 2.0

    # Act
    calc = CalculationFactory.create_calculation(a, '+', b)

    # Assert
    assert isinstance(calc, AddCalculation) # Check if calc is an instance of AddCalculation
    assert calc.a == a                      # Verify first operand
    assert calc.b == b                      # Verify second operand


def test_factory_creates_subtract_calculation():
    """
    Test that CalculationFactory creates an SubtractCalculation instance.

    Ensures that the factory correctly instantiates the SubtractCalculation
    class when the '-' calculation type is requested.
    """

    # Arrange
    a = 8.0
    b = 2.0

    # Act
    calc = CalculationFactory.create_calculation(a, '-', b)

    # Assert
    assert isinstance(calc, SubtractCalculation) # Check if calc is an instance of SubtractCalculation
    assert calc.a == a                           # Verify first operand
    assert calc.b == b                           # Verify second operand
    
def test_factory_creates_multiplication_calculation():
    """
    Test that CalculationFactory creates an MultiplyCalculation instance.

    Ensures that the factory correctly instantiates the MultiplyCalculation
    class when the '*' calculation type is requested.
    """

    # Arrange
    a = 8.0
    b = 2.0

    # Act
    calc = CalculationFactory.create_calculation(a, '*', b)

    # Assert
    assert isinstance(calc, MultiplyCalculation) # Check if calc is an instance of MultiplyCalculation
    assert calc.a == a                           # Verify first operand
    assert calc.b == b                           # Verify second operand
    
def test_factory_creates_division_calculation():
    """
    Test that CalculationFactory creates an DivideCalculation instance.

    Ensures that the factory correctly instantiates the DivideCalculation
    class when the '/' calculation type is requested.
    """

    # Arrange
    a = 8.0
    b = 2.0

    # Act
    calc = CalculationFactory.create_calculation(a, '/', b)

    # Assert
    assert isinstance(calc, DivideCalculation)   # Check if calc is an instance of DivideCalculation
    assert calc.a == a                           # Verify first operand
    assert calc.b == b                           # Verify second operand

def test_factory_creates_power_calculation():
    """
    Test that CalculationFactory creates an PowerCalculation instance.

    Ensures that the factory correctly instantiates the PowerCalculation
    class when the '**' calculation type is requested.
    """

    # Arrange
    a = 8.0
    b = 2.0

    # Act
    calc = CalculationFactory.create_calculation(a, '**', b)

    # Assert
    assert isinstance(calc, PowerCalculation)    # Check if calc is an instance of PowerCalculation
    assert calc.a == a                           # Verify first operand
    assert calc.b == b                           # Verify second operand

def test_factory_creates_modulus_calculation():
    """
    Test that CalculationFactory creates an ModulusCalculation instance.

    Ensures that the factory correctly instantiates the ModulusCalculation
    class when the '%' calculation type is requested.
    """

    # Arrange
    a = 8.0
    b = 2.0

    # Act
    calc = CalculationFactory.create_calculation(a, '%', b)

    # Assert
    assert isinstance(calc, ModulusCalculation)  # Check if calc is an instance of ModulusCalculation
    assert calc.a == a                           # Verify first operand
    assert calc.b == b                           # Verify second operand


def test_factory_create_unsupported_calculation():
    """
    Test that CalculationFactory raises ValueError when an unsupported calculation type is requested.

    This test ensures that requesting a calculation type not registered with the factory
    results in a ValueError with an appropriate error message.
    """

    # Arrange
    a = 8.0
    b = 2.0
    unsupported_type = '//'  # Unsupported calculation type

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        CalculationFactory.create_calculation(a, unsupported_type, b)

    # Verify that the exception message contains the unsupported type
    assert f"Unsupported calculation type: '{unsupported_type}'" in str(exc_info.value)

def test_factory_register_calculation_duplicate():
    """
    Test that registering a calculation type that's already registered raises ValueError.

    This test verifies that attempting to register a calculation type that has already
    been registered with the factory results in a ValueError to prevent duplicate entries.
    """

    # Arrange & Act
    with pytest.raises(ValueError) as exc_info:
        @CalculationFactory.register_calculation('+')  # Attempts to register '+' again
        class AnotherAddCalculation(Calculation):
            """
            AnotherAddCalculation attempts to register the '+' calculation type again.
            """
            def execute(self) -> float:
                return Operation.addition(self.a, self.b)

    # Assert
    assert "Calculation type '+' is already registered." in str(exc_info.value)

#-------------------------------------------
# Test String Representations
#-------------------------------------------

# __str__ representations

@patch.object(Operation, 'addition', return_value=12.0)
def test_calculation_str_representation_addition(mock_addition):
    """
    Test the __str__ method of AddCalculation.

    This test verifies that the string representation of an AddCalculation instance
    is formatted correctly, displaying the class name, operation, operands, and result.
    """

    # Arrange
    a = 8.0
    b = 4.0
    add_calc = AddCalculation(a, b)

    # Act
    calc_str = str(add_calc)

    # Assert
    expected_str = f"{add_calc.__class__.__name__}: {a} + {b} = 12.0"
    assert calc_str == expected_str

@patch.object(Operation, 'subtraction', return_value=4.0)
def test_calculation_str_representation_subtraction(mock_subtraction):
    """
    Test the __str__ method of SubtractCalculation.

    This test verifies that the string representation of an SubtractCalculation instance
    is formatted correctly, displaying the class name, operation, operands, and result.
    """

    # Arrange
    a = 8.0
    b = 4.0
    subtract_calc = SubtractCalculation(a, b)

    # Act
    calc_str = str(subtract_calc)

    # Assert
    expected_str = f"{subtract_calc.__class__.__name__}: {a} - {b} = 4.0"
    assert calc_str == expected_str

@patch.object(Operation, 'multiplication', return_value=32.0)
def test_calculation_str_representation_multiplication(mock_multiplication):
    """
    Test the __str__ method of MultiplyCalculation.

    This test verifies that the string representation of an MultiplyCalculation instance
    is formatted correctly, displaying the class name, operation, operands, and result.
    """

    # Arrange
    a = 8.0
    b = 4.0
    multiply_calc = MultiplyCalculation(a, b)

    # Act
    calc_str = str(multiply_calc)

    # Assert
    expected_str = f"{multiply_calc.__class__.__name__}: {a} * {b} = 32.0"
    assert calc_str == expected_str

@patch.object(Operation, 'division', return_value=2.0)
def test_calculation_str_representation_division(mock_division):
    """
    Test the __str__ method of DivideCalculation.

    This test verifies that the string representation of an DivideCalculation instance
    is formatted correctly, displaying the class name, operation, operands, and result.
    """

    # Arrange
    a = 8.0
    b = 4.0
    divide_calc = DivideCalculation(a, b)

    # Act
    calc_str = str(divide_calc)

    # Assert
    expected_str = f"{divide_calc.__class__.__name__}: {a} / {b} = 2.0"
    assert calc_str == expected_str

@patch.object(Operation, 'power', return_value=64.0)
def test_calculation_str_representation_division(mock_power):
    """
    Test the __str__ method of PowerCalculation.

    This test verifies that the string representation of an PowerCalculation instance
    is formatted correctly, displaying the class name, operation, operands, and result.
    """

    # Arrange
    a = 8.0
    b = 2.0
    power_calc = PowerCalculation(a, b)

    # Act
    calc_str = str(power_calc)

    # Assert
    expected_str = f"{power_calc.__class__.__name__}: {a} ** {b} = 64.0"
    assert calc_str == expected_str

@patch.object(Operation, 'modulus', return_value=0.0)
def test_calculation_str_representation_division(mock_modulus):
    """
    Test the __str__ method of ModulusCalculation.

    This test verifies that the string representation of an ModulusCalculation instance
    is formatted correctly, displaying the class name, operation, operands, and result.
    """

    # Arrange
    a = 8.0
    b = 2.0
    mod_calc = ModulusCalculation(a, b)

    # Act
    calc_str = str(mod_calc)

    # Assert
    expected_str = f"{mod_calc.__class__.__name__}: {a} % {b} = 0.0"
    assert calc_str == expected_str

# __repr__ representations

def test_calculation_repr_representation_addition():
    """
    Test the __repr__ method of AddCalculation.

    This test ensures that the repr representation of a AddCalculation instance
    accurately reflects the class name and the operands.
    """
    # Arrange
    a = 10.0
    b = 5.0
    add_calc = AddCalculation(a, b)

    # Act
    calc_repr = repr(add_calc)

    # Assert
    expected_repr = f"{AddCalculation.__name__}(a={a}, b={b})"
    assert calc_repr == expected_repr

def test_calculation_repr_representation_subtraction():
    """
    Test the __repr__ method of SubtractCalculation.

    This test ensures that the repr representation of a SubtractCalculation instance
    accurately reflects the class name and the operands.
    """
    # Arrange
    a = 10.0
    b = 5.0
    subtract_calc = SubtractCalculation(a, b)

    # Act
    calc_repr = repr(subtract_calc)

    # Assert
    expected_repr = f"{SubtractCalculation.__name__}(a={a}, b={b})"
    assert calc_repr == expected_repr

def test_calculation_repr_representation_multiplication():
    """
    Test the __repr__ method of MultiplyCalculation.

    This test ensures that the repr representation of a MultiplyCalculation instance
    accurately reflects the class name and the operands.
    """
    # Arrange
    a = 10.0
    b = 5.0
    multiply_calc = MultiplyCalculation(a, b)

    # Act
    calc_repr = repr(multiply_calc)

    # Assert
    expected_repr = f"{MultiplyCalculation.__name__}(a={a}, b={b})"
    assert calc_repr == expected_repr

def test_calculation_repr_representation_division():
    """
    Test the __repr__ method of DivideCalculation.

    This test ensures that the repr representation of a DivideCalculation instance
    accurately reflects the class name and the operands.
    """
    # Arrange
    a = 10.0
    b = 5.0
    divide_calc = DivideCalculation(a, b)

    # Act
    calc_repr = repr(divide_calc)

    # Assert
    expected_repr = f"{DivideCalculation.__name__}(a={a}, b={b})"
    assert calc_repr == expected_repr

def test_calculation_repr_representation_power():
    """
    Test the __repr__ method of PowerCalculation.

    This test ensures that the repr representation of a PowerCalculation instance
    accurately reflects the class name and the operands.
    """
    # Arrange
    a = 10.0
    b = 5.0
    power_calc = PowerCalculation(a, b)

    # Act
    calc_repr = repr(power_calc)

    # Assert
    expected_repr = f"{PowerCalculation.__name__}(a={a}, b={b})"
    assert calc_repr == expected_repr

def test_calculation_repr_representation_modulus():
    """
    Test the __repr__ method of ModulusCalculation.

    This test ensures that the repr representation of a ModulusCalculation instance
    accurately reflects the class name and the operands.
    """
    # Arrange
    a = 10.0
    b = 5.0
    mod_calc = ModulusCalculation(a, b)

    # Act
    calc_repr = repr(mod_calc)

    # Assert
    expected_repr = f"{ModulusCalculation.__name__}(a={a}, b={b})"
    assert calc_repr == expected_repr

#-------------------------------------------
# Parametrize Test for Execute Method
#-------------------------------------------

@pytest.mark.parametrize(
    "a, calc_type, b, expected_result",
    [
        (8.0, '+', 2.0, 10.0),
        (8.0, '-', 2.0, 6.0),
        (8.0, '*', 2.0, 16.0),
        (8.0, '/', 2.0, 4.0),
        (8.0, '**', 2.0, 64.0),
        (8.0, '%', 2.0, 0.0)
])
@patch.object(Operation, 'addition')
@patch.object(Operation, 'subtraction')
@patch.object(Operation, 'multiplication')
@patch.object(Operation, 'division')
@patch.object(Operation, 'power')
@patch.object(Operation, 'modulus')

def test_calculation_execute_parameterized(
    mock_modulus, mock_power, mock_division,
    mock_multiplication, mock_subtraction, mock_addition, 
    a, calc_type, b, expected_result
):
    """
    Parameterized test for execute method of different Calculation subclasses.

    This test runs multiple scenarios where different calculation types are executed
    with specific operands, verifying that the correct result is returned.
    """

    # Arrange: Set the appropriate mock based on calculation type
    if calc_type == '+':
        mock_addition.return_value = expected_result
    elif calc_type == '-':
        mock_subtraction.return_value = expected_result
    elif calc_type == '*':
        mock_multiplication.return_value = expected_result
    elif calc_type == '/':
        mock_division.return_value = expected_result
    elif calc_type == '**':
        mock_power.return_value = expected_result
    elif calc_type == '%':
        mock_modulus.return_value = expected_result

    # Act: Create calculation instance and execute
    calc = CalculationFactory.create_calculation(a, calc_type, b)
    result = calc.execute()

    # Assert: Verify the correct operation was called and result matches
    if calc_type == '+':
        mock_addition.assert_called_once_with(a, b)
    elif calc_type == '-':
        mock_subtraction.assert_called_once_with(a, b)
    elif calc_type == '*':
        mock_multiplication.assert_called_once_with(a, b)
    elif calc_type == '/':
        mock_division.assert_called_once_with(a, b)
    elif calc_type == '**':
        mock_power.assert_called_once_with(a, b)
    elif calc_type == '%':
        mock_modulus.assert_called_once_with(a, b)

    assert result == expected_result

#-------------------------------------------
# Parametrize Test for String Representation
#-------------------------------------------

@pytest.mark.parametrize("a, calc_type, b, expected_str", [
    (8.0, '+', 2.0, "AddCalculation: 8.0 + 2.0 = 10.0"),
    (8.0, '-', 2.0, "SubtractCalculation: 8.0 - 2.0 = 6.0"),
    (8.0, '*', 2.0, "MultiplyCalculation: 8.0 * 2.0 = 16.0"),
    (8.0, '/', 2.0, "DivideCalculation: 8.0 / 2.0 = 4.0"),
    (8.0, '**', 2.0, "PowerCalculation: 8.0 ** 2.0 = 64.0"),
    (8.0, '%', 2.0, "ModulusCalculation: 8.0 % 2.0 = 0.0"),
])

@patch.object(Operation, 'addition', return_value=10.0)
@patch.object(Operation, 'subtraction', return_value=6.0)
@patch.object(Operation, 'multiplication', return_value=16.0)
@patch.object(Operation, 'division', return_value=4.0)
@patch.object(Operation, 'power', return_value=64.0)
@patch.object(Operation, 'modulus', return_value=0.0)

def test_calculation_str_parameterized(
    mock_modulus, mock_power, mock_division,
    mock_multiplication, mock_subtraction, mock_addition,
    a, calc_type, b, expected_str
):
    """
    Parameterized test for __str__ method of Calculation subclasses.

    This test verifies that the string representation of different Calculation instances
    is formatted correctly, displaying the class name, operation, operands, and result.
    """

    # Arrange: No additional setup needed as mocks are already set via decorators

    # Act: Create calculation instance and get string representation
    calc = CalculationFactory.create_calculation(a, calc_type, b)
    calc_str = str(calc)

    # Assert: Verify the string representation matches the expected format
    assert calc_str == expected_str