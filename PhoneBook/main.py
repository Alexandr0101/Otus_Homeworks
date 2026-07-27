from functions import (open_file, open_and_save, add_contact, check_lastname, check_firstname,
                       check_phone_num, is_contact_in_contacts, get_contact, get_contacts_and_indexes, delete_contact)

while True:
    response_num = int(input("""Привет:) Добро пожаловать в телефонный справочник!
    Показать все контакты -> введи 1: 
    Создать контакт -> введи 2: 
    Найти контакт -> введи 3:  
    Изменить контакт -> введи 4:  
    Удалить контакт -> введи 5: 
    Открыть файл -> введи 6: 
    Сохранить файл -> введи 7: 
    Для выхода -> введи 8: 
    """))
    if response_num == 8:
        print('Пока')
        break
    elif response_num == 1:
        print(open_file())
    elif response_num == 2:

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

    elif response_num == 3:
        lastname = check_lastname()
        if lastname is None:
            continue

        firstname = check_firstname()
        if firstname is None:
            continue

        print(get_contact(lastname, firstname))

    elif response_num == 4:
        show_contacts = get_contacts_and_indexes()
        if show_contacts is None:
            continue

        print(f'Контакт изменён на {show_contacts}')

    elif response_num == 5:
        deleted_contact = delete_contact()
        if deleted_contact is None:
            continue

        print(deleted_contact)
    elif response_num == 6:
        open_file()
    elif response_num == 7:
        result = open_and_save()
        if result == 'Success':
            print('Файл успешно сохранён\n')