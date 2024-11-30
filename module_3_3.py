#Создайте функцию print_params(a = 1, b = 'строка', c = True),
#которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print()
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

#Создайте список values_list с тремя элементами разных типов.
values_list = [2, 'столбец', False]

#Создайте словарь values_dict с тремя ключами, соответствующими
# параметрам функции print_params, и значениями разных типов.
values_dict = {'a': 3, 'b': 'ячейка', 'c': True}

print()
print_params(*values_list)
print_params(**values_dict)

#Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = [54.32, 'Строка']

#Проверьте, работает ли print_params(*values_list_2, 42)
print()
print_params(*values_list_2, 42)