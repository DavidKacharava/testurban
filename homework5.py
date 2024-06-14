immutable_var = 1, 2, 'a' ,'b'
print(immutable_var)
#immutable_var[0] = 100
#print(immutable_var)
#  ошибка, кортеж не поддерживает обрашение по элементам, потому что они не изменяемые

mutable_list =[1,2,'a','b','c']
mutable_list[4] = 'Modified'
print(mutable_list)