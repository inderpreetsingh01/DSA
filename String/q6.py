def func(str):
    m = {}
    for ch in str:
        if ch not in m:
            m[ch]=1
        else:
            m[ch]+=1

    for i, ch in enumerate(str):
        if m[ch]==1:
            return i
    return -1


print(func("geeksforgeeks"))
print(func("abcabc"))
print(func("apple")) 