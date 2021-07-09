# AS ASKED THE CODE IS ONLY FOR LOWERCASE ENGLISH ALPHABETS

def chooseandswap(str):

    copy_str = str

    for j in range(len(copy_str)):
        Min = min(copy_str)
        min_index = copy_str.index(Min)

        if j == min_index:
            copy_str = copy_str.replace(copy_str[j], "~")

        if j != min_index and copy_str[j] != '~':
            swapper_index = j
            break

    if min_index != 0:
        c1 = str[min_index]
        c2 = str[swapper_index]

        lst = list(str)
        for i in range(len(lst)):
            if (lst[i] == c1):
                lst[i] = c2

            elif (lst[i] == c2):
                lst[i] = c1
        return "".join(lst)
    else:
        return str


str = "aaaabbbbbecccdd"
chooseandswap(str)
