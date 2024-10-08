from .basic import Calculator
import math
from .utils import convert_to_radians


class EngineeringCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def square_root(self, x, **kwargs):
        try:
            result = math.sqrt(x)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def power(self, x, y, **kwargs):
        try:
            result = math.pow(x, y)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def log(self, x, base=10, **kwargs):
        try:
            result = math.log(x, base)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def ln(self, x, **kwargs):
        try:
            result = math.log(x)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def sin(self, x, **kwargs):
        try:
            x = convert_to_radians(x, kwargs.get('angle_unit', 'radian'))
            result = math.sin(x)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def cos(self, x, **kwargs):
        try:
            x = convert_to_radians(x, kwargs.get('angle_unit', 'radian'))
            result = math.cos(x)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"

    def tan(self, x, **kwargs):
        try:
            x = convert_to_radians(x, kwargs.get('angle_unit', 'radian'))
            result = math.tan(x)
            return self.kwargs_apply(result, **kwargs)
        except Exception as e:
            return f"에러가 발생했습니다: {str(e)}"
