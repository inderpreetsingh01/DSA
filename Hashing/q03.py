# subarray should be continous

def zero_sum_subarray(arr):
    '''
    zero_sum_subarray
    '''
    sum_set = set([0])
    sum1=0

    for val in arr:
        sum1+=val
        if sum1 in sum_set:
            return True
              
        sum_set.add(sum1)

    return False


arr1 = [1, 4, 13, -3, -10, 5]
arr2 = [-1, 4, -3, 5, 1]
arr3 = [3, 1, -3, 5, 6]
arr4 = [5, 6, 0, 8]

print(zero_sum_subarray(arr1))
print(zero_sum_subarray(arr2))
print(zero_sum_subarray(arr3))
print(zero_sum_subarray(arr4))