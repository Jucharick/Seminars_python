# Напишите программу, которая отсортирует отдельно элементы массива с четными и нечетными значениями.
# Все элементы с нечетными значениями нужно отсортировать по возрастанию, а элементы с четными значениями -
# по убыванию. При этом элементы каждой из групп (как четные, так и нечетные) должны занимать то же множество позиций



my_array = [219, 234, 890, 81, 73, 96]

even = [i for i in my_array if i%2==0] # четные
odd = [i for i in my_array if i%2!=0] # нечетные

print(my_array)
even.sort(reverse=True)
print(even)
odd.sort()
print(odd)

for index, value in enumerate(my_array):
    if value %2 == 0:
        my_array[index] = even.pop(0) # первый элемент списка even удаляем
    else:
        my_array[index] = odd.pop(0)

print(my_array)