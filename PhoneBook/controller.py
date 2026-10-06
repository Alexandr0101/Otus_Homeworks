from view import (get_response_num, show_notification,
                  check_lastname, check_firstname, check_phone_num,
                  show_contact, select_contact)

from model import (open_file, is_contact_in_contacts,
                   get_contact, add_contact, change_contact,
                   delete_contact, Contact)

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

        first_name = check_firstname(True)
        if first_name == '1':
            continue

        check_contact = is_contact_in_contacts(last_name, first_name)
        if check_contact:
            show_notification('C', last_name=last_name, first_name=first_name)
            continue

        phone_num = check_phone_num(True)
        if phone_num == '1':
            continue

        new_contact = Contact(last_name, first_name, phone_num)

        show_notification('E', last_name, first_name)
        continue

    if result == '3':
        last_name = check_lastname(True)
        if last_name == '1':
            continue

        first_name = check_firstname(True)
        if first_name == '1':
            continue

        result = get_contact(last_name, first_name)

        if len(result) == 0:
            show_notification('G', last_name, first_name)
            continue

        show_contact(result)

    if result == '4':
        contact_list = open_file()

        index_contact = select_contact(contact_list)
        if index_contact == '0':
            continue

        last_name = check_lastname(True)
        if last_name == '1':
            continue

        first_name = check_firstname(True)
        if first_name == '1':
            continue

        phone_num = check_phone_num(True)
        if phone_num == '1':
            continue

        final = change_contact(index_contact, last_name, first_name, phone_num)
        if final == 'OK':
            show_notification('H', first_name = first_name, last_name = last_name, phone_num = phone_num)
        else:
            show_notification('I')



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