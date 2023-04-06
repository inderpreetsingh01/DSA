# iterative solution
def func(str1, str2):
    begin = 0
    end = len(str2)
    for ch1 in str1:
        if str2[begin]==ch1:
            begin+=1
    
    return begin==end


# recursive solution
def func(str1, str2):
    if len(str2)==0:
        return True
    
    elif len(str1)==0:
        return False
    
    if str1[0]==str2[0]:
        return func(str1[1:], str2[1:])
    
    else:
        return func(str1[1:], str2)


print(func('ABCD', 'AD'))
print(func('ABCDE', 'AED'))
print(func('ABCDEFG', 'ADG'))
