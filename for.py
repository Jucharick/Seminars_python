# исключения while True
def input_day():
    while True:
        try:
            day = int(input('Введите день недели: '))
            if 0 < day < 8:
                return day
            else:
                print('Такого дня недели нет')
        except:
            print('Ну просили же ввести цифру, а ты?')

# week_day = input_day()


# for
my_list = [22, 52, 54, 72, 7, 80]

for item in my_list:
    if item < 10:
        print(item)
        break
else:
    print('Однозначных чисел в списке нет')

print()
for item in range(len(my_list)):
    print(item)

print()
for i in range(1, 10, 2): # range не перебирает индексы, а генерирует последовательность (и мы им можем пользоваться как перебором индексов)
    print(i)

print()

# while 
i = 0
while i <10: # можено перебирать бесконечно )))
    print(i)
    i+=1