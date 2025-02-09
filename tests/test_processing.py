import unittest
from main import processData

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        """Sample data setup"""
        self.sample_data = [
            {"narrative": ["Theft", "Burglary"], "report_date": "2025-01-20", "offense_date": "", "latitude": 29.67, "longitude": -82.33},
            {"narrative": "Robbery", "report_date": "2025-01-21", "offense_date": "2025-01-21", "latitude": None, "longitude": -82.22},
            {"narrative": "Fraud", "report_date": "2025-01-22", "offense_date": "2025-01-22", "latitude": 29.55, "longitude": -82.11}
        ]

    def test_extract_with_offset_and_limit(self):
        """Test extracting an arbitrary offset and limit"""
        result = processData(self.sample_data, offset=1, limit=2)
        print("RESULTTTTT: ", result)
        expected = [
            "Robberyþ2025-01-21þ2025-01-21þþ-82.22",
            "Fraudþ2025-01-22þ2025-01-22þ29.55þ-82.11"
        ]
        self.assertEqual(result, expected)

    def test_extract_incident_type(self):
        """Test extracting incident type (single & multiple values)"""
        result = processData(self.sample_data, offset=0, limit=1)
        self.assertEqual(result, ["Theft,Burglaryþ2025-01-20þþ29.67þ-82.33"])

    def test_extract_dates(self):
        """Test extracting report and offense dates"""
        result = processData(self.sample_data, offset=1, limit=1)
        self.assertEqual(result, ["Robberyþ2025-01-21þ2025-01-21þþ-82.22"])

    def test_extract_latitude_longitude(self):
        """Test extracting latitude and longitude"""
        result = processData(self.sample_data, offset=2, limit=1)
        self.assertEqual(result, ["Fraudþ2025-01-22þ2025-01-22þ29.55þ-82.11"])

if __name__ == "__main__":
    unittest.main()
