def persistence(n, count = 0):
    if len(str(n)) == 1:
        return count
    else:
        count += 1

    i = 1
    for j in str(n):
        i *= int(j)

    return persistence(i, count)
