# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#  Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

ls = [2, 3, 5, 9, 3]
a = 0

for i in range(len(ls)):
    if i % 2 == 1:
        a += ls[i]
print(a)
