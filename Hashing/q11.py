# there can be no more than k-1 entries occuring more than n/k times
# since (k)(n/k + 1) should be less than n which is not the case
# so we will create a map with k-1 entries and when we encounter a new element and 
# map is filled we will just subtract 1 from the frequencies of all previous elements and remove the element with 0 frequency or value
# Same as Moores voting algorithm 
import time

def func(arr, k):
    c = len(arr)/k
    m = {}
    return_arr = []
    del_key = []

    for val in arr:
        if val not in m and len(m)<k-1:
                m[val] = 1
        elif val in m:
            m[val]+=1
        else:
            for key, val in m.items():
                m[key]-=1
                if m[key]==0:
                    del_key.append(key)

            for key in del_key:
                del m[key]

    for key in m.keys():
        i=0
        for val in arr:
            if val==key:
                i+=1
            if i>c:
                return_arr.append(key)
                break
    print(len(m))
    return return_arr       


arr = [3,1,2,2,1,2,3,3]
k= 4
op = [2,3]

# arr = [3]*50000 + [2]*30001 + [1]*20000 + [0]*14000 + [5]*6000
# k = 4
# op = [2,3]


import unittest
  
class Test(unittest.TestCase):
        
    def setUp(self):
        pass

    def test_a(self):
        start_time = time.time()
        self.assertEqual(set(op), set(func(arr, k)))
        print(f"Time taken {time.time()-start_time}")
  
if __name__ == '__main__':
    unittest.main()

