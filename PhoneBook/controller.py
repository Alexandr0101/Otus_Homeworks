from view import (get_response_num, show_notification,
                  check_lastname, check_firstname, check_phone_num,
                  show_contact, select_contact, is_delete_contact)

from model import (open_file, is_contact_in_contacts,
                   get_contact, add_contact, change_contact,
                   delete_contact, get_contact_string, Contact)

toggle = True
while toggle:
    result = get_response_num()
    if result == '6':
        show_notification('AA')
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
        add_contact(new_contact)
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

    if result == '5':
        contact_list = open_file()
        index_contact = select_contact(contact_list)
        contact_string = get_contact_string(index_contact)
        user_response = is_delete_contact(contact_string)

        if user_response == '1':
            delete_contact(index_contact)
            show_notification('J', full_contact = contact_string)

        else:
            continue