# * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов
# из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

from collections import Counter

view = open('../nginx_logs.txt')

new_view = []


for i in view:
    web_list = i.split()
    del web_list[1:]
    web_list = ''.join(web_list)
    new_view.append(web_list)

max_spam = Counter(new_view)
max_values = max(max_spam.values())
most_popular_ip = (k for k, v in max_spam.items() if v == max_values)
most_popular_ip = ''.join(list(most_popular_ip))

print(f'Самый часто встречающийся IP-адрес: {most_popular_ip}'
      f'\nОн встречается {max_values} раз')
view.close()