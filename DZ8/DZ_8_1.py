# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного
# выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
# виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ...
# raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
# выражении; имеет ли смысл в данном случае использовать функцию re.compile()?


import re
def email_parse(email_address):
    pattern = r'[\w-]+@(\w+\.+\w+)'
    RE_NAME = re.compile(pattern)
    email_dict = {}
    for item in [email_address]:
        try:
            assert RE_NAME.match(item), f'{item=}'
        except AssertionError:
            raise ValueError(f'ValueError: wrong email {email_address}:')
        else:
            adress = ''.join(email_address)
            adress = adress.partition('@')

            name_adress = adress[0]
            domain_adress = adress[2]

            email_dict.setdefault('username', name_adress)
            email_dict.setdefault('domain', domain_adress)

    return email_dict

qwe = email_parse('hallousouguwou-4678@yopmail.com')
print(qwe)
