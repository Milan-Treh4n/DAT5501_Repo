import unittest
from duration_calendar import user_input_date

class TestUserInputDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(user_input_date("2023-10-15"), "2023-10-15")

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            user_input_date("15-10-2023")

    def test_non_date_string(self):
        with self.assertRaises(ValueError):
            user_input_date("not-a-date")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            user_input_date("")

