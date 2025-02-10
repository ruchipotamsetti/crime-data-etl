import main

TEST_URL = "https://data.cityofgainesville.org/resource/gvua-xt9q.json"
TEST_FILE = "data.json"

# Test fetching data from an API
def test_fetch_data_from_api(): 
    data =  main.getDataFromApi(TEST_URL) 
    assert isinstance(data, list) # Ensure data is returned as a list
    assert len(data) > 0 # Ensure data list is not empty

# Test fetching data froma local JSON file
def test_fetch_data_from_file(): 
    data = main.getDataFromFile(TEST_FILE)
    assert isinstance(data, list) # Ensure data is returned as a list
    assert len(data) > 0 # Ensure data list is not empty