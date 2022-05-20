ls = []
for i in range(1, 1000):
    if i % 2 != 0:
        result = i ** 3
        ls.append(result)
print(ls)

ls2 = []
for j in ls:
    a = (j % 10)
    b = (j // 10) % 10
    c = ((j // 10) // 10) % 10
    d = ((j // 10) // 10) // 10
    summa = a + b + c + d
    if summa % 7 == 0:
        ls2.append(j)
print(sum(ls2))

ls3 = []
for x in ls:
    x += 17
    a1 = (x % 10)
    b1 = (x // 10) % 10
    c1 = ((x // 10) // 10) % 10
    d1 = ((x // 10) // 10) // 10
    summa2 = a1 + b1 + c1 + d1
    if summa2 % 7 == 0:
        ls3.append(x)
print(sum(ls3))

# решение со звёздочкой
ls4 = []
for item in range(1, 1000):
    if item % 2 != 0:
        result = item ** 3
        a3 = (result % 10)
        b3 = (result // 10) % 10
        c3 = ((result // 10) // 10) % 10
        d3 = ((result // 10) // 10) // 10
        summa3 = a3 + b3 + c3 + d3
        if summa3 % 7 == 0:
            ls4.append(result)
print(sum(ls4))
