def func(str, pat):
    i=0
    out = []
    while(i<len(str)-len(pat)+1):
        j=0
        while(((j)<len(pat)) and (pat[j]==str[j+i])):
            j+=1
        if j==0:
            i+=1
        elif j==len(pat):
            out.append(i)
            i+=j
        else:
            i+=j

    return out

print(func('ABCEABEFABCD', 'ABCD'))
print(func('AZERTQER', 'ER'))
print(func('ABCAAAD', 'ABD'))