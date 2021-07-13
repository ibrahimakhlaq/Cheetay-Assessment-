# AS ASKED THE CODE IS ONLY FOR LOWERCASE ENGLISH ALPHABETS

def chooseandswap(str):

    copy_str = str

    for j in range(len(copy_str)):
        Min = min(copy_str)
        min_index = copy_str.index(Min)

        if j == min_index:
            lst = list(copy_str)
            lst[j] = "~"
            copy_str = "".join(lst)
        if j != min_index and copy_str[j] != '~':
            swapper_index = j
            break

    if min_index != 0:
        c1 = str[min_index]
        c2 = str[swapper_index]

        lst = list(str)
        for i in range(swapper_index, len(lst)):
            if (lst[i] == c1):
                lst[i] = c2

            elif (lst[i] == c2):
                lst[i] = c1
        return "".join(lst)
    else:
        return str


str = "abaaaab"
print(chooseandswap(str))

