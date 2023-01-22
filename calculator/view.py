# взаимодействие с пользователем - ввод и вывод в консоль
import view


def view_data(data):
    print(f'result = {data}')

def get_type():
    num_type = int(input('Choose 1 or 2 (1 - int, 2 - complex): '))
    return num_type

def get_value_int():
    return int(input('value = '))

def get_value_complex():
    return complex(input('value = '))

def get_sign():
    return input('Select a sign: ')