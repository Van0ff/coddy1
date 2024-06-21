def sort_list(list_a, list_b):
    res = []
    i = len(list_a) - 1
    j = len(list_b) - 1

    while i >= 0 or j >= 0:
        if i >= 0 and j >= 0:
            if list_a[i] > list_b[j]:
                res.append(list_a[i])
                i -= 1
            else:
                res.append(list_b[j])
                j -= 1
        elif i >= 0:
            res.append(list_a[i])
            i -= 1
        elif j >= 0:
            res.append(list_b[j])
            j -= 1

    return res


list_a = [7, 9, 17, 19, 21]
list_b = [2, 4, 6, 8, 10]

new_list = sort_list(list_a, list_b)
print(new_list)
# Вывод: [21, 19, 17, 10, 9, 8, 7, 6, 4, 2]

