import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from module.engineering import EngineeringCalculator

def test_square_root():
    calc = EngineeringCalculator()
    result1 = calc.square_root(16)
    result2 = calc.square_root(2, precision=3)
    print("Square root of 16:", result1)
    print("Square root of 2 with precision 3:", result2)
    assert result1 == 4.0
    assert result2 == "1.414"

def test_power():
    calc = EngineeringCalculator()
    result1 = calc.power(2, 3)
    result2 = calc.power(2, 0.5, precision=2)
    print("2 to the power of 3:", result1)
    print("2 to the power of 0.5 with precision 2:", result2)
    assert result1 == 8.0
    assert result2 == "1.41"

def test_log():
    calc = EngineeringCalculator()
    result1 = calc.log(100, base=10)
    result2 = calc.log(16, base=2, precision=3)
    print("Log base 10 of 100:", result1)
    print("Log base 2 of 16 with precision 3:", result2)
    assert result1 == 2.0
    assert result2 == "4.000"

def test_ln():
    calc = EngineeringCalculator()
    result = calc.ln(2.71828, precision=2)
    print("Natural log of 2.71828 with precision 2:", result)
    assert result == "1.00"

def test_trigonometric_functions():
    calc = EngineeringCalculator()
    result1 = calc.sin(90, angle_unit='degree', precision=3)
    result2 = calc.cos(0, angle_unit='degree')
    result3 = calc.tan(45, angle_unit='degree', precision=3)
    print("Sine of 90 degrees with precision 3:", result1)
    print("Cosine of 0 degrees:", result2)
    print("Tangent of 45 degrees with precision 3:", result3)
    assert result1 == "1.000"
    assert result2 == 1.0
    assert result3 == "1.000"

if __name__ == "__main__":
    test_square_root()
    test_power()
    test_log()
    test_ln()
    test_trigonometric_functions()