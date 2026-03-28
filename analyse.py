#! /usr/bin/env python

import os
import csv
from pprint import pprint

header = None

in_script_dir = lambda name: os.path.join(os.path.dirname(__file__), name)

with open(in_script_dir("data.csv"), newline="") as f:
    reader = csv.reader(f, delimiter=",")

    # Remove duplicates
    data = {}
    for i, row in enumerate(reader):
        if i == 0:
            header = row
            continue

        if row[5] == "House of Tangrams": # Filter for House of Tangrams runs
            data[row[2]] = row

    data = list(data.values())

# Filter for won games
data = list(filter(lambda x: x[6] == "1", data))

# Filter for zero hints
data = list(filter(lambda x: x[11] == "0", data))

with open(in_script_dir("cleaned_data.csv"), "w", newline="") as f:
    writer = csv.writer(f, delimiter=",")

    writer.writerow(header)
    writer.writerows(data)
