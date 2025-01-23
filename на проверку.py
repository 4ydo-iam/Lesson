my_list = {}

note = []#{'имя' : 'Алексей'},
        #{'заметка' : 'Купить продукты на неделю'},
        #{'статус': 'Новая'},
        #{'дата создания':'27.01.2025'},
        #{'дедлайн': '30.01.2025'}
        #]

print('Добро пожаловать в менеджер заметок!')
print(f'      Сегодня {data_}')

while True:
    ask_add_titles = input('Желаете создать новую заметку? (да/нет): ')
    if ask_add_titles == 'да':
        print('Приступим!')
    elif ask_add_titles == 'нет':
        print('       Всего хорошего!')
        break
    else:
        print('Ошибка! Не верный ввод используйте (да/нет')
        continue
    while True:
        name_input = input('Введите имя пользователя: ')
        my_list['имя'] = name_input
        if name_input == '':
            print('Ошибка! Имя не может быть пустым!')
            continue                                                                        # print(my_list)
        while True:
            greate_titles = input('Введите название заметки: ')
            my_list['заметка'] = greate_titles
            if greate_titles == '':
                print('Ошибка! Поля "название" не может быть пустым.')
                continue
            while True:
                statys_input = input('Введите статус заметки (новая, в процессе, выполнено) :')
                if statys_input == 'новая' or statys_input == 'в процессе' or statys_input == 'выполнено':
                    my_list['статус'] = statys_input
                else:
                    print('Ошибка! Введите (новая, в процессе, выполнено)')
                    continue
                while True:
                    greate_date = input('Введите дату окончания заметки в формате (дд.мм.гггг)')
                    my_list['дата создания'] = data_
                    try:
                        data_format = datetime.strptime(greate_date,'%d.%m.%Y').date()
                        data_deadline = (data_format - now_date).days
                        if data_deadline == 0:
                            my_list['дедлайн'] = 'заявка закончится сегодня'
                        if data_deadline > 0:
                            my_list['дедлайн'] = f'До конца заметки {data_deadline} дней'

                        if data_deadline < 0:
                            print('Ошибка! Дата создания не может быть меньше текущей даты!')
                            continue
                    except ValueError:
                        print('Ошибка! Не верный формат даты, используйте формат (дд.мм.гггг)')

                    break
                break
            break
        break
    note.append(my_list)
print(note)
print('\nВаши заметки')
for my_list in note:
    print(f'Имя пользователя: ', my_list['имя'])
    print(f'Название заметки ', my_list['заметка'])
    print(f'Статус ', my_list['статус'])
    print(f'Дата создания ' , my_list['дата создания'])
    print(f'Дата окончания ' , my_list['дедлайн'])