# subarray should be continous
# Time O(n), Auxillary Space O(n)

def given_sum_longest_subarray(arr, _sum):
    '''
    zero_sum_subarray
    '''
    m = {}
    pre_sum=0
    res = 0

    for i, val in enumerate(arr):
        pre_sum+=val
        if pre_sum == _sum:
            res = i+1
            
        if pre_sum-_sum in m:
            res = max(res, i+1 - m[pre_sum-_sum])
              
        # pre_sum is not our desired sum so we dont want to increase length of its subgroup 
        # otherwise length for subgroup for _sum will decrease
        if pre_sum not in m:
            m[pre_sum] = i+1

    return res

arr1 = [5, 8, -4, -4, 9, -2, 2]
sum1 = 0
arr2 = [3, 1, 0, 1, 8, 2, 3, 6]
sum2 = 5
arr3 = [8, 3, 7]
sum3 = 15
arr4 = [8, 3, 1, 5, -6, 6, 2, 2]
sum4 = 4

print(given_sum_longest_subarray(arr1, sum1))
print(given_sum_longest_subarray(arr2, sum2))
print(given_sum_longest_subarray(arr3, sum3))
print(given_sum_longest_subarray(arr4, sum4))