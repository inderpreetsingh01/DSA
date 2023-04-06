def count(arr):
    '''
    arr (lst): list
    
    '''
    # M1
    unique_vals = set()
    for val in arr:
        unique_vals.add(val)

    #M2
    unique_vals = set(arr)

    return len(unique_vals)

print(count([1,2,3,4,5,5,4,3,2,1]))