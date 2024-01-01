# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

def find_even_index(arr, count = 0):
    if count == len(arr):
        return -1
    if sum(arr[0:count]) == sum(arr[count + 1:]):
        return count
    return find_even_index(arr, count + 1)
