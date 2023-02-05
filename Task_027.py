# Напишите программу вычисления арифметического выражения, заданного строкой.
# Используйте операции +, -, /, *
# Приоритет операций стандартный.

# Пример:
# 2+2 => 4
# 1+2*3 => 7
# 1-2*3 => -5
# 1+3+4*5/2 => 14
# 1+2*3 - 10/5 +1 => 6
# -1+2*3 - 10/5 +1 => 4
# -1+2*3 - 10/5 +1+1*4/2 +1 => 7

str = '-1+2*3 - 10/5 +1'
str= str.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('/', ' / ').replace('*', ' * ')
if str[1] == ('-'):
    str = '-' + str[3:]
print(str)
my_list = str.split()
print(my_list)

orig_example = my_list.copy()




# for фиксирует длину списка один раз и после del не проверяет длину списка снова (а она у нас уменьшается)
# while при каждой итерации проверяет длину списка



operation = {'+': lambda x, y: x+y,
             '-': lambda x, y: x-y,
             '*': lambda x, y: x*y,
             '/': lambda x, y: x/y,}

def calculate(operation_1, operation_2):
    i = 0
    while operation_1 in my_list or operation_2 in my_list:
        if my_list[i] in [operation_1, operation_2]:
            my_list[i - 1] = operation.get(my_list[i])(int(my_list[i - 1]), int(my_list[i + 1]))
            my_list.pop(i)
            my_list.pop(i)
        else:
            i+=1

while len(my_list)>1:
    calculate('*', '/')
    calculate('+', '-')

print(f'{" ".join(orig_example)} = {my_list[0]}')


# while len(my_list) > 1:
#     i = 0
#     while i < len(my_list):
#         if my_list[i] == '*':
#             my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
#             del my_list[i]
#             del my_list[i] # нам надо удалить элемент my_list[i+1], но после удаления my_list[i] (который равен *) my_list[i+1] станет my_list[i]
#         i+=1
#     print(my_list)

#     i = 0
#     while i < len(my_list):
#         if my_list[i] == '/':
#             my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
#             del my_list[i]
#             del my_list[i]
#         i+=1
#     print(my_list)

#     i = 0
#     while i < len(my_list):
#         if my_list[i] == '-':
#             my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
#             del my_list[i]
#             del my_list[i]
#         i+=1

#     i = 0
#     while i < len(my_list):
#         if my_list[i] == '+':
#             my_list[i-1] = int(my_list[i-1]) + int(my_list[i+1])
#             del my_list[i]
#             del my_list[i]
#         i+=1


print(my_list)


