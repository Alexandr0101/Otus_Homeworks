from functions import (open_file, add_contact, check_lastname, check_firstname,
                       check_phone_num, is_contact_in_contacts, get_contact, get_contacts_and_indexes, delete_contact)

while True:
    response_num = input("""Привет:) Добро пожаловать в телефонный справочник!
    Показать все контакты -> введи 1: 
    Создать контакт -> введи 2: 
    Найти контакт -> введи 3:  
    Изменить контакт -> введи 4:  
    Удалить контакт -> введи 5: 
    Для выхода -> введи 6: 
    """)
    if not response_num.isdigit():
        print('Выбор пункта меню должен состоять только из цифр!')
        continue

    if response_num == '6':
        print('Пока')
        break

    elif response_num == '1':
        print(open_file())

    elif response_num == '2':

        lastname = check_lastname()
        if lastname is None:
            continue

        firstname = check_firstname()
        if firstname is None:
            continue

        check_contact = is_contact_in_contacts(lastname, firstname)
        if check_contact == True:
            print(f'Контакт {lastname} {firstname} уже существует')
            continue

        phonenum = check_phone_num()
        if phonenum is None:
            continue

        result = add_contact(lastname, firstname, phonenum)
        print(f'Контакт {lastname} {firstname} успешно добавлен')

    elif response_num == '3':
        lastname = check_lastname()
        if lastname is None:
            continue

        firstname = check_firstname()
        if firstname is None:
            continue

        result = get_contact(lastname, firstname)

        if len(result) == 0:
            print(f'Контакта {lastname} {firstname} не существует')
            continue

        print(get_contact(lastname, firstname))

    elif response_num == '4':
        show_contacts = get_contacts_and_indexes()
        if show_contacts is None:
            continue

        print(f'Контакт изменён на {show_contacts}')

    elif response_num == '5':
        deleted_contact = delete_contact()
        if deleted_contact is None:
            continue

        print(deleted_contact)

    else:
        print(f'Ошибочный ввод: "{response_num}". Такого пункта меню не существует!')
