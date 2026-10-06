

def get_response_num() -> str:
    """Выводит главное меню в консоль и возвращает значение от пользователя"""
    toggle = True
    while toggle:
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

        return response_num

def show_contact(contact_list: list) -> None:
    print(contact_list)

def show_notification(result: str, last_name='', first_name='', phone_num = '') -> None:
    """Получает код для вывода текстового значения"""
    if result == '6':
        print('Пока')

    if result == 'A':
        print('Фамилия должна состоять только из букв!'
              'Введи фамилию или 1 для выхода')

    if result == 'B':
        print('Имя должно состоять только из букв!'
              'Введи имя или 1 для выхода')

    if result == 'C':
        print(f'Контакт {last_name} {first_name} уже существует')

    if result == 'D':
        print('Номер телефона должен состоять только из цифр!'
              'Введи номер или 1 для выхода')

    if result == 'E':
        print(f'Контакт {last_name} {first_name} успешно добавлен')

    if result == 'G':
        print(f'Контакта {last_name} {first_name} не существует')

    if result == 'H':
        print(f'Контакт изменён на {first_name} {last_name} {phone_num}')

    if result == 'I':
        print('Что-то пошло не так')

def check_lastname(toggle) -> str:
    while toggle:
        lastname = input('Введи фамилию или 1 для выхода')

        if lastname == '1':
            return lastname

        if not lastname.isalpha():
             show_notification('A')
             continue

        return lastname

def check_firstname(toggle) -> str | None:
    while toggle:
        first_name = input('Введи имя или 1 для выхода')

        if first_name == '1':
            return first_name

        if not first_name.isalpha():
            show_notification('B')
            continue

        return first_name

def check_phone_num(toggle) -> str | None:
    while toggle:
        phone_num = input('Введи номер телефона или 1 для выхода')

        if phone_num == '1':
            return phone_num

        if not phone_num.isdigit():
            show_notification('D')
            continue
        return phone_num

def select_contact(contact_list: list[str]) -> int | str:
    for index, line in enumerate(contact_list):
        print(index + 1, line)

    toggle = True
    while toggle:
        check_num = input('Введи номер строки или 0 для выхода: ')
        if check_num == '0':
            return '0'

        if not check_num.isdigit():
            print('Номер строки должен состоять только из цифр!')
            continue

        real_index = int(check_num) - 1
        if real_index > len(contact_list) - 1:
            print(f'Номера строки {check_num} не существует!')
            continue

        return real_index
