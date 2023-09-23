import os
import jsonschema as js
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

json_list = os.listdir(os.getcwd())

json_list.pop(json_list.index("schema_checker.py"))
json_list.pop(json_list.index("schema.json"))
json_list.pop(json_list.index("example_sourcebook.jsonc"))

for json_file in json_list:
    with open(json_file) as f:
        data_json = json.load(f)

    with open("schema.json") as f:
        data_schema = json.load(f)
    try:
        js.validate(data_json, data_schema)

    except:
        print("Error")

print("Check completed")