# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой
# строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X.

num = int(input('Введи число элементов: '))
num_list = [int(input(f'Введите элемент {i + 1}: ')) for i in range(num)]
print(num_list)
x_num = int(input('Введи число Х: '))
print(num_list.count(x_num))

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в
# первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых
# чисел Ai. Последняя строка содержит число X.

# num = int(input('Введи число элементов массива: '))
# x_num = int(input('Введи число Х: '))
# el_list = [int(input(f'Введите элемент массива {i + 1}: ')) for i in range(num)]
# num_dict = {x_num - el: el for el in
#             el_list}  # создаем словарь, в котором ключ - разница между числом X и значением в самом словаре
# print(num_dict.values())
# min_dif = min(num_dict.keys(), key=lambda i: i ** 2)  # находим наименьший ключ
# print(f'Ближайшее число в массиве к числу {x_num}: ', num_dict[min_dif])

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. Напишите программу, которая
# вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое
# содержит либо только английские, либо только русские буквы.

# dic = {1: ('a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r', 'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'),
#        2: ('d', 'g', 'д', 'к', 'л', 'м', 'п', 'у'),
#        3: ('b', 'c', 'm', 'p', 'б', 'г', 'ё', 'ь', 'я'),
#        4: ('f', 'h', 'v', 'w', 'y', 'й', 'ы'),
#        5: ('k', 'ж', 'з', 'х', 'ц', 'ч'),
#        8: ('j', 'x', 'ш', 'э', 'ю'),
#        10: ('q', 'z', 'щ', 'ф', 'ъ')}
#
# word = input('Введите слово: ')
# summ = 0
# for char in word:
#     for key in dic.keys():
#         if char in dic[key]:
#             summ += key
# print(summ)