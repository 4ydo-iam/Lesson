

list_ = ['Алексей',
         {'Список покупок':'Купить продукты на неделю'},
         'Мария',
         {'Учёба':'Подготовиться к экзамену'}]
first = list_[0],list_[1]
second = list_[2],list_[3]
print(first)
print('Текущие заметки: ')
print('1.Имя: ',first[0],'\n',
      'Заголовок: ',*list_[1],'\n',
      'Описание: ',list_[1].get('Список покупок'))

print('2.Имя: ',list_[2],'\n',
      'Заголовок: ',*list_[3],'\n',
      'Описание: ',list_[3].get('Учёба'))
first1 = (list_[0],list_[1])
print(first1)
list_del = input('Введите для удаления: ')
while True:
    if list_del == 'Алексей':
        first1.pop