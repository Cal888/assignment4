"""
tests/test_calculator.py



"""
import pytest
from io import StringIO
from app.calculator import display_help, display_history, calculator

def test_display_help(capsys):
    """Tests display_help function to ensure it prints out the correct help message."""

    # Arrange: None

    # Act: Call function
    display_help()

    # Assert
    captured = capsys.readouterr()
    expected_output = """
    REPL Calculator Help
    --------------------

    Operations:
        <number1> <operator> <number2>
        - Perform a calculation with a supported operator and two numbers.
        
        Supported Operations:
        +   : Adds two operands.
        -   : Subtracts the second operand from the first.
        *   : Multiplies two operands.
        /   : Divide first operand by the second.
        **  : First operand to the power of the second.
        %   : Remainder of first operand divided by second.

    Special Commands:
        help    : Displays this help message.
        history : Shows the history of calculations.
        exit    : Exits the calculator.

    Examples:
        3 + 3
        5 - 2
        3 * 4
        4 / 2
        2 ** 2
        8 % 2
    """

    assert captured.out.strip() == expected_output.strip()

def test_display_history(capsys):
    """Tests display_history when it is empty."""

    # Arrange
    history = []

    # Act
    display_history(history)

    # Assert
    captured = capsys.readouterr()
    assert captured.out.strip() == "No calculations performed yet."

def test_display_history_with_entries(capsys):
    """Test the display_history function when there are entries in the history."""

    # Arrange
    history = [
        "AddCalculation: 8.0 + 2.0 = 10.0",
        "SubtractCalculation: 8.0 - 2.0 = 6.0",
        "MultiplyCalculation: 8.0 * 2.0 = 16.0",
        "DivideCalculation: 8.0 / 2.0 = 4.0",
        "PowerCalculation: 8.0 ** 2.0 = 64.0",
        "ModulusCalculation: 8.0 % 2.0 == 0.0"
    ]

    # Act
    display_history(history)

    # Assert
    captured_output = capsys.readouterr()
    excepted_output = """Calculation History:
1. AddCalculation: 8.0 + 2.0 = 10.0
2. SubtractCalculation: 8.0 - 2.0 = 6.0
3. MultiplyCalculation: 8.0 * 2.0 = 16.0
4. DivideCalculation: 8.0 / 2.0 = 4.0
5. PowerCalculation: 8.0 ** 2.0 = 64.0
6. ModulusCalculation: 8.0 % 2.0 == 0.0"""
    
    assert captured_output.out.strip() == excepted_output.strip()

def test_calculator_exit(monkeypatch, capsys):
    """Test the calculator function's ability to handle the 'exit' command."""

    # Arrange
    user_input = 'exit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Exiting REPL calculator. Goodbye!" in captured.out
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 0

def test_calculator_help_command(monkeypatch, capsys):
    """Test the calculator function's ability to handle the 'help' command."""

    # Arrange
    user_input = 'help\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()
    
    # Assert
    captured = capsys.readouterr()
    assert "REPL Calculator Help" in captured.out
    assert "Exiting REPL calculator. Goodbye!" in captured.out

def test_calculator_invalid_input(monkeypatch, capsys):
    """Test the calculator function's handling of invalid input format."""

    # Arrange
    user_input = 'invalid input\nadd 5\nsubtract\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Invalid input. Please use the format: <number1> <operator> <number2>" in captured.out
    assert "Type 'help' for more information." in captured.out

def test_calculator_addition(monkeypatch, capsys):
    """Test the calculator's addition operation."""

    # Arrange
    user_input = '8.0 + 2.0\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Result: AddCalculation: 8.0 + 2.0 = 10.0" in captured.out

def test_calculator_subtraction(monkeypatch, capsys):
    """Test the calculator's subtraction operation."""

    # Arrange
    user_input = '8.0 - 2.0\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Result: SubtractCalculation: 8.0 - 2.0 = 6.0" in captured.out

def test_calculator_multiplication(monkeypatch, capsys):
    """Test the calculator's multiplication operation."""

    # Arrange
    user_input = '8.0 * 2.0\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Result: MultiplyCalculation: 8.0 * 2.0 = 16.0" in captured.out

def test_calculator_division(monkeypatch, capsys):
    """Test the calculator's division operation."""

    # Arrange
    user_input = '8.0 / 2.0\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Result: DivideCalculation: 8.0 / 2.0 = 4.0" in captured.out

def test_calculator_division_by_zero(monkeypatch, capsys):
    """Test the calculator's handling of division by zero."""

    # Arrange
    user_input = '8.0 / 0.0\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Cannot divide by zero." in captured.out


def test_calculator_power(monkeypatch, capsys):
    """Test the calculator's power operation."""

    # Arrange
    user_input = '8.0 ** 2.0\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Result: PowerCalculation: 8.0 ** 2.0 = 64.0" in captured.out

def test_calculator_modulus(monkeypatch, capsys):
    """Test the calculator's modulus operation."""

    # Arrange
    user_input = '8.0 % 2.0\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Result: ModulusCalculation: 8.0 % 2.0 = 0.0" in captured.out

# New Tests to Increase Coverage

def test_calculator_invalid_number_input(monkeypatch, capsys):
    """Test the calculator's handling of invalid number input."""

    # Arrange
    user_input = '8 + five\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Invalid input. Please ensure numbers are valid." in captured.out or \
           "could not convert string to float: 'five'" in captured.out or \
           "Invalid input. Please use the format: <number1> <operator> <number2>" in captured.out
    
def test_calculator_unsupported_operation(monkeypatch, capsys):
    """Test the calculator's handling of an unsupported operation."""

    # Arrange
    user_input = '2 // 3\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Unsupported calculation type: '//'." in captured.out
    assert "Type 'help' for a list of supported operations." in captured.out


def test_calculator_keyboard_interrupt(monkeypatch, capsys):
    """Test the calculator's handling of KeyboardInterrupt (Ctrl+C)."""

    # Arrange
    def mock_input(prompt):
        raise KeyboardInterrupt()
    monkeypatch.setattr('builtins.input', mock_input)

    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Keyboard interupt detected. Exiting calculator. Goodbye!" in captured.out
    assert exc_info.value.code == 0

def test_calculator_eof_error(monkeypatch, capsys):
    """Test the calculator's handling of EOFError (Ctrl+D)."""

    # Arrange
    def mock_input(prompt):
        raise EOFError()
    monkeypatch.setattr('builtins.input', mock_input)

    # Act
    with pytest.raises(SystemExit) as exc_info:
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "EOF detected. Exiting calculator. Goodbye!" in captured.out
    assert exc_info.value.code == 0

def test_calculator_unexpected_exception(monkeypatch, capsys):
    """Test the calculator's handling of unexpected exceptions during calculation execution."""

    # Arrange
    class MockCalculation:
        def execute(self):
            raise Exception("Mock exception during execution")
        def __str__(self):
            return "MockCalculation"

    def mock_create_calculation(operation, a, b):
        return MockCalculation()

    monkeypatch.setattr('app.calculation.CalculationFactory.create_calculation', mock_create_calculation)
    user_input = '8.0 + 2.0\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        calculator()

    # Assert
    captured = capsys.readouterr()
    assert "An error occurred during calculation: Mock exception during execution" in captured.out
    assert "Please try again." in captured.out

# Additional test to get 100% coverage

def test_calculator_history_command(monkeypatch, capsys):
    """Test the history command displays calculation history."""

    user_input = (
        "2 + 2\n"
        "history\n"
        "exit\n"
    )

    monkeypatch.setattr("sys.stdin", StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()

    assert "History" in captured.out or "2 + 2" in captured.out





