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

def is_contact_in_contacts(last_name : str, first_name : str) -> bool:
    with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt', 'r') as f:
        for i in f:
            if last_name in i and first_name in i:
                return True
    return False

def check_input(last_name : str = '', first_name: str = '', phone_num: str = '') -> bool:
    if last_name:
        if last_name.isalpha():
            return True
    if first_name:
        if first_name.isalpha():
            return True
    if phone_num:
        if phone_num.isdigit():
            return True
    return False

def add_contact(last_name: str, first_name: str, phone_num: str) -> str:
    file = open_file()
    file.append(f'{last_name} {first_name} {phone_num};\n')
    with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt', 'w') as f:
        f.writelines(file)


