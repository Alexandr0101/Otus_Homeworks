class Contact:
    """Класс представляющий контакт
        Атрибуты:
        last_name (str): Фамилия контакта
        first_name (str): Имя контакта
        phone_num (str): Номер телефона"""

    def __init__(self, last_name: str, first_name: str, phone_num: str):
        self.last_name = last_name
        self.first_name = first_name
        self.phone_num = phone_num

    def __repr__(self) -> str:
        return f'{self.last_name} {self.first_name} {self.phone_num}'

    def to_file(self):
        return f"{self.last_name} {self.first_name} {self.phone_num}"


def open_file() -> list[str]:
    """Открывает файл или создаёт новый
    возвращает список строк"""
    with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt', 'a+') as f:
        f.seek(0)
        return f.readlines()

def is_contact_in_contacts(lastname: str, firstname: str) -> bool:
    """Проверяет наличие контакта в списке
    возвращает буль"""
    contacts = open_file()
    for i in contacts:
        if lastname in i.split() and firstname in i.split():
            return True
    return False

def get_contact(lastname : str, firstname: str) -> list[str]:
    """Поиск по имени и фамилии в списке, добавление найденного в новый список
    возвращает список найденного"""
    contacts_list = open_file()
    count = 0
    contacts = []
    for i in contacts_list:
        if lastname in i.split() and firstname in i.split():
            count += 1
            contacts.append(f'{count}: {i}')
    return contacts

def add_contact(contact: Contact) -> None:
    """Добавляет созданный контакт в список контактов"""
    file = open_file()
    file.append(f'{contact.to_file()}\n')
    with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt', 'w') as f:
        f.writelines(file)

def change_contact(index: int, last_name: str, first_name: str, phone_num: str ) -> str:
    """Изменяет контакт
    Возвращает строку для подтверждения операции"""
    result = open_file()
    result[index] = f'{last_name} {first_name} {phone_num}\n'
    with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt', 'w') as f:
        f.writelines(result)
    return 'OK'


def delete_contact(real_index: int):
    """Удаляет контакт возвращает  строку для подтверждения операции"""
    result = open_file()
    del result[real_index]
    with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt', 'w') as f:
        f.writelines(result)

    return 'OK'

def get_contact_string(index:int) -> str:
    """Возращает строку из списка по индексу"""
    return open_file()[index]
