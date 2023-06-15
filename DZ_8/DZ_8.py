# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .тхт. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находится в файле.
# 1. Программа должна выводить данные.
# 2. Программа должна сохранять данные в текстовом файле.
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи.
# 4. Использование функций, ваша программа не должна быть линейной.
# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или
# фамилию и Вы должны реализовать функционал для изменения и удаления данных.

# ф-ция чтения файла в список
def read_phonebook():
    file = open('PHONEBOOK.txt', 'r+', encoding='utf-8')
    phone_list = []
    file.seek(0)
    while True:
        line = file.readline().rstrip()
        phone_list.append(line)
        if not line:
            file.close()
            return phone_list[:len(phone_list)-1]

# ф-ция вывода тел. книги на экран
def print_phonebook():
    phones = read_phonebook()
    print('*' * 30)
    for line in phones:
        if line != '':
            print(line)
    print('*' * 30)

# поиск контакта по ФИО
def find_line():
    phones = read_phonebook()
    target = input('Найти: ')
    print('*' * 30)
    for phone in phones:
        if target in phone.split():
            print(phone)
    print('*' * 30)

# ф-ция добааления контакта
def add_line():
    new_line = input('Добавить: ')
    phones = read_phonebook()
    if new_line in phones:
        print('*' * 30)
        print('Такой контакт уже есть')
        print('*' * 30)
    else:
        phones.append(new_line)
    with open('PHONEBOOK.txt', 'w', encoding='utf-8') as file:
        for phone in phones:
            if phones.index(phone) == len(phones) - 1:
                file.write(phone)
            else:
                file.write(phone + '\n')

# ф-ция изменения контакта
def rewrite_line():
    phones = read_phonebook()
    new_phones = []
    target = input('Введите данные контакта (фамилия/имя/отчество/номер), который хотите изменить: ')
    new_phones = [phone for phone in phones if target in phone.split()] # в результате поиска можем получить несколько
    # контактов. найденные контакты будут пронумерованы и выведены на экран. пользователю будет предложено выбрать
    # нужный ему контакт по соответствующему номеру.
    print('Найдено контактов: ')
    if len(new_phones) > 0:
        print('*' * 30)
        for index, phone in enumerate(new_phones):
            print(f'{index + 1} : {phone}')
        print('*' * 30)
        choice = int(input('Введите номер контакта, который хотите изменить: '))
        if choice - 1 <= index:
            new_line = input('Введите новые данные: ')
            for index, phone in enumerate(phones):
                if phone == new_phones[choice - 1]:
                    phones[index] = new_line
            with open('PHONEBOOK.txt', 'w', encoding='utf-8') as file:
                for phone in phones:
                    if phones.index(phone) == len(phones) - 1: # если контакт последний в списке, то после его записи
                        # в файле не делаем перенос строки (иначе могут появится пустые строки в файле)
                        file.write(phone)
                    else:
                        file.write(phone + '\n')
    else:
        print('0')

# ф-ция удаления контакта
def delete_line():
    phones = read_phonebook()
    new_phones = []
    target = input('Введите данные контакта (фамилия/имя/отчество/номер), который хотите удалить: ')
    for phone in phones:
        if target in phone.split():
            new_phones.append(phone)
    print('Найдено контактов: ')
    if len(new_phones) > 0:
        print('*' * 30)
        for index, phone in enumerate(new_phones):
            print(f'{index + 1} : {phone}')
        print('*' * 30)
        choice = int(input('Введите номер контакта, который хотите удалить: '))
        if choice - 1 <= index:
            for index, phone in enumerate(phones):
                if phone == new_phones[choice - 1]:
                    phones.remove(phones[index])
            with open('PHONEBOOK.txt', 'w', encoding='utf-8') as file:
                for phone in phones:
                    file.write(phone + '\n')
    else:
        print('0')


while True:
    print('1 - Посмотреть телефонную книгу\n'
          '2 - Найти запись\n'
          '3 - Добавить запись\n'
          '4 - Изменить запись\n'
          '5 - Удалить запись\n'
          '0 - Выйти')
    choice = input('Введите номер команды: ')
    if choice == '1':
        print_phonebook()
        continue
    if choice == '2':
        find_line()
        continue
    if choice == '3':
        add_line()
        continue
    if choice == '4':
        rewrite_line()
        continue
    if choice == '5':
        delete_line()
        continue
    if choice == '0':
        break