# **cis6930sp25 -- Assignment1**

**Name:** Ruchita Potamsetti

---

## **Assignment Description**
This script fetches and processes crime records from the given API or a local file. It takes command line parameters like offset and limit to filter the number of records needed. Then from the filtered records relevant fields are extracted and are seperated by a thorn (`þ`) character before printing to STDOUT. Fields that have multiple entries are seperated by commas and the fields with null or empty entries are left blank.

---

## **How to Install**
To install the necessary dependencies using `pipenv`, run:
```sh
pipenv install -e .
```
This will create a virtual environment and install all required packages.

---

## **How to Run**
Execute the program using:
```sh
pipenv run python main.py --url https://data.cityofgainesville.org/resource/gvua-xt9q.json --offset 0 --limit 5
```
Alternatively, you can run it with a local JSON file:
```sh
pipenv run python main.py --file data.json --offset 2 --limit 3
```

---

## **Example Output**
```sh
Theftþ2025-01-10T14:23:15.000þ2025-01-10T13:00:00.000þ29.66658þ-82.32067
Theft,Burglaryþ2025-02-02T20:49:44.000þ2025-02-02T20:30:43.000þ29.64089þ-82.30588
Assaultþ2025-01-12T16:00:42.000þþ29.67214þ-82.31548
```

### **Example Video**
![video](video)

---

## **Features and Functions**

### **`main.py`**
- **`getDataFromApi(url)`** - Fetches JSON data from the provided API URL.
- **`getDataFromFile(filepath)`** - Reads incident data from a local JSON file.
- **`processData(crime_records, offset, limit)`** - Loops through the received crime records applying offset and/or limit filtering, extracts relevant fields, and formats the output using a thorn separator.

---

## **Bugs and Assumptions**
- If both the API url and file are provided in the command line as arguments then it would fetch data from the API.
- Assumes that API responses always return valid JSON.
- Requires an active internet connection when fetching data from a URL.
- Limited error handling for malformed JSON files.

---

