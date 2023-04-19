import json
import os
import sys
from sniffer import Sniffer


strict = False if len(sys.argv) > 1 and sys.argv[1] == 'nostrict' else True
print("Strict mode for parsing: {}".format(strict))

schema_dir = "./schema"
os.makedirs(schema_dir, exist_ok=True)

#ENTER YOUR JSON FILE HERE
json_file = "./data/data_1.json"

file_number = os.path.splitext(json_file)[0].split("_")[-1]
file_number = int(file_number) if file_number.isnumeric() else 0
schema_file = f"{schema_dir}/schema_{file_number}.json"
        

sniffer = Sniffer(json_file, strict=strict)
schema = sniffer.sniff_schema()

with open(schema_file, "w") as file:
    json.dump(schema, file, indent=2)
