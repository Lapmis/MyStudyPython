# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases
count = 0
lst = []
with open('test_file/task_3.txt', encoding='utf-8') as file:
    for line in file.readlines():
        if line == "\n":
            lst.append(count)
            count = 0
            continue
        count += int(line)
lst.sort(reverse=1)
three_most_expensive_purchases = sum(lst[:3])

# Здесь пишем код

assert three_most_expensive_purchases == 202346
