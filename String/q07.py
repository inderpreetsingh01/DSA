# creates a new string to return 
# def func(str):
#     str_out = ''
#     end = len(str)
#     for i in range(1, len(str)+2):
#         ch = str[len(str)-i]
#         if ch==' ' or i==len(str)+1:
#             for j in range(len(str)-i+1, end):
#                 str_out+=str[j]
#             str_out+=' '
#             end = len(str)-i

#     return str_out

def swap(str, i, j):
    temp = str[j]
    str[j] = str[i]
    str[i] = temp

def reverse(str, start, end):
    while(start<end):
        swap(str, start, end)
        start+=1
        end-=1

# modify the same string
def func(str):
    str_list = list(str)
    start = 0
    for i in range(0, len(str_list)+1):
        if i==len(str_list) or str_list[i]==' ':
            reverse(str_list, start, i-1)
            start = i+1

    reverse(str_list, 0, len(str_list)-1)

    return ('').join(str_list)

print(func('welcome to course'))
print(func('how are you doing'))
print(func('geeks for geeks'))