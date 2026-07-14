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
    elif response_num == 2:
        while True:
            last_name = input('Введи фамилию: \n'
                              'Для выхода введи 1 \n')
            if last_name == '1':
                break
            check_last_name =  check_input(last_name = last_name)
            if check_last_name:
                first_name = input('Введи имя: \n'
                                   'Для выхода введи 1 \n')
                if first_name == '1':
                    break
                check_firstname = check_input(first_name = first_name)
                if check_firstname:
                    contact_data = is_contact_in_contacts(last_name, first_name)
                    if not contact_data:
                        phone_num = input('Введи номер телефона: ')
                        check_phone_num = check_input(phone_num = phone_num)
                        if check_phone_num:
                            contact_data = add_contact(last_name, first_name, phone_num)
                            print(f'Контакт {last_name} {first_name} успешно добавлен')
                            break
                        else:
                            print('Вводите только цифры: ')
                    else:
                        print(f'Контакт {last_name} {first_name} уже существует')
                else:
                    print('Вводите только буквы: ')
            else:
                print('Вводите только буквы: ')
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