def func(str1, str2):
    m = {}
    for ch in str1:
        if ch not in m:
            m[ch] = 1
        else:
            m[ch]+=1

    for ch in str2:
        if ch in m:
            m[ch]-=1
            if m[ch]==0:
                del m[ch]

    return not len(m)

print(func('listen', 'silent'))
print(func('aaacb', 'cabaa'))
print(func('aab', 'bab'))