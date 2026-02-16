"""
tests/conftest.py

Configuration test file.
"""
import pytest
from app.calculation import (
    CalculationFactory,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    PowerCalculation,
    ModulusCalculation
)

@pytest.fixture(autouse=True)
def reset_calculation_factory():
    """Fixture to reset CalculationFactory's registered calculations before each test."""

    # Clear existing registrations
    CalculationFactory._calculations.clear()

    # Re-register the default calculations
    CalculationFactory.register_calculation('+')(AddCalculation)
    CalculationFactory.register_calculation('-')(SubtractCalculation)
    CalculationFactory.register_calculation('*')(MultiplyCalculation)
    CalculationFactory.register_calculation('/')(DivideCalculation)
    CalculationFactory.register_calculation('**')(PowerCalculation)
    CalculationFactory.register_calculation('%')(ModulusCalculation)

