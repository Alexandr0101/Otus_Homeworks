def open_file() -> list[str]:
    """open file or create and open file"""
    with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt', 'a+') as f:
        f.seek(0)
        return f.readlines()

def is_contact_in_contacts(lastname: str, firstname: str) -> bool:
    contacts = open_file()
    for i in contacts:
        if lastname in i.split() and firstname in i.split():
            return True
    return False

def get_contact(lastname : str, firstname: str,) -> [str]:
    contacts_list = open_file()
    count = 0
    contacts = []
    for i in contacts_list:
        if lastname in i.split() and firstname in i.split():
            count += 1
            contacts.append(f'{count}: {i}\n')
    return contacts

def add_contact(last_name: str, first_name: str, phone_num: str):
    file = open_file()
    file.append(f'{last_name} {first_name} {phone_num};\n')
    with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt', 'w') as f:
        f.writelines(file)

def get_contacts_and_indexes()-> str | None:
    result = open_file()
    for index, line in enumerate(result):
        print(index + 1, line)
    real_index = 0
    while True:
        check_num = input('Введи номер строки или 0 для выхода: ')
        if check_num == '0':
            return None

        if not check_num.isdigit():
            print('Номер строки должен состоять только из цифр!')
            continue

        real_index = int(check_num) -1
        if real_index > len(result)-1:
            print(f'Номера строки {check_num} не существует!')
            continue
        break
    lastname = check_lastname()
    if lastname is None:
        return None

    firstname = check_firstname()
    if firstname is None:
        return None

    phone_num = check_phone_num()
    if phone_num is None:
        return None

    result[real_index] = f'{lastname} {firstname} {phone_num}\n'
    with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt', 'w') as f:
        f.writelines(result)
    return result[real_index]


def delete_contact():
    result = open_file()
    for index, line in enumerate(result):
        print(index + 1, line)
    real_index = 0
    while True:
        check_num = input('Введи номер строки или 0 для выхода: ')
        if check_num == '0':
            return None

        if not check_num.isdigit():
            print('Номер строки должен состоять только из цифр!')
            continue

        real_index = int(check_num) - 1
        if real_index > len(result) - 1:
            print(f'Номера строки {check_num} не существует!')
            continue
        break

    while True:
        response = input(f'Точно хочешь удалить контакт {result[real_index]} ?'
                         f'Введи 1 для удаления или 2 для выхода')

        if response == '2':
            return None


        if response == '1':
            deleted_contact = result[real_index]
            del result[real_index]
            with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt', 'w') as f:
                f.writelines(result)
            return  f'Контакт {deleted_contact} удалён!'

        print('Введи 1 или 2!')
        continue