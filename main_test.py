import unittest
from main import sub

class TestCalc(unittest.TestCase):
    def testsub(self):
        return self.assertEqual(sub(3,2),1)
    


if __name__=='__main__':
    unittest.main()