def func(str):
    begin = 0
    end = len(str)-1
    while(begin<end):
        if str[begin]!=str[end]:
            return False
        begin+=1
        end-=1
    return True


print(func('gfg'))
print(func('malayyalam'))
print(func('ok'))