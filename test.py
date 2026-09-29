import unittest
from fractions import Fraction
from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
        
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()
    
    ## The test results show that the failed test expects the sum of the fractions to equal 1
    ## but the actual result was 9/10.
    ## The test that worked was "test_list_int" which expected the program to correclt add a list of integers
    ## It passed becuase 1+2+3 = 6 so the import sum() function served its purpose.