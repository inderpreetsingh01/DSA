import time

def func(arr, k):
    c = len(arr)/k
    m = {}
    return_arr = []
    for val in arr:
        if val not in m:
            m[val] = 1
        else:
            m[val]+=1
            if m[val] > c:
                return_arr.append(val)

    return return_arr       


arr = [3,1,2,2,1,2,3,3]
k= 4
op = [2,3]

# arr = [3]*50000 + [2]*30001 + [1]*20000 + [0]*14000 + [5]*6000
# k= 4
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
