# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

x = input('введите предложение')
words=x.split()
num=1
for w in words:
    print(f'#{num} {w[:10]}')
    num+=1





