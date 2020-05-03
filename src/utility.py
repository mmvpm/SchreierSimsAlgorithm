# *-* coding: utf-8 *-*



# Удобный переход из 0-индексации
def plus(a, add = 1):
    return type(a)(list(map(lambda x: x + add, a)))


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)