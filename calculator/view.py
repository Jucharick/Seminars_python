# взаимодействие с пользователем - ввод и вывод в консоль
import view


def view_data(data):
    print(f'result = {data}')

def get_value(a):
    if a == 1:
        return int(input('value = '))
    else:
        return complex(input('value = '))

def get_sign():
    return input('Select a sign: ')