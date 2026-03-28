#! /usr/bin/env python

import os
import csv

import numpy as np
import matplotlib.pyplot as plt

in_script_dir = lambda name: os.path.join(os.path.dirname(__file__), name)

# Read data
with open(in_script_dir("filtered_data.csv"), newline="") as f:
    data = list(csv.reader(f, delimiter=","))[1:]

# Extract time data
data = list(map(lambda x: float(x[4]), data))

plt.title("Filtered Data")
plt.xlabel("Student")
plt.ylabel("Completion Time [s]")
plt.scatter(np.linspace(1, len(data), len(data)), data)
plt.grid()
plt.tight_layout()
plt.savefig("filtered_data.png")

plt.clf()
plt.title("Filtered & Ascendingly Sorted Data")
plt.xlabel("Student")
plt.ylabel("Completion Time [s]")
plt.scatter(np.linspace(1, len(data), len(data)), sorted(data))
plt.grid()
plt.tight_layout()
plt.savefig("sorted_filtered_data.png")
