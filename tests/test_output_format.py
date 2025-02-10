import unittest
from main import processData

class TestOutputFormat(unittest.TestCase):

    def setUp(self):
        self.sample_data = [
            {"narrative": "Assault", "report_date": "2025-01-10", "offense_date": "2025-01-09", "latitude": 29.1, "longitude": -82.1},
            {"narrative": "Theft", "report_date": "2025-01-11", "offense_date": "", "latitude": None, "longitude": -82.2}
        ]

    # Test whether `processData` correctly formats data into thorn-separated (þ) strings.
    def test_correct_formatting(self): 
        result = processData(self.sample_data, offset=0, limit=2)
        expected_output = [
            "Assaultþ2025-01-10þ2025-01-09þ29.1þ-82.1",
            "Theftþ2025-01-11þþþ-82.2"
        ]
        self.assertEqual(result, expected_output) # Compare function output with expected output

if __name__ == "__main__":
    unittest.main()
