import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from module.basic import Calculator

def test_add():
    calc = Calculator()
    result1 = calc.add(1, 2, 3)
    result2 = calc.add(1.5, 2.5, return_float=True)
    print("Addition result (1, 2, 3):", result1)
    print("Addition result with float (1.5, 2.5):", result2)
    assert result1 == 6
    assert result2 == 4.0

def test_subtract():
    calc = Calculator()
    result1 = calc.subtract(10, 5)
    result2 = calc.subtract(10.5, 2.5, return_float=True)
    print("Subtraction result (10, 5):", result1)
    print("Subtraction result with float (10.5, 2.5):", result2)
    assert result1 == 5
    assert result2 == 8.0

def test_multiply():
    calc = Calculator()
    result1 = calc.multiply(2, 3, 4)
    result2 = calc.multiply(1.5, 2, return_float=True)
    print("Multiplication result (2, 3, 4):", result1)
    print("Multiplication result with float (1.5, 2):", result2)
    assert result1 == 24
    assert result2 == 3.0

def test_divide():
    calc = Calculator()
    result1 = calc.divide(10, 2)
    result2 = calc.divide(7, 2, return_float=True)
    result3 = calc.divide(10, 0)
    print("Division result (10, 2):", result1)
    print("Division result with float (7, 2):", result2)
    print("Division by zero (10, 0):", result3)
    assert result1 == 5
    assert result2 == 3.5
    assert result3 == "0으로 나눌 수 없습니다"

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()