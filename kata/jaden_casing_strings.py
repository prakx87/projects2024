# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python

def to_jaden_case(string):
    updated_string_list = []
    for word in string.split(" "):
        updated_string_list.append(word.capitalize())
    return " ".join(updated_string_list)