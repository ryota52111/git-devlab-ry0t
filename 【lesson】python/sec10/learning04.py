# import json

# data = {
#     "Int": 6,
#     "Float": 6.6,
#     "String": "Python3",
#     "List": [7, 8, "F", "E"],
#     "Dict":{"C": 2,"D": 3},
#     "Tuple": (2, 3.4, None),
#     "Bool": [True, False],
#     #　×"Set"
# }


# filename = r"C:\Users\r_sas\Desktop\hello_sublime\sec10\json_sample.json"
# with open(filename, "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=4)

import json
import pprint

filename = r"C:\Users\r_sas\Desktop\hello_sublime\sec10\json_sample.json"
with open (filename, "r", encoding="utf-8") as f:
    data = json.load(f)

pprint.pprint(data)
