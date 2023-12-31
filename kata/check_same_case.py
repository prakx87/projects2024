def same_case(a, b): 
    # your code here
    if not a.isalpha() or not b.isalpha():
        return -1
    elif (a.isupper() and b.isupper()) or (a.islower() and b.islower()):
        return 1
    elif (a.isupper() and b.islower()) or (a.islower() and b.isupper()):
        return 0