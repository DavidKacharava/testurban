my_dict = {'Vasya':1975,'Egor':1999,'Masha':2002}
print(my_dict)
print(my_dict['Masha'])
print(my_dict.get('David'))         #get возврашает значение по указанному ключу , если нет сушествующего ключа  он просто вернет none
a = my_dict.pop('Egor')             #Метод «pop» как бы вытаскивает из словаря ключ и значение
print(a)
my_dict.update({'Kamila': 1981,     #update обновляет сразу несколько ключей и значений
                'Artem':1915})
print(my_dict)


my_set = {1, 'apple', 42.314}
print(my_set)
my_set.add(13)                      #add добавляет элемент в множества
my_set.add( (5, 6, 1.6))
my_set.discard(1)
print(my_set)











