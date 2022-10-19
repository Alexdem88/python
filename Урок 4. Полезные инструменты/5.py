# 5. Реализовать формирование списка, используя функцию range()
# и возможности генератора. В список должны войти чётные числа от 100 до 1000
# (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

my_list = [el for el in range(100, 1000) if el % 2 == 0]
print(reduce(lambda a,b:a*b,my_list))





