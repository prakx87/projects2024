import random

def generate(length):
    binary_num = []
    for i in range(length):
        binary_num.append(random.randint(0, 1))
    return binary_num


print(generate(50))