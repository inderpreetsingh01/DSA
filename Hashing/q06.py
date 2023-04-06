# longest_subarray_with_equal_zero_and_one

def func(arr): 
    '''
    ok
    '''
    pre_sum = 0
    m = {}
    res = 0
    for i, val in enumerate(arr):
        if val==1:
            pre_sum+=1
        elif val==0:
            pre_sum-=1

        if pre_sum == 0:
            res = i+1

        if pre_sum in m:
            res = max(res, i+1-m[pre_sum])

        if pre_sum not in m:
            m[pre_sum] = i+1

    return res
    
arr1 = [1,0,1,1,1,0,0]
arr2 = [1,1,1,1]
arr3 = [0,0,1,1,1,1,1,0]
arr4 = [0,0,1,0,1,1]

print(func(arr1))
print(func(arr2))
print(func(arr3))
print(func(arr4))
# func(arr2)
# func(arr3)
# func(arr4)