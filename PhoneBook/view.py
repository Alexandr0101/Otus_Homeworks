


def get_response_num() -> str:
    """Выводит главное меню в консоль и возвращает значение от пользователя"""

    response_num = input("""Привет:) Добро пожаловать в телефонный справочник!
    Показать все контакты -> введи 1: 
    Создать контакт -> введи 2: 
    Найти контакт -> введи 3:  
    Изменить контакт -> введи 4:  
    Удалить контакт -> введи 5: 
    Для выхода -> введи 6: 
    """)
    return response_num


def show_notification(result: str) -> str:
    """Получает код для вывода текстового значения"""
    if result == '6':
        print('Пока')

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
        phone_num = input('Введи номер телефона или 1 для выхода')

        if phone_num == '1':
            return None

        if not phone_num.isdigit():
            print('Номер телефона должен состоять только из цифр!'
                  'Введи номер или 1 для выхода')
            continue
        return phone_num