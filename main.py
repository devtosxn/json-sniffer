import json
from sniffer import Sniffer


sniffer = Sniffer("./data/data_1.json", strict=True)
schema = sniffer.sniff_schema()

with open("schema.json", "w") as file:
    json.dump(schema, file, indent=2)
