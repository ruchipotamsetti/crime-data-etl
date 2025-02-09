import main

TEST_URL = "https://data.cityofgainesville.org/resource/gvua-xt9q.json"
TEST_FILE = "data.json"

def test_fetch_data_from_api():
    data =  main.getDataFromApi(TEST_URL)
    assert isinstance(data, list)
    assert len(data) > 0

def test_fetch_data_from_file():
    data = main.getDataFromFile(TEST_FILE)
    assert isinstance(data, list)
    assert len(data) > 0