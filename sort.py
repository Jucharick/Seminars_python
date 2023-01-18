a = [1, 6, 5, 8, 3, 7]
a.sort()
print(a)


b = (3, 5, 6, 54, 3, 2)
new_b = sorted(b) # a.sort() не сортирует кортежи, для их сортировки можно использовать sorted() => возвращает список
print(new_b)

c = [12, 34, 567, 671]
new_c = sorted(c, reverse=True) # сортировка по убыванию
print(new_c)

