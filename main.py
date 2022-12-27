import rational as rat
import complex_nums as cn
from logger import log_result as log

def calc():
    while True:
        type_nums = input("Вас приветсвует калькулятор! Укажите, с какими числами будем работать!\nВведите 'r' для рациональных чисел или 'с' для комплексных\n")
        if type_nums == 'r':
            first_num = input("Введите первое число(например 3/7): ")
            second_num = input("Введите второе число(например 3/7): ")
            operation = input("Выберите и введите желаемую операцию(+,-,*,/): ")
            print()
            result = rat.fract(first_num,second_num,operation)
        elif type_nums == 'c':
            first_num = input("Введите первое число(например 3+7j): ")
            second_num = input("Введите второе число(например 3+7j): ")
            operation = input("Выберите и введите желаемую операцию(+,-,*,/): ")
            print()
            result = cn.complex_num(first_num,second_num,operation)
        else:
            print("Неверная команда!")
        log(result)

        return (result)


print("Результат вычисления:  ",calc())

