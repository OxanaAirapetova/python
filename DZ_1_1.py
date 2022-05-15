duration = int(input('Введите время в секундах: '))
if 0 < duration < 60:
    sec = duration
    print(sec, 'сек')
elif 60 <= duration < 3600:
    minute = duration // 60
    sec = duration % 60
    print(minute, 'сек', sec, 'сек')
elif 3600 <= duration < 86400:
    hour = duration // 3600
    minute = (duration % 3600) // 60
    sec = (duration % 3600) % 60
    print(hour, 'час', minute, 'мин', sec, 'сек')
else:
    day = duration // 86400
    hour = (duration % 86400) // 3600
    minute = ((duration % 86400) % 3600) // 60
    sec = ((duration % 86400) % 3600) % 60
    print(day, 'дн', hour, 'час', minute, 'мин', sec, 'сек')