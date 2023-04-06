arr1 = [2,3,4,5,6,7]
arr2 = [1,2,3,4,5]
set1 = set(arr1)
set2 = set(arr2)

print(f"a: {arr1}")
print(f"b: {arr2}")
print(f"Elements in both array a and b {set1 & set2}")
print(f"Elements in either a or b or both {set1 | set2}")
print(f"Elements in a or b but not both {set1 ^ set2}")
print(f"Elements in a but not in b {set1 - set2}")

