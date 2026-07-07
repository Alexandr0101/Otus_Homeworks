from functions import open_file, open_and_save

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
        pass
    elif response_num == 2:
        pass
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