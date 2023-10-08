from jinja2 import Template

import requests
import json
import xmltodict

url = "https://ergast.com/api/f1/current"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

data_dict = xmltodict.parse(response.text)
json_data = json.dumps(data_dict, indent=4)

if __name__ == "__main__":
    with open("data.json","w") as f:
        f.write(json_data)
    