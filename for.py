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

week_day = input_day()