def func(arr):
    set_a = set(arr)
    final = 1
    for val in set_a:
        i=1
        if val-1 not in set_a: 
            while(val+i in set_a): 
                i+=1
        final = max(final, i)
    return final

arr1 = [1,9,3,4,2,20]
op1 = 4

arr2 = [8,20,7,30]
op2 = 2

arr3 = [30,40,20]
op3 = 1

arr4 = [1,9,3,2,8]
op4 = 3


import unittest
  
class Test(unittest.TestCase):
        
    def setUp(self):
        pass

    def test_a(self):
        self.assertEqual(op1, func(arr1))

    def test_b(self):
        self.assertEqual(op2, func(arr2))

    def test_c(self):
        self.assertEqual(op3, func(arr3))

    def test_d(self):
        self.assertEqual(op4, func(arr4))
  
if __name__ == '__main__':
    unittest.main()
