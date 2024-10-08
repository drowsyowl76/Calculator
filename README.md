# 계산기 패키지

이 패키지는 간단한 계산기 (`Calculator`)와 공학용 계산기 (`EngineeringCalculator`), 복소수 계산기 (`ComplexCalculator`)를 제공합니다. 이 패키지를 사용하여 기본적인 사칙연산부터 고급 공학 연산까지 수행할 수 있습니다.

## 파일 설명

- `__init__.py`: 패키지 초기화 파일로, 필요한 클래스와 함수를 임포트하여 패키지 레벨에서 사용할 수 있도록 합니다.
- `basic.py`: 기본 계산기 클래스 (`Calculator`)가 포함되어 있으며, 덧셈(`add`), 뺄셈(`subtract`), 곱셈(`multiply`), 나눗셈(`divide`)과 같은 기본적인 사칙연산 기능을 제공합니다.
- `engineering.py`: 공학용 계산기 클래스 (`EngineeringCalculator`)가 포함되어 있으며, 제곱근(`square_root`), 거듭제곱(`power`), 로그(`log`), 자연로그(`ln`), 
   삼각 함수(`sin, cos, tan`)와 같은 고급 연산 기능을 제공합니다.
   `complex.py`: 복소수 계산기 클래스 (`ComplexCalculator`)가 포함되어 있으며, 복소수 덧셈(`add`), 뺄셈(`subtract`), 곱셈(`multiply`), 나눗셈(`divide`), 
   복소수의 절대값(`magnitude`) 및 편각 계산(`argument`), 직교 좌표계(`to_polar`)와 극 좌표계 간의 변환 기능(`to_rectangular`)을 제공합니다. 
   인수는 'a+bj' 또는 'a-bj' 형식의 문자열이어야 합니다.
- `utils.py`: 계산에 사용되는 유틸리티 함수들이 포함되어 있습니다. 결과 반올림(`round_result`)과 각도 변환(`convert_to_radians`) 함수가 있습니다.

# 사용 예시

## 기본 계산기
```python
from calculator import Calculator

calc = Calculator()
print(calc.add(1, 2, 3))  # 출력: 6
print(calc.subtract(10, 5))  # 출력: 5
print(calc.multiply(2, 4, 6))  # 출력: 48
print(calc.divide(10, 2))  # 출력: 5
```

## 공학용 계산기
```python
from calculator import EngineeringCalculator

eng_calc = EngineeringCalculator()
print(eng_calc.square_root(16))  # 출력: 4.0
print(eng_calc.power(2, 3))  # 출력: 8.0
print(eng_calc.log(100, base=10))  # 출력: 2.0
print(eng_calc.sin(30, angle_unit='degree'))  # 출력: 0.5
```

## 복소수 계산기
```python
from calculator import ComplexCalculator

comp_calc = ComplexCalculator()
print(comp_calc.add("1+2j", "3+4j"))  # 출력: (4+6j)
print(comp_calc.magnitude("3+4j"))  # 출력: 5.0
print(comp_calc.argument("1+1j"))  # 출력: 0.7853981633974483 (라디안)
print(comp_calc.to_polar("1+1j"))  # 출력: (1.4142135623730951, 0.7853981633974483)
```


