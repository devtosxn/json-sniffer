import json
import sys
from sniffer import Sniffer


strict = False if len(sys.argv) > 1 and sys.argv[1] == 'nostrict' else True
print("Strict mode for parsing: {}".format(strict))
        

sniffer = Sniffer("./data/data_1.json", strict=strict)
schema = sniffer.sniff_schema()

with open("schema.json", "w") as file:
    json.dump(schema, file, indent=2)
