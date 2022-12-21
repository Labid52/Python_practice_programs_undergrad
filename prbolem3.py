def remove_space(s):
    strr = ''
    for i in s:
        if i != ' ':
            strr = strr + i
        else:
            continue
    return strr
ff = remove_space(' I am        learning Python      bject        oriented     programming ')
print(ff)
