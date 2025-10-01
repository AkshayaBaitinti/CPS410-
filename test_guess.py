import unittest
from main import check_guess

    
class TestGuessingGame(unittest.TestCase):
    def test_guess_too_low(self):
        result = check_guess(25, 60)
        self.assertEqual(result, "Too low!")

    def test_guess_too_high(self):
        result = check_guess(85, 40)
        self.assertEqual(result, "Too high!")

    def test_guess_correct(self):
        result = check_guess(50, 50)
        self.assertEqual(result, "Correct!")

if __name__ == "__main__":

    unittest.main()
