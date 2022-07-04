# *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6
# урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs
# ) для получения информации вида: (<remote_addr>, <request_datetime>,
# <request_type>, <requested_resource>, <response_code>, <response_size>),
# например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET
# /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET',
# '/downloads/product_2', '304', '0')
# © geekbrains.ru 15

import re


pattern = r'[\d,(\.)]+[\s-]+[\S,\d]+' \
          r'[\s-]+[\s+]+[\d]+[\S]+[\s-]+' \
          r'[\S"]+[\s-]+[\/]+[\w]+[\/]+[\w]+' \
          r'[\s]+[\w]+[\/]+[\d,\.,\"]+' \
          r'[\s]+[\d]+[\s]+[\d]+'

RE_NAME = re.compile(pattern)
adress = '80.91.33.133 - - [17/May/2015:08:05:48 +0000] ' \
         '"GET /downloads/product_1 HTTP/1.1" 404 324 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"'
adress_reg = RE_NAME.findall(adress)

list_adress = (''.join(adress_reg)).split()
list_adress_clean = [re.sub('[|["]|]', '', i) for i in list_adress]

del list_adress_clean[1:3]
del list_adress_clean[5]
list_adress_clean[1] = f'{list_adress_clean[1]} {list_adress_clean[2]}'
del list_adress_clean[2]

list_adress_clean_t = tuple(list_adress_clean)
print(f'Результат парсинга: {list_adress_clean_t}')

