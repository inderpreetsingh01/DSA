# longest common span with same sum in two binary arrays

def func(arr1, arr2):
    pre_sum = 0
    m = {}

    res = 0

    for i, vals in enumerate(zip(arr1, arr2)):
        num = vals[0]-vals[1]

        pre_sum += num

        if pre_sum == 0:
            res = i+1

        if pre_sum in m:
            res = max(res, i+1-m[pre_sum])

        if pre_sum not in m:
            m[pre_sum] = i+1

    return res

# Test Cases
arr11 = [0, 1, 0, 0, 0, 0]
arr12 = [1, 0, 1, 0, 0, 1]
op1 = 4

arr21 = [0, 1, 0, 1, 1, 1, 1]
arr22 = [1,1,1,1,1,0,1]
op2 = 6

arr31 = [0,0,0]
arr32 = [1,1,1]
op3 = 0

arr41 = [0,0,1,0]
arr42 = [1,1,1,1]
op4 = 1

import unittest
  
class Test(unittest.TestCase):
      
    def setUp(self):
        pass

    def test_a(self):
        self.assertEqual(op1, func(arr11, arr12))

    def test_b(self):
        self.assertEqual(op2, func(arr21, arr22))

    def test_c(self):
        self.assertEqual(op3, func(arr31, arr32))

    def test_d(self):
        self.assertEqual(op4, func(arr41, arr42))
  
if __name__ == '__main__':
    unittest.main()