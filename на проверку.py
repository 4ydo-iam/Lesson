from datetime import datetime

time_now = datetime.now().date()
time_print = datetime.strftime(time_now,'%d.%m.%Y')

note = [{'имя' : 'Вова','название' : 'Учёба','описание' : 'Подготовка к экзамену'}]
my_list = {}

#def name():
#        name_input = input('Введите имя пользователя: ')
#        if name_input == '':
#            print('Имя не может быть пустым!')
#        else:
#            print(f'Приветствую{name_input}!')
#            return name_input
#def titles():
#    while True:
#        titl_input = input('Введите название заметки: ')
#        description_input = input('Введите описание заметки: ')
#        if titl_input == '' or description_input == '':
#            print('Ошибка! "название" и "описание" не могут быть пустыми!')
#            continue
def del_notes():
    notes = note #[{'имя': 'Вова', 'название': 'Учёба', 'описание': 'Подготовка к экзамену'}]
    print(notes)
    while True:
        del_notes = input('Желаете удалить заметку?: ')
        if del_notes == 'нет':
            print('Отлично! Всего доброго!')
            break
        if del_notes == 'да':
            print('Приступим!')
            del_notes_input = input('Ведите имя пользователя или название заметки для удаления: ')
            for my_list in note:
                if my_list['имя'] == del_notes_input or my_list['название'] == del_notes_input:
                    ask = input('Заметка найдена! Вы уверены в удалении?(да/нет): ')
                    if ask == 'да':
                        note.remove(my_list)
                        print('Заметка удалена!')
                        print(note)
                    elif ask == 'нет':
                        print('хорошо')
                        break
                    else:
                        print('Ошибка! Используйте только (да/нет)')
                        continue
            if del_notes_input not in note:
                print('Заметка не найдена!')
                continue

        break
print('Приветствую в менеджере заметок!')
print(f'Сегодня: {time_print}')
while True:
    new_titles = input('Желаете создать новую заметку?(да/нет)')
    if new_titles == 'нет':
        print('Отлично!')
        break
    elif new_titles == 'да':
        print('Отлично приступим!')
    else:
        print('Ошибка! Используйте лиш (да/нет).')
        continue
    while True:
        name_input = input('Введите Имя пользователя:')
        if name_input == '':
            print('Ошибка! Имя пользователя не может быть пустым!')
            continue

        while True:
            title_input = input('Введите название заметки: ')
            description_input = input('Введите описание заметки: ')
            if title_input == '' or description_input == '':
                print('Ошибка! "название" и "опиcание" не могут быть пустыми!')
                continue

            while True:
                try:
                    time_input = input('Введите дату окончания заметки в формате(дд.мм.гггг): ')
                    data_new = datetime.strptime(time_input,'%d.%m.%Y').date()
                    data_check = (data_new - time_now).days
                    print(data_new , time_print)
                except ValueError:
                    print('Ошибка! Не верны формат даты! Введите в формате (дд.мм.гггг)')

                if data_check == 0:
                    status = 'Заметка закончится сегодя!'
                    break
                if data_check > 0:
                    status = f'Заметка закончится через {data_check} дней'
                    break
                if data_check < 0:
                    print('Ошибка! Дата окончания не может быть меньше текущей!')
                    continue
            my_list = {'имя': name_input, 'название': title_input, 'описание': description_input, 'статус': status}
            note.append(my_list)
            print(note)
            break
        break
del_notes()










#print(note)





    #my_list = {'имя': name(), 'название': titl_input, 'описание': description_input}
