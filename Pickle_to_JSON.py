# import libraries
import pickle
import json
import sys
import os

# open pickle file
with open(sys.argv[1], 'rb') as infile:
    obj = pickle.load(infile)

# convert pickle object to json object
json_obj = json.loads(json.dumps(obj, default=str))

# write the json file
with open(
        os.path.splitext(sys.argv[1])[0] + '.json',
        'w',
        encoding='utf-8'
    ) as outfile:
    json.dump(json_obj, outfile, ensure_ascii=False, indent=4)


# how to convert json_obj back to the pickle

# import libraries
import pickle
import json
import sys
import os

# open JSON file
with open(sys.argv[1], 'r', encoding='utf-8') as infile:
    json_str = infile.read()

# convert JSON string to JSON object
json_obj = json.loads(json_str)

# convert JSON object to Pickle object
obj = json_obj

# write the Pickle file
with open(
        os.path.splitext(sys.argv[1])[0] + '.pkl',
        'wb'
    ) as outfile:
    pickle.dump(obj, outfile)
