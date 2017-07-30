import json
from pprint import pprint
from collections import OrderedDict

with open('my_file.json') as data_file:
    data = json.load(data_file, object_pairs_hook=OrderedDict)
count = 0
for item in data:
    a = str(item['modulePackage']).split(".")
    item['moduleId'] = a[len(a)-1]

with open("my_file.json", "w") as outfile:
    json.dump(data, outfile)
