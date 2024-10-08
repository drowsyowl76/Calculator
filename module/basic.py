from .utils import round_result
from functools import reduce

class Calculator:
    def __init__(self):
        pass

    def kwargs_apply(self, result, **kwargs):
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

    def add(self, *args, **kwargs):
        try:
            result = sum(args)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def subtract(self, *args, **kwargs):
        try:
            result = reduce(lambda x, y: x - y, args)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def multiply(self, *args, **kwargs):
        try:
            result = reduce(lambda x, y: x * y, args)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def divide(self, *args, **kwargs):
        try:
            result = reduce(lambda x, y: x / y, args)
            return self.kwargs_apply(result, **kwargs)
        except ZeroDivisionError:
            return "0으로 나눌 수 없습니다"
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"