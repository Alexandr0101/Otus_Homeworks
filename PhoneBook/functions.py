def open_file():
    with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt', 'a+') as f:
        f.seek(0)
        return f.readlines()

def open_and_save():
   contact_data = open_file()
   with open('/Users/alex/OTUS/Homeworks/PhoneBook/Contacts.txt', 'w') as f:
       f.writelines(contact_data)
       return 'Success'
