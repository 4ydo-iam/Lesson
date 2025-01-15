from datetime import datetime                   # берём библиотеку datetime и выводим на экран текущею дату и время

data_today = datetime.now()
data_ = data_today.strftime('%d.%m.%Y')
print('Приветствую, сегодня :','\n',data_)

                                                  # запрашиваем у пользователя дату окончания заголовка,
                                                  # преобразуем его в формат даты
                                                  # создаём цик с обработкой ошибок -
                                                  # при неверном вводе программа сообщает об этом
                                                  # и возвращает в начало цикла
while True:
    data1_ = input('Введите дату окночания заметки, в формате (день.месяц.год): ')
    try :
        #datetime.strptime(data1_, "%d.%m.%Y")
        data11_ = datetime.strptime(data1_, '%d.%m.%Y')
        data_today = datetime.strptime(data_,'%d.%m.%Y')
        break
    except ValueError:
        print('Дата некорректна')
data_check = (data11_ - data_today).days

if data_check == 0:                                 # выводим разницу дней
    print('Заметка сегодня закончится!')
elif data_check > 0:
    print('До конца заметки:',data_check,'дней')
elif data_check < 0:
    print('Заметка закончилась :',-data_check,'дней назад!')