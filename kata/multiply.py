def multiply(n):
    power = len(str(n).removeprefix("-"))
    return n * (5 ** power)


print(multiply(-2))