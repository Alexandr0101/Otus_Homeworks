def open_file() -> list[str]:
    """open file or create and open file"""
    with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt', 'a+') as f:
        f.seek(0)
        return f.readlines()

def open_and_save() -> str:
    """open and rewrite existing file"""
    contact_data = open_file()
    with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt', 'w') as f:
        f.writelines(contact_data)
        return 'Success'

def check_lastname() -> str | None:
    while True:
        lastname = input('Введи фамилию или 1 для выхода')

        if lastname == '1':
            return None

        if not lastname.isalpha():
             print('Фамилия должна состоять только из букв!'
                  'Введи фамилию или 1 для выхода')
             continue

        return lastname


def check_firstname() -> str | None:
    while True:
        first_name = input('Введи имя или 1 для выхода')

        if first_name == '1':
            return None

        if not first_name.isalpha():
            print('Имя должно состоять только из букв!'
                  'Введи имя или 1 для выхода')
            continue
        return first_name

def check_phone_num() -> str | None:
    while True:
        phone_num = input('Введи имя или 1 для выхода')

        if phone_num == '1':
            return None

        if not phone_num.isdigit():
            print('Номер телефона должен состоять только из цифр!'
                  'Введи номер или 1 для выхода')
            continue
        return phone_num

def is_contact_in_contacts(lastname: str, firstname: str) -> bool:
    with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt') as f:
        for i in f:

            if lastname in i.split() and firstname in i.split():
                return True

        return False

def add_contact(last_name: str, first_name: str, phone_num: str):
    file = open_file()
    file.append(f'{last_name} {first_name} {phone_num};\n')
    with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt', 'w') as f:
        f.writelines(file)


