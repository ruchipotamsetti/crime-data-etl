from main import processData, getDataFromFile

# Test whether `processData` correctly formats data into thorn-separated (þ) strings.
def test_correct_formatting(): 
    crime_records = getDataFromFile("resources/data.json")
    processed_records = processData(crime_records, offset=0, limit=2)
    expected_output = [
        "Suspicious Incident,Domestic Simple Batteryþ2025-02-04T00:45:42.000þ2025-02-04T00:30:41.000þþ-82.32067",
        "Battery (simple)þ2025-02-03T22:29:21.000þ2025-02-01T01:30:00.000þ29.65197þ-82.32623"
    ]
    assert processed_records == expected_output # Compare function output with expected output
