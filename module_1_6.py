my_dict = {'Masha': 2000 , 'Petya': 1999 , 'Max': 1997}
print(my_dict)

print(my_dict ['Max']) #вывести значение опредиленого ключа

print (my_dict.get('Petya', 'Пользователь не найден!'))
print (my_dict.get('Lena', 'Пользователь не найден!'))

my_dict.update({'Sasha': 1987, 'Oleg': 1999})
print(my_dict)

my_dict.pop('Sasha')
print(my_dict)

#my_dict ['viktor'] = 1990
#print(my_dict) #добавить в словарь новый ключь и значение

my_set_ = {1, 2, 3, 4, 2, 1, 3, 4, 7}
print(my_set_)

my_set_.add ("hello")
my_set_.add (2.2)
my_set_.discard(2)
print(my_set_)

