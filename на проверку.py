from datetime import datetime

time_now = datetime.now().date()
time_print = datetime.strftime(time_now,'%d.%m.%Y')

note = [#{'имя' : 'Алексей','название' : 'Список покупок',             # список словарей по умолчанию
        # 'описание' : 'Купить продукты на неделю',
        # 'статус' : 'Отложено',
        # 'deadline' : 'Заметка закончится через 60 дней'},
        #{'имя' : 'Мария','название' : 'Учёба',
        # 'описание' : 'Подготовиться к экзамену',
        # 'статус' : 'В процессе',
        # 'deadline' : 'Заметка закончится сегодня'}
        ]
my_list = {}                    # создаём словарь для новых данных

End = 'Выполнено'              # создаём переменные
go = 'В процессе'
post = 'Отложено'

def status():
    if not note:
        print('Список заметок пуст.')
        return
    while True:
        change_status = input('Желаете изменить статус заметки? (да/нет): ').lower()
        if change_status == 'нет':
            print('Хорошо, до встречи!')
            break
        if change_status != 'да':
            print('Вы ввели неверное значение. Введите "да" или "нет".')
            continue

        shou_notes()
        change_input = input('Выберите название заметки, в которой надо изменить статус: ').lower()
        #found = False
        for my_list in note:
            if my_list['название'].lower() == change_input:
                print(f'Текущий статус заметки: {my_list["статус"]}')
                print(' Выполнено  - 1', '\n', 'В процессе - 2', '\n', 'Отложено   - 3')
                change_value = input('Введите значение: ')
                if change_value == '1':
                    my_list['статус'] = End
                elif change_value == '2':
                    my_list['статус'] = go
                elif change_value == '3':
                    my_list['статус'] = post
                else:
                    print('Введено неверное значение.')
                    continue
                print(f'Новый статус: {my_list["статус"]}')
                found = True
                break
        #if not found:
            print('Заметка с таким названием не найдена.')

def del_notes():
    while True:                                            # создаём функцию для удаления
        del_notes = input('Желаете удалить заметку?(да/нет): ').lower()  # с поиощью функции .lower
        if del_notes == 'нет':                                   # делаем ввод не чувствительным к регистру
            print('Отлично! Всего доброго!')
            break
        if del_notes == 'да':
            print('\nПриступим!')
            shou_notes()
            del_notes_input = input('Ведите имя пользователя или название заметки для удаления: ').lower()
            for my_list in note:
                if my_list['имя'] == del_notes_input or my_list['название'] == del_notes_input:
                    ask = input('Заметка найдена! Вы уверены в удалении?(да/нет): ').lower()
                    if ask == 'да':
                        note.remove(my_list)
                        print('Заметка удалена!')
                        break
                    elif ask == 'нет':
                        print('хорошо')
                        break
                    else:
                        print('Ошибка! Используйте только (да/нет)')
                        continue
                else:
                    print('Заметка не найдена!')
                    continue

def shou_notes():
    print('\nВаши заметки:')                              # создаём функцию для финальной печати всего списка заметок
    for my_list in note:
        print(f'Имя: {my_list['имя']}')
        print(f'Название заметки: {my_list['название']}')
        print(f'Описание заметки: {my_list['описание']}')
        print(f'Статус заметки:  {my_list['статус']}')
        print(f'Время истечения: {my_list['deadline']}')

print('Приветствую в менеджере заметок!')
print(f'     Сегодня: {time_print}')
while True:                                         # основной цикл для создания заметок
    new_titles = input('Желаете создать новую заметку?(да/нет): ').lower()
    if new_titles == 'нет':
        print('Отлично!')
        break
    elif new_titles == 'да':
        print('Отлично приступим!')
    else:
        print('Ошибка! Используйте только (да/нет).')
        continue

    while True:                             # вложенный цикл для имени пользователя
        name_input = input('Введите Имя пользователя: ')
        if name_input == '':
            print('Ошибка! Имя пользователя не может быть пустым!')
            continue

        while True:                         # вложенный цикл для создания заметки и описания
            title_input = input('Введите название заметки: ').lower()
            description_input = input('Введите описание заметки: ').lower()
            if title_input == '' or description_input == '':
                print('Ошибка! "название" и "опиcание" не могут быть пустыми!')
                continue
            while True:
                status = input('Введите статус заметки (новая, в процессе, выполнено): ').lower()
                if status == 'новая' or status == 'в процессе'  or status == 'выполнено':
                    pass
                else:
                    print('Ошибка! Не верный ввод используйте (новая, в процессе, выполнено)')
                    continue

                while True:                             # вложенный цикл для работы со временим
                    try:
                        time_input = input('Введите дату окончания заметки в формате(дд.мм.гггг): ')
                        data_new = datetime.strptime(time_input,'%d.%m.%Y').date()
                        data_check = (data_new - time_now).days
                        print(data_new , time_print)
                    except ValueError:
                        print('Ошибка! Не верны формат даты! Введите в формате (дд.мм.гггг)')
                    if data_check == 0:
                        deadline = 'Заметка закончится сегодня!'
                        break
                    if data_check > 0:
                        deadline = f'Заметка закончится через {data_check} дней'
                        break
                    if data_check < 0:
                        print('Ошибка! Дата окончания не может быть меньше текущей!')
                        continue
                my_list = {'имя': name_input,                 # создаём словарь с данными
                           'название': title_input,
                           'описание': description_input,
                           'статус' : status,
                           'deadline': deadline}
                note.append(my_list)                           # добавляем словарь в список
                break
            break
        break
del_notes()          # вызываем функцию удаления заметок
status()
shou_notes()         # вызываем функцию демонстрации заметок