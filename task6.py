# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

sp = [1.1, 1.2, 3.1, 5, 10.01]

ls = []
for i in sp:
    b = i % int(i)
    ls.append(b)
while 0 in ls:
    ls.remove(0)
print(round(max(ls) - min(ls), 2))
