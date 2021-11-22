import math
import random


def U(a, b):
    return a + (b - a) * random.random()


def Ud(a, b):
    separator = 0
    distance = 1/(b-a + 1)
    x = U(0, 1)
    for i in range(b-a + 1):
        separator += distance
        if x <= separator:
            return a+i


def E(lda):
    x = U(0, 1)
    return -(1 / lda) * math.log(x, math.e)


def Ed(lda):
    return int(E(lda))


def test():
    amount_to_generate = 5000
    list_size = 10
    values = [0 for _ in range(list_size)]
    counted = 0

    for _ in range(amount_to_generate):
        x = E(0.2)

        separator = 0
        for i in range(list_size):
            separator += 1
            if x <= separator:
                values[i] += 1
                counted += 1
                break

    return values, amount_to_generate - counted


# for i in range(100):
#     print(Ed(0.4))
# print(test())

