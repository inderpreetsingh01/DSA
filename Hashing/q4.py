# subarray should be continous
# Time O(n), Auxillary Space O(n)

def given_sum_subarray(arr, _sum):
    '''
    zero_sum_subarray
    '''
    sum_set = set([0])
    sum1=0

    for val in arr:
        sum1+=val
        if sum1-_sum in sum_set:
            return True
              
        sum_set.add(sum1)

    return False


arr1 = [5, 8, 6, 13, 3, -1]
sum1 = 22
arr2 = [15, 2, 8, 10, -5, -8, 6]
sum2 = 3
arr3 = [3, 2, 5, 6]
sum3 = 10

print(given_sum_subarray(arr1, sum1))
print(given_sum_subarray(arr2, sum2))
print(given_sum_subarray(arr3, sum3))