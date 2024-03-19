# lst = [1, 3, 4, 7, 8]
lst = [1, 3, 1, 5]


def is_increasing(lst):
    for i in range(lst[0], lst[3]):
        if (lst[i] > lst[i - 1]):
            return True
        else:
            return False


# is_increasing(lst)
print(is_increasing(lst))
