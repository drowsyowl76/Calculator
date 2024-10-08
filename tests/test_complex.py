import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from module.complex import ComplexCalculator

def test_add():
    calc = ComplexCalculator()
    result1 = calc.add("1+2j", "2+3j")
    result2 = calc.add("1+1j", "-1-1j")
    print("Addition of 1+2j and 2+3j:", result1)
    print("Addition of 1+1j and -1-1j:", result2)
    assert result1 == complex(3, 5)
    assert result2 == complex(0, 0)

def test_subtract():
    calc = ComplexCalculator()
    result = calc.subtract("5+5j", "2+3j")
    print("Subtraction of 5+5j and 2+3j:", result)
    assert result == complex(3, 2)

def test_multiply():
    calc = ComplexCalculator()
    result = calc.multiply("1+2j", "2+3j")
    print("Multiplication of 1+2j and 2+3j:", result)
    assert result == complex(-4, 7)

def test_divide():
    calc = ComplexCalculator()
    result1 = calc.divide("4+2j", "2+1j")
    result2 = calc.divide("1+1j", "0+0j")
    print("Division of 4+2j by 2+1j:", result1)
    print("Division of 1+1j by 0:", result2)
    assert result1 == complex(2, 0)
    assert result2 == "0으로 나눌 수 없습니다"

def test_magnitude():
    calc = ComplexCalculator()
    result = calc.magnitude("3+4j")
    print("Magnitude of 3+4j:", result)
    assert result == 5.0

def test_argument():
    calc = ComplexCalculator()
    result = calc.argument("1+1j")
    print("Argument of 1+1j:", result)
    assert result == pytest.approx(0.785398, 0.01)

def test_to_polar():
    calc = ComplexCalculator()
    result = calc.to_polar("1+1j")
    print("Polar form of 1+1j:", result)
    assert result == (pytest.approx(1.414213, 0.01), pytest.approx(0.785398, 0.01))

def test_to_rectangular():
    calc = ComplexCalculator()
    result = calc.to_rectangular(1, 0.785398)
    print("Rectangular form of polar coordinates (1, 0.785398):", result)
    assert result == pytest.approx(complex(0.70710678118, 0.70710678118), rel=1e-6)

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_magnitude()
    test_argument()
    test_to_polar()
    test_to_rectangular()