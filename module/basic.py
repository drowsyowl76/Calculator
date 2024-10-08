from .utils import round_result
from functools import reduce
from typing import Any,Union

class Calculator:
    def __init__(self):
        pass

    def kwargs_apply(self, result: float, **kwargs: Any) -> Union[float, str]:
        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)
        
        if precision is not None:
            result = round_result(float(result), precision)
            result = f"{result:.{precision}f}"
        
        if return_float:
            result = float(result)
        elif precision is None:
            result = int(result)
        
        return result

    def add(self, *args:float, **kwargs: Any) -> Union[float, str]:
        try:
            result = sum(args)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def subtract(self, *args:float, **kwargs: Any) -> Union[float, str]:
        try:
            result = reduce(lambda x, y: x - y, args)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def multiply(self, *args:float, **kwargs: Any) -> Union[float, str]:
        try:
            result = reduce(lambda x, y: x * y, args)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def divide(self, *args:float, **kwargs: Any) -> Union[float, str]:
        try:
            result = reduce(lambda x, y: x / y, args)
            return self.kwargs_apply(result, **kwargs)
        except ZeroDivisionError:
            return "0으로 나눌 수 없습니다"
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"
        
    # 테스트 코드
if __name__ == "__main__":
    calc = Calculator()

    # 테스트 데이터
    x = 10
    y = 5
    z = 2

    # 덧셈 테스트
    print("덧셈:", calc.add(x, y, z))

    # 뺄셈 테스트
    print("뺄셈:", calc.subtract(x, y, z))

    # 곱셈 테스트
    print("곱셈:", calc.multiply(x, y, z))

    # 나눗셈 테스트
    print("나눗셈:", calc.divide(x, y))
    print("나눗셈 (0으로 나누기):", calc.divide(x, 0))