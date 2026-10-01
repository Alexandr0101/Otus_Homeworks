from view import (get_response_num, show_notification, check_lastname, check_firstname, show_contact)
from model import (open_file, is_contact_in_contacts, get_contact, add_contact, get_contacts_and_indexes, delete_contact)

toggle = True
while toggle:
    result = get_response_num()
    if result == '6':
        show_notification(result)
        toggle = False

    if result == '1':
        contact_list = open_file()
        show_contact(contact_list)
        continue

    if result == '2':
        last_name = check_lastname(True)
        if last_name == '1':
            continue

        first_name = check_firstname()






    #
    # elif response_num == '2':
    #
    #     lastname = check_lastname()
    #     if lastname is None:
    #         continue
    #
    #     firstname = check_firstname()
    #     if firstname is None:
    #         continue
    #
    #     check_contact = is_contact_in_contacts(lastname, firstname)
    #     if check_contact == True:
    #         print(f'Контакт {lastname} {firstname} уже существует')
    #         continue
    #
    #     phonenum = check_phone_num()
    #     if phonenum is None:
    #         continue
    #
    #     result = add_contact(lastname, firstname, phonenum)
    #     print(f'Контакт {lastname} {firstname} успешно добавлен')
    #
    # elif response_num == '3':
    #     lastname = check_lastname()
    #     if lastname is None:
    #         continue
    #
    #     firstname = check_firstname()
    #     if firstname is None:
    #         continue
    #
    #     result = get_contact(lastname, firstname)
    #
    #     if len(result) == 0:
    #         print(f'Контакта {lastname} {firstname} не существует')
    #         continue
    #
    #     print(get_contact(lastname, firstname))
    #
    # elif response_num == '4':
    #     show_contacts = get_contacts_and_indexes()
    #     if show_contacts is None:
    #         continue
    #
    #     print(f'Контакт изменён на {show_contacts}')
    #
    # elif response_num == '5':
    #     deleted_contact = delete_contact()
    #     if deleted_contact is None:
    #         continue
    #
    #     print(deleted_contact)
    #
    # else:
    #     print(f'Ошибочный ввод: "{response_num}". Такого пункта меню не существует!')