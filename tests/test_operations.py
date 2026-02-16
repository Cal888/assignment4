"""
tests/test_operations.py

Unit tests for mathematical operations: 
    - addition
    - subtraction
    - multiplication
    - division
    - power

Individual tests are organized in the AAA (Arrange, Act, Assert) pattern and include two operands.

Test Criteria:
    - Two positive operands.
    - Two negative operands.
    - Positive and negative operand.
    - Positive and zero operand.

Parametrize tests for invalid input types.

Test Criteria:
    - Calculation Method : addition, subtraction, multiplication, division, power
    - a                  : float
    - b                  : float
    - Expected Exception : TypeError
"""

import pytest
from app.operation import Operation

#-----------------------------------------
# Test Addition Method
#-----------------------------------------

def test_addition_positive():
    """Testing addition method with two positive operands."""

    # Arrange
    a = 8.0
    b = 2.0
    expected_result = 10.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, but got {result}"

def test_addition_negative():
    """Testing addition method with two negative operands."""

    # Arrange
    a = -8.0
    b = -2.0
    expected_result = -10.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, but got {result}"

def test_addition_positive_negative():
    """Testing addition method with a positive and negative operand."""

    # Arrange
    a = 8.0
    b = -2.0
    expected_result = 6.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + ({b}) to be {expected_result}, but got {result}"

def test_addition_with_zero():
    """Testing addition method with zero."""

    # Arrange
    a = 8.0
    b = 0.0
    expected_result = 8.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, but got {result}"

#-----------------------------------------
# Test Subtraction Method
#-----------------------------------------

def test_subtraction_positive():
    """Testing subtraction method with two positive operands."""

    # Arrange
    a = 8.0
    b = 2.0
    expected_result = 6.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - {b} to be {expected_result}, but got {result}"


def test_subtraction_negative():
    """Testing subtraction method with two negative operands."""

    # Arrange
    a = -8.0
    b = -2.0
    expected_result = -6.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - ({b}) to be {expected_result}, but got {result}"


def test_subtraction_positive_negative():
    """Testing subtraction method with a positive and negative operand."""

    # Arrange
    a = 8.0
    b = -2.0
    expected_result = 10.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - ({b}) to be {expected_result}, but got {result}"

def test_subtraction_with_zero():
    """Testing subtraction method with zero."""

    # Arrange
    a = 8.0
    b = 0.0
    expected_result = 8.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - {b} to be {expected_result}, but got {result}"

#-----------------------------------------
# Test Multiplication Method
#-----------------------------------------

def test_multiplication_positive():
    """Testing multiplication method with two positive operands."""

    # Arrange
    a = 8.0
    b = 2.0
    expected_result = 16.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, but got {result}"

def test_multiplication_negative():
    """Testing multiplication method with two negative operands."""

    # Arrange
    a = -8.0
    b = -2.0
    expected_result = 16.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, but got {result}"

def test_multiplication_positive_negative():
    """Testing multiplication method with a positive and negative operand."""

    # Arrange
    a = 8.0
    b = -2.0
    expected_result = -16.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, but got {result}"


def test_multiplication_with_zero():
    """Testing multiplication method with zero."""

    # Arrange
    a = 8.0
    b = 0.0
    expected_result = 0.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, but got {result}"

#-----------------------------------------
# Test Division Method
#-----------------------------------------

def test_division_positive():
    """Testing division method with two positive operands."""
    
    # Arrange
    a = 8.0
    b = 2.0
    expected_result = 4.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, but got {result}"


def test_division_negative():
    """Testing division method with two negative operands."""

    # Arrange
    a = -8.0
    b = -2.0
    expected_result = 4.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, but got {result}"

def test_division_positive_negative():
    """Testing division method with a positive and negative operand."""

    # Arrange
    a = 8.0
    b = -2.0
    expected_result = -4.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, but got {result}"

