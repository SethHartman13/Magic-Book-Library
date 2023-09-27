import os
import jsonschema as js
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

json_list = os.listdir(f"{os.getcwd()}/jsons/")

for json_file in json_list:
    with open(f"{os.getcwd()}/jsons/{json_file}") as f:
        data_json = json.load(f)

    with open("schema.json") as f:
        data_schema = json.load(f)
    try:
        js.validate(data_json, data_schema)
        print(f"No Errors found: {json_file}")

    except:
        print(f"Error: {json_file}")

print("Check completed")