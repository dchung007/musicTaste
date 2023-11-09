import json
import glob

result = []
for f in glob.glob("merged_file.json"):
    with open(f, "r") as infile:
        result = json.load(infile)


