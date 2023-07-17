import pandas as pd
import unittest
import calc

class TestCalc(unittest.testCase):
    def test_add(self):
        result =calc.add(10,5)
        self.assertEqual(result,15)



liste=[3,6,7,7,8]
s=map(lambda x: x*2,liste)
print(list(s))

