
import argparse
import requests
import json

# url = "https://data.cityofgainesville.org/resource/gvua-xt9q.json"
def getDataFromApi(url):
    response = requests.get(url)
    if response.status_code == 200:
        crime_records = response.json() 
        return crime_records 
    else:
        print(f"Error : {response.status_code}")
        return []

def getDataFromFile(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error: Unable to read file - {e}")
        return []
    
def formatValues(value):
    if isinstance(value, list):
        return ",".join(map(str, value))
    return str(value) if value else ""
    return

def processData(crime_records, offset, limit):
    
    if offset is None:
        # print("offset: ",offset)
        offset=0
    if limit is None:
        # print("limit: ", limit)
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

    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str) 
    parser.add_argument("--offset", default=None, type=int)
    parser.add_argument("--limit", default=None, type=int)
    parser.add_argument("--file", type=str)
    args = parser.parse_args()
    
    data=[]
    offset = args.offset
    limit = args.limit
    if args.url:
        data = getDataFromApi(args.url)
    elif args.file:
        data = getDataFromFile(args.file)
    else:
        print("Error: Either --url or --file must be provided")

    result = processData(data, offset, limit)
    for line in result:
        print(line)