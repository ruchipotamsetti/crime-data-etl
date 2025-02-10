# **cis6930sp25 -- Assignment1**

**Name:** Ruchita Potamsetti

---

## **Assignment Description**
This script fetches and processes crime records from the given API or a local file. It takes command line parameters like offset and limit to filter the number of records needed. Then from the filtered records relevant fields are extracted and are seperated by a thorn (`þ`) character before printing to STDOUT. Fields that have multiple entries are seperated by commas and the fields with null or empty entries are left blank.

---

## **Project Structure** 

```plaintext
cis6930sp25-assignment1/
├── COLLABORATORS.md      # A markdown file describing collaborations and inspirations taken from other websites.
├── Pipfile               # Defines the dependencies and virtual environment for the project (used with pipenv).
├── README.md             # Project description and instructions.
├── main.py               # Main Python script that contains the core functionality of the project.
├── pyproject.toml        # Configuration file for the project, used by pipenv.
├── Assignment1_demo.gif  # Demo video
└── .github/workflows          
    ├── pytest.yaml  # Configuration file for running tests using GitHub Actions (CI).
└── tests/                # Directory containing all test files.
    ├── test_downloading_data.py  # Tests related to downloading data from API and files.
    ├── test_output_format.py    # Tests to verify extraction of relevant fields and filtering.
    └── test_processing.py       # Tests to verify the thorn-separated output format.
└── resources/                # Directory containing all test files.
    └── data.json  # Mock json data file to run tests.
```

---

## **To Install**
To install the necessary dependencies using `pipenv`, run:
```sh
pipenv install -e .
```
This will create a virtual environment and install all required packages.

---

## **To Run**
Execute the program using:
```sh
pipenv run python main.py --url https://data.cityofgainesville.org/resource/gvua-xt9q.json --offset 0 --limit 5
```
Alternatively, you can run it with a local JSON file:
```sh
pipenv run python main.py --file resources/data.json --offset 2 --limit 3
```

---

## **Example Output**
```sh
Theftþ2025-01-10T14:23:15.000þ2025-01-10T13:00:00.000þ29.66658þ-82.32067
Theft,Burglaryþ2025-02-02T20:49:44.000þ2025-02-02T20:30:43.000þ29.64089þ-82.30588
Assaultþ2025-01-12T16:00:42.000þþ29.67214þ-82.31548
```

---

## **To Test**
After installing, use the command below to execute the pytests:
```sh
pipenv run python -m pytest -v
```

---

### **Demo**
![](https://github.com/ruchipotamsetti/cis6930sp25-assignment1/blob/master/Assignment1_demo.gif)
---

## **Features and Functions**

### **`main.py`**
- **`getDataFromApi(url)`** :
  - Fetches JSON data from the given API URL.
  - Parameters:
    - url (str): The API endpoint to fetch data from.
  - Returns: A list of JSON objects (crime records) if successful, otherwise an empty list.
- **`getDataFromFile(filepath)`** :
  - Reads incident data from a local JSON file.
  - Parameters:
     - filepath (str): The path to the JSON file.
  - Returns: A list of JSON objects (crime records) if successful, otherwise an empty list.
- **`formatValues(value)`** :
  - Formats the field values as required. If a field has multiple entries it is seperated by commas. If a field has null or empty entries it is considered as blank.
  - Parameters:
     - value: The value to format (can be a string, list, or None).
  - Returns: str: A formatted string. If the value is a list, it joins elements with commas. If the value is None, it returns an empty string.
- **`processData(crime_records, offset, limit)`** 
  - Loops through the received crime records applying offset and/or limit filtering, extracts relevant fields, and formats the output using a thorn separator.
  - Parameters: crime_records (list):
     - The list of crime records (JSON objects).
     - offset (int): The number of records to skip before processing.
     - limit (int): The number of records to return.
  - Returns: list: A list of formatted strings, where fields are separated by the thorn (þ) character.

---

## **Bugs and Assumptions**
- If both the API url and file are provided in the command line as arguments then it would fetch data from the API.
- Assumes that API responses always return valid JSON.
- Requires an active internet connection when fetching data from a URL.
- Limited error handling for malformed JSON files.

---

