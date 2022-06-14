import sys

argv = sys.argv[1:]
index = argv
sales = []
if len(index) == 2:
    int_index_one = int(index[0])
    int_index_two = int(index[1])
    with open('bakery.csv', encoding='utf-8') as f:
         for i in f.readlines():
             sales.append(i.strip())
    print('\n'.join(sales[int_index_one:int_index_two + 1]))
elif len(index) == 1:
    int_index_one = int(index[0])
    with open('bakery.csv', encoding='utf-8') as f:
        for i in f.readlines():
            sales.append(i.strip())
    print('\n'.join(sales[int_index_one:]))
else:
    with open('bakery.csv', encoding='utf-8') as f:
        for i in f.readlines():
            sales.append(i.strip())
    print('\n'.join(sales))