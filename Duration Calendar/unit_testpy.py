import unittest
import datetime
from duration_calendar import calculate_days_difference  

class TestCalculateDaysDifference(unittest.TestCase):
    
    def test_past_date(self):
        today = datetime.date.today()
        past_date = today - datetime.timedelta(days=10)
        self.assertEqual(calculate_days_difference(str(past_date)), 10)
    
    def test_future_date(self):
        today = datetime.date.today()
        future_date = today + datetime.timedelta(days=5)
        self.assertEqual(calculate_days_difference(str(future_date)), -5)
    
    def test_today(self):
        today = datetime.date.today()
        self.assertEqual(calculate_days_difference(str(today)), 0)
    
    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            calculate_days_difference("10/20/2025")  # invalid format, should raise ValueError

if __name__ == "__main__":
    unittest.main()


