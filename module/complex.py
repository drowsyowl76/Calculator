from .basic import Calculator
from functools import reduce
import cmath
import re

class ComplexCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def parse_complex(self, value):
        if isinstance(value, str) and re.match(r'^-?\d+\.?\d*[+-]\d+\.?\d*[jJ]$', value):
            return complex(value)
        else:
            raise ValueError("정확한 형식이 아닙니다. 'a+bj' 또는 'a-bj' 형식의 문자열이어야 합니다.")

    def add(self, *args):
        try:
            args = [self.parse_complex(arg) for arg in args]
            return sum(args)
        except ValueError as e:
            return str(e)

    def subtract(self, *args):
        try:
            args = [self.parse_complex(arg) for arg in args]
            return reduce(lambda x, y: x - y, args)
        except ValueError as e:
            return str(e)

    def multiply(self, *args):
        try:
            args = [self.parse_complex(arg) for arg in args]
            return reduce(lambda x, y: x * y, args)
        except ValueError as e:
            return str(e)

    def divide(self, *args):
        try:
            args = [self.parse_complex(arg) for arg in args]
            return reduce(lambda x, y: x / y, args)
        except ZeroDivisionError:
            return "0으로 나눌 수 없습니다"
        except ValueError as e:
            return str(e)

    def magnitude(self, z):
        try:
            z = self.parse_complex(z)
            return abs(z)
        except ValueError as e:
            return str(e)

    def argument(self, z):
        try:
            z = self.parse_complex(z)
            return cmath.phase(z)
        except ValueError as e:
            return str(e)

    def to_polar(self, z):
        try:
            z = self.parse_complex(z)
            return cmath.polar(z)
        except ValueError as e:
            return str(e)

    def to_rectangular(self, r, theta):
        try:
            return cmath.rect(float(r), float(theta))
        except ValueError as e:
            return str(e)
    # 테스트 코드
if __name__ == "__main__":
    calc = ComplexCalculator()

    # 테스트 데이터
    complex1 = "3+4j"
    complex2 = "1-2j"
    complex3 = "-1+1j"

    # 덧셈 테스트
    print("덧셈:", calc.add(complex1, complex2, complex3))

    # 뺄셈 테스트
    print("뺄셈:", calc.subtract(complex1, complex2, complex3))

    # 곱셈 테스트
    print("곱셈:", calc.multiply(complex1, complex2, complex3))

    # 나눗셈 테스트
    print("나눗셈:", calc.divide(complex1, complex2))
    print("나눗셈 (0으로 나누기):", calc.divide(complex1, "0+0j"))

    # 크기(절댓값) 테스트
    print("크기:", calc.magnitude(complex1))

    # 각도(Argument) 테스트
    print("각도:", calc.argument(complex1))

    # 극좌표 변환 테스트
    print("극좌표 변환:", calc.to_polar(complex1))

    # 직교 좌표 변환 테스트
    r, theta = 5.0, cmath.pi / 4
    print("직교 좌표 변환:", calc.to_rectangular(r, theta))