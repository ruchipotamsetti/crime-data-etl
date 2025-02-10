# Import the necessary libraries
import argparse
import requests
import json



# This function takes url as the input argument, fetches data from the API and return the file in the JSON format

def getDataFromApi(url):
    response = requests.get(url)
    if response.status_code == 200:
        crime_records = response.json() 
        return crime_records 
    # if the functions fails to fetch the data, then print the error code
    else:
        print(f"Error : {response.status_code}")
        return []

# This function returns a list of crime records by parsing the JSON file that is fetched.
def getDataFromFile(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error: Unable to read file - {e}")
        return []

# This function returns elements joined by commas if the value is a list. If the passed value is None, it returns an empty string.
def formatValues(value):
    if isinstance(value, list):
        return ",".join(map(str, value))
    return str(value) if value else ""

# This function returns a string with only the required fields seperated by thorn character, filtering the data using the parameters passed
def processData(crime_records, offset, limit):
    if offset is None:
        offset=0
    if limit is None:
        limit = len(crime_records)
    else:
        limit = limit + offset
    thorn = "\u00FE"
    output_lines = []
    for i in range(offset, limit):
        incident_type = formatValues(crime_records[i].get('narrative'))
        report_date = formatValues(crime_records[i].get('report_date'))
        offense_date = formatValues(crime_records[i].get('offense_date'))
        latitude = formatValues(crime_records[i].get('latitude'))
        longitude = formatValues(crime_records[i].get("longitude"))
        formatted_line = thorn.join([incident_type, report_date, offense_date, latitude, longitude])
        output_lines.append(formatted_line)
    return output_lines

if __name__ == "__main__":

    parser = argparse.ArgumentParser() # creating ArgumentParser object to handle command-line arguments
    parser.add_argument("--url", type=str, help="The source location on the web.") 
    parser.add_argument("--offset", default=None, type=int, help="The offset to jump forward.")
    parser.add_argument("--limit", default=None, type=int, help="The number of records you want to retrive.")
    parser.add_argument("--file", type=str, help="The source location locally.")
    args = parser.parse_args() # parsing the arguments and storing them in args
    
    records=[]
    offset = args.offset
    limit = args.limit
    if args.url:
        records = getDataFromApi(args.url) 
    elif args.file:
        records = getDataFromFile(args.file)
    else:
        print("Error: Either --url or --file must be provided")

    formatted_crime_records = processData(records, offset, limit)
    for record in formatted_crime_records:
        print(record)