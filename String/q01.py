# longest common span with same sum in two binary arrays

def func(str):
    arr = [0]*26
    for ch in str:
        arr[ord(ch)-ord('a')]+=1

    for i, val in enumerate(arr):
        if val!=0:
            print(f"{chr(i+ord('a'))} {val}")


# Test Cases
str1 = 'geeksforgeeks'
func(str1)