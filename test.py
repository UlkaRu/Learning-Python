Быстрое возведение в степень

def rec(b, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return rec(b * b, n / 2)
    else:
        return b * rec(b, n - 1)


b, n = float(input()), int(input())

print(rec(b, n))
