# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
# Подсказка: используйте функцию range() и генератор.


my_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(my_list)
# or
print(f'Числа, который кратны 20 и 21 в списке с диапазоном от 20 до 240 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')