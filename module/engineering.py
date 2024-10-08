from .basic import Calculator
import math
from .utils import convert_to_radians
from typing import Union, Any

class EngineeringCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def square_root(self, x: float, **kwargs: Any)-> Union[float, str]:
        try:
            result = math.sqrt(x)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def power(self, x: float, y: float, **kwargs: Any)-> Union[float, str]:
        try:
            result = math.pow(x, y)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def log(self, x: float, base: float =10, **kwargs: Any)-> Union[float, str]:
        try:
            result = math.log(x, base)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def ln(self, x: float, **kwargs: Any):
        try:
            result = math.log(x)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def sin(self, theta: float, **kwargs: Any)-> Union[float, str]:
        try:
            theta = convert_to_radians(theta, kwargs.get('angle_unit', 'radian'))
            result = math.sin(theta)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def cos(self, theta: float, **kwargs: Any)-> Union[float, str]:
        try:
            theta = convert_to_radians(theta, kwargs.get('angle_unit', 'radian'))
            result = math.cos(theta)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def tan(self, theta: float, **kwargs: Any)-> Union[float, str]:
        try:
            theta = convert_to_radians(theta, kwargs.get('angle_unit', 'radian'))
            result = math.tan(theta)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"
        
# 테스트 코드
if __name__ == "__main__":
    calc = EngineeringCalculator()

    # 테스트 데이터
    x = 16
    y = 2
    theta = 30

    # 제곱근 테스트
    print("제곱근:", calc.square_root(x))

    # 거듭제곱 테스트
    print("거듭제곱:", calc.power(x, y))

    # 로그 테스트 (기본값은 밑이 10)
    print("로그(base 10):", calc.log(x))

    # 자연로그 테스트
    print("자연로그:", calc.ln(x))

    # 사인 테스트 (각도 단위: 도)
    print("사인 (도 단위):", calc.sin(theta,return_float="True", angle_unit='degree'))

    # 코사인 테스트 (각도 단위: 도)
    print("코사인 (도 단위):", calc.cos(theta,return_float="True", angle_unit='degree'))

    # 탄젠트 테스트 (각도 단위: 도)
    print("탄젠트 (도 단위):", calc.tan(theta, return_float="True",angle_unit='degree'))