from functions import open_file, open_and_save, check_input, is_contact_in_contacts, add_contact

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
        from functions import add_contact, check_input, is_contact_in_contacts

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
            elif response_num == 2:
                while True:
                    last_name = input('Введи фамилию или 1 для выхода: ')
                    if last_name == '1':
                        break
                    check_last_name = check_input(last_name=last_name)
                    if not check_last_name:
                        print('Фамилия должна состоять только из букв')
                        while True:
                            last_name = input('Введи фамилию или 1 для выхода: ')
                            if last_name == '1':
                                break
                            if not check_input(last_name=last_name):
                                continue
                            if check_input(last_name=last_name):
                                break
                    first_name = input('Введи имя или 1 для выхода: ')
                    if first_name == '1':
                        break
                    check_first_name = check_input(first_name=first_name)
                    if not first_name:
                        print('Фамилия должна состоять только из букв.')
                        while True:
                            first_name = input('Введи имя или 1 для выхода: ')
                            if first_name == '1':
                                break
                            if not check_input(first_name=first_name):
                                continue
                            if check_input(first_name=first_name):
                                break
                    check_contact = is_contact_in_contacts(last_name, first_name)
                    if check_contact:
                        print(f'Контакт {last_name} {first_name} уже существует')
                    phone_num = input('Введи номер телефона или 1 для выхода: ')
                    if phone_num == '1':
                        break
                    if not phone_num:
                        print('Номер телефона должен состоять только из цифр')
                        while True:
                            phone_num = input('Введи номер телефона или 1 для выхода: ')
                            if phone_num == '1':
                                break
                            if not check_input(phone_num=phone_num):
                                continue
                            if check_input(phone_num=phone_num):
                                break
                    result = add_contact(last_name, first_name, phone_num)
                    print(f'Контакт {last_name} {first_name} успешно добавлен')
    elif response_num == 3:
        pass
    elif response_num == 4:
        pass
    elif response_num == 5:
        pass
    elif response_num == 6:
        open_file()
    elif response_num == 7:
        result = open_and_save()
        if result == 'Success':
            print('Файл успешно сохранён\n')