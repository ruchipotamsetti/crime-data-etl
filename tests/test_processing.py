from main import processData, getDataFromFile

# Test extracting an arbitrary offset and limit
def test_filtering_with_offset_and_limit():
    crime_records = getDataFromFile("resources/data.json")
    result = processData(crime_records, offset=1, limit=2)
    expected = [
        "Battery (simple)þ2025-02-03T22:29:21.000þ2025-02-01T01:30:00.000þ29.65197þ-82.32623",
        "þ2025-02-03T21:22:07.000þ2025-02-03T20:42:00.000þ29.67923þ-82.27794"
    ]
    assert result == expected

# Test extracting incident type (single & multiple values)
def test_extracting_incident_type():
    crime_records = getDataFromFile("resources/data.json")
    result = processData(crime_records, offset=0, limit=1)
    expected = ["Suspicious Incident,Domestic Simple Batteryþ2025-02-04T00:45:42.000þ2025-02-04T00:30:41.000þþ-82.32067"]
    assert result == expected

# Test extracting report and offense dates
def test_extracting_dates():
    crime_records = getDataFromFile("resources/data.json")
    result = processData(crime_records, offset=1, limit=1)
    expected = ["Battery (simple)þ2025-02-03T22:29:21.000þ2025-02-01T01:30:00.000þ29.65197þ-82.32623"]
    assert result == expected

# Test extracting latitude and longitude
def test_extracting_latitude_longitude():
    crime_records = getDataFromFile("resources/data.json")
    result = processData(crime_records, offset=4, limit=1)
    expected = ["Domestic Simple Batteryþ2025-02-03T19:26:00.000þ2025-02-03T19:20:00.000þ29.64258þ"]
    assert result == expected