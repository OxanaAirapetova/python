# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

def generic_nums(num):
    for elem in range(1, num + 1, 2):
        yield elem
                     #в этот оператор мы записываем "прыгунок по циклу" и то, что делаем с элементом последовательности,
                        # когда прыгунок на него попадает


odd_to_100 = generic_nums(100)
print(next(odd_to_100))
print(next(odd_to_100))
print(next(odd_to_100))
print(next(odd_to_100))
print(next(odd_to_100))
print(next(odd_to_100))
print(next(odd_to_100))
print(next(odd_to_100))
print(next(odd_to_100))
print(next(odd_to_100))
print(next(odd_to_100))
print(next(odd_to_100))

