# Simple program to read in as a Dictionary object
# Author: Jenny Formentera

import csv

FILENAME = "data.csv" # name of the data file
DATADIR = "../week01/"  # where the file is located

total = 0
count = 0

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)

    for line in reader:
        total += line['age']
        count += 1

print (f"average is {total/(count)}") # why is there no -1 this time?