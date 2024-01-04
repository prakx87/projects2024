# https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python

def add_binary(a,b):
    sum = a + b
    bin_val = ""
    while True:
        div = sum // 2
        rem = sum % 2

        sum = div
        bin_val = str(rem) + bin_val

        if div == 0:
            break

    return bin_val.removeprefix("0")

print(add_binary(1,1))