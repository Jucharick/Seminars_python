class Person:
    def __init__(self, name, height, color): # __ __ - магические методы )))
        self.name = name   # поля
        self.height = int(height)   # поля
        self.color = color  # поля

    def __eq__(self, __o: object) -> bool:
        if self.name == __o.name:
            return ('Тезки')
        else:
            return ('Не тезки')

    def hello(self):  # метод класса
        print(f'Меня зовут {self.name}, мой рост {self.height}')
    

ivan = Person('ivan', 190, 'brown')  # 'ivan', 190, 'brown' - аргументы
print(ivan.name, ivan.height, ivan.color)

vasy = Person('vasy', 180, 'green')
print(vasy.name, vasy.height, vasy.color)

ivan.hello()
vasy.hello()

print(ivan == vasy)  # триггер == -> срабатывает метод __eq__

