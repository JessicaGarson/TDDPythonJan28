from tip import calculateTip
import unittest

class TestcalculateTip(unittest.TestCase):
    """
    Test the calculateTip function from the tip module
    """    
    def test_calc_excellent(self):
        result = calculateTip(100, "Excellent")
        self.assertEqual(result, 20)

    def test_calc_great(self):
        result = calculateTip(50, "Great")
        self.assertEqual(result, 7.5)
        
     
    def test_calc_good(self):
        result = calculateTip(50, "Good")
        self.assertEqual(result, 5)


    def test_calc_poor(self):
        result = calculateTip(100, "Poor")
        self.assertEqual(result, 5)

    def test_calc_terrible(self):
        result = calculateTip(40, "Terrible")
        self.assertEqual(result, 0)

if __name__ == "__main__":
        unittest.main()
