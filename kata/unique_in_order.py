# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(sequence):
    output = []
    if len(sequence):
        output.append(sequence[0])
    if len(sequence) > 1:
        for character in sequence[1:]:
            if character != output[-1]:
                output.append(character)
    return output