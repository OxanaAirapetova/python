# * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?


import requests
import xmltodict
import datetime as DTM


def currency_rates_adv(current):
    global money
    site = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if current.upper() not in site:
        return print(f'Значение валюты отсутствует в словаре. Результат: {None}')

    site = xmltodict.parse(site)
    money_code = current.upper()
    for i in site['ValCurs']['Valute']:
        if i['CharCode'] == money_code:
            money = i['Value']
            print(f'Курс {money_code} на сегодня: {money} руб')

    time_money = site['ValCurs']['@Date']
    time_money = DTM.datetime.strptime(time_money, '%d.%m.%Y').date()
    print(f'Курс {money_code} на {time_money}: {money} руб')
    print(type(time_money))


if __name__ == '__main__':
    currency_rates_adv('gbp')
    print('Функция работает из файла DZ_4_3')
elif __name__ != '__main__':
    print('Функция работает из файла utils')

