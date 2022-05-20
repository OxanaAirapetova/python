for i in range(1, 101):
    if i == 1:
        print(i, 'процент')
    elif 1 < i <= 4:
        print(i, 'процента')
    elif 4 < i <= 20:
        print(i, 'процентов')
    elif 20 < i and i % 10 == 1:
        print(i, 'процент')
    elif 2 <= i % 10 <= 4:
        print(i, 'процента')
    else:
        print(i, 'процентов')