def test_division_with_zero_divisor():
    """Testing division method with zero in the denominator."""

    # Arrange
    a = 8.0
    b = 0.0

    # Act and Assert
    with pytest.raises(ZeroDivisionError) as exc_info:
        Operation.division(a, b)
        
    # Verify exception message is as expected
    assert str(exc_info.value) == "Cannot divide by zero."

def test_division_with_zero_numerator():
    """Testing division method with zero in the numerator."""

    # Arrange
    a = 0.0
    b = 8.0
    expected_result = 0.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, but got {result}"

#-----------------------------------------
# Test Power Method
#-----------------------------------------

def test_power_positive():
    """Testing positive operand 'a' raised to the power of positive operand 'b'."""

    # Arrange
    a = 8.0
    b = 2.0
    expected_result = 64.0

    # Act
    result = Operation.power(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} ** {b} to be {expected_result}, but got {result}"

def test_power_negative():
    """Testing negative operand 'a' raised to the power of negative operand 'b'."""

    # Arrange
    a = -8.0
    b = -2.0
    expected_result = 0.015625

    # Act
    result = Operation.power(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} ** {b} to be {expected_result}, but got {result}"

def test_power_positive_negative():
    """Testing positive operand 'a' raised to the power of negative operand 'b'."""

    # Arrange
    a = 8.0
    b = -2.0
    expected_result = 0.015625

    # Act
    result = Operation.power(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} ** {b} to be {expected_result}, but got {result}"

def test_power_with_zero_exponent():
    """Testing positive operand 'a' raised to the power of zero."""

    # Arrange
    a = 8.0
    b = 0.0
    expected_result = 1.0

    # Act
    result = Operation.power(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} ** {b} to be {expected_result}, but got {result}"

#-----------------------------------------
# Test Modulus Method
#-----------------------------------------

def test_modulus_positive():
    """Testing the remainder of positive operands 'a' and 'b'."""

    # Arrange
    a = 8.0
    b = 3.0
    expected_result = 2.0

    # Act
    result = Operation.modulus(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} % {b} to be {expected_result}, but got {result}"

def test_modulus_negative():
    """Testing the remainder of negative operands 'a' and 'b'."""

    # Arrange
    a = -8.0
    b = -5.0
    expected_result = -3.0

    # Act
    result = Operation.modulus(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} % {b} to be {expected_result}, but got {result}"

def test_modulus_positive_negative():
    """Testing the remainder of positive operand 'a' and negative operand 'b'."""

    # Arrange
    a = 8.0
    b = -2.0
    expected_result = 0.0

    # Act
    result = Operation.modulus(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} % {b} to be {expected_result}, but got {result}"

def test_modulus_with_zero_divisor():
    """Testing the remainder of positive operands 'a' with zero."""

    # Arrange
    a = 10
    b = 0.0

    # Act and Assert
    with pytest.raises(ZeroDivisionError) as exc_info:
        Operation.modulus(a, b)
        
    # Verify exception message is as expected
    assert str(exc_info.value) == "Modulus: Cannot divide by zero."

def test_modulus_with_zero_numerator():
    """Testing the remainder of positive operands 'a' with zero."""

    # Arrange
    a = 0.0
    b = 3.0
    expected_result = 0.0

    # Act
    result = Operation.modulus(a, b)
        
    # Assert
    assert result == expected_result, f"Expected {a} % {b} to be {expected_result}, but got {result}"

#-----------------------------------------
# Negative Testing (Invalid Inputs)
#-----------------------------------------

@pytest.mark.parametrize(
    "calc_method, a, b, expected_exception", 
    [
        (Operation.addition, '8', 2.0, TypeError),
        (Operation.subtraction, 8.0, '2', TypeError),
        (Operation.multiplication, '8', '2', TypeError),
        (Operation.division, 8.0, '2', TypeError),
        (Operation.power, '8', 2.0, TypeError),
        (Operation.modulus, 2.0, '7', TypeError)
    ])

def test_operations_invalid_input_types(calc_method, a, b, expected_exception):
    """Testing invalid input parameters to raise TypeError."""

    with pytest.raises(expected_exception):
        calc_method(a, b)