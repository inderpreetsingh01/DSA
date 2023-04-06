def func(arr, k):
    m = {}
    return_arr = []
    for val in arr[:k]:
        if val not in m:
            m[val] = 1
        else:
            m[val]+=1

    return_arr.append(len(m))

    for i, val in enumerate(arr[k:]):
        if val not in m:
            m[val] = 1
        else:
            m[val]+=1

        m[arr[i]]-=1
        if  m[arr[i]] == 0:
            del m[arr[i]]
        
        return_arr.append(len(m)) 

    return return_arr


arr = [10,20,20,10,30,40,10]
k = 4
op = [2,3,4,3]

import unittest
  
class Test(unittest.TestCase):
        
    def setUp(self):
        pass

    def test_a(self):
        self.assertEqual(op, func(arr, k))
  
if __name__ == '__main__':
    unittest.main()