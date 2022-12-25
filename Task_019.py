# Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа разделителя используйте пробел.

nums = input('Введите числа через пробел: ').split(' ')
print(nums)
max_n = int(nums[0])
min_n = int(nums[0])
for i in range(len(nums)):
    if int(nums[i]) > max_n:
        max_n = int(nums[i])
    if int(nums[i]) < min_n:
        min_n = int(nums[i])
print(f'Большее => {max_n}, меньшее => {min_n}')

# использование map
list_num = list(map(int, nums)) # map итерирует nums и пременяет метод int к каждому элементу nums
print(list_num)
print(f'Большее => {max(list_num)}, меньшее => {min(list_num)}')