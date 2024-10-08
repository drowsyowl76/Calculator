import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from module.basic import Calculator
from module.engineering import EngineeringCalculator
from module.complex import ComplexCalculator

if __name__ == "__main__":
    calc = Calculator()
    print("-------------Basic_Calculator_Example------------------")
    print(calc.add(1, 2, 3))  # 출력: 6
    print(calc.subtract(10, 5))  # 출력: 5
    print(calc.multiply(2, 4, 6))  # 출력: 48
    print(calc.divide(10, 2))  # 출력: 5
    print("-------------Engineering_Calculator_Example------------------")
    eng_calc = EngineeringCalculator()
    print(eng_calc.square_root(16))  # 출력: 4.0
    print(eng_calc.power(2, 3))  # 출력: 8.0
    print(eng_calc.log(100, base=10))  # 출력: 2.0
    print(eng_calc.sin(30, angle_unit='degree'))  # 출력: 0.5
    print("-------------Complex_Calculator_Example------------------")
    comp_calc = ComplexCalculator()
    print(comp_calc.add("1+2j", "3+4j","5+20j"))  # 출력: (4+6j)
    print(comp_calc.magnitude("3+4j"))  # 출력: 5.0
    print(comp_calc.argument("1+1j"))  # 출력: 0.7853981633974483 (라디안)
    print(comp_calc.to_polar("1+1j"))  # 출력: (1.4142135623730951, 0.7853981633974483)
    print(comp_calc.to_rectangular(1,45,angle_unit="degree"))
