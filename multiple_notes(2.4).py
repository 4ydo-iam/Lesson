from datetime import datetime          # импортируем datatime для работы с блоком времени

name1 = []         # создаём переменные списка и словаря
title1 = {}
print('Добро пожаловать в "Менеджер заметок"')     # запрашиваем ввод данных у пользователя
while True:                                         # создаём цикл для повторного ввода данных и обработки ошибок
    a = input('Желаете создать новую заметку?(да/нет): ')
    if a == 'да':
        b = input('Введите имя пользователя: ')
        name1.append(b)
    elif a == 'нет':
        print('     Всего хорошего!','\n','Возвращайтесь по скорее!')
        break
    else:
        print('Не корректный ввод, используйте (да/нет)')
        continue
    b = True
    while b:                                # делаем вложенные циклы для повторного ввода и обработки ошибок
        key = input('Введите заголовок заметки: ')
        meaning = input('Введите описание заметки: ')
        if key == '' or meaning == '':
            print('Ошибка - строка, заголовок или описание пустые!','\n','        !!!Введите значение!!!')
            continue
        title1[key] = meaning
        while True:
            a = input('Желаете продолжить? (да/нет): ')
            if a == 'нет':
                b = False
                break
            if a == 'да':
                break
            while True:
                if a != 'да' or a != 'нет':
                    print('Не корректный ввод, введите (да/нет)')
                    break

    while True:
        data_ = datetime.now()   # вложенный цикл datetime выводит сегодняшнюю дату и запрашивает у пользователя дату
        data_today = datetime.strftime(data_,'%d.%m.%Y') # окончания, производит сравнение, показывает результат
        try:
            date_deadline = input('Введите дату окочания заметки в формате (день.месяц.год): ')
            date_final = datetime.strptime(date_deadline,'%d.%m.%Y')
            date_now = datetime.strptime(data_today,'%d.%m.%Y')
            break
        except ValueError:
            print('Дата введена не верно - используйте формат 00.00.0000')
    date_check = (date_final - date_now).days
    if date_check == 0:
        print('Заметка сегодня закончится!')
    elif date_check > 0:
        print('До конца заметки:',date_check,'дней')
    elif date_check < 0:
        print('Заметка закончилась :',-date_check,'дней назад!')
    print('Имя: ',*name1)
    print('Заголовок заметки: ',*list(title1.keys()))
    print('Описание заметки: ',*list(title1.values()))
    
# весь цикл будет повторяться пока пользователь не введёт "нет" на вопрос 'Желаете создать новую заметку?(да/нет): '
