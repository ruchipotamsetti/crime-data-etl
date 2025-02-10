import main

TEST_URL = "https://data.cityofgainesville.org/resource/gvua-xt9q.json"
TEST_FILE_PATH = "resources/data.json"

# Test fetching data from an API
def test_fetch_data_from_api(): 
    crime_records =  main.getDataFromApi(TEST_URL) 
    assert isinstance(crime_records, list) # Ensure data is returned as a list
    assert len(crime_records) > 0 # Ensure data list is not empty

# Test fetching data froma local JSON file
def test_fetch_data_from_file(): 
    crime_records = main.getDataFromFile(TEST_FILE_PATH)
    assert isinstance(crime_records, list) # Ensure data is returned as a list
    assert len(crime_records) > 0 # Ensure data list is not empty