# Simple program to read a CSV file
# Author: Jenny Formentera

import csv

FILENAME = "data.csv" # name of the data file
DATADIR = "../week01/"  # where the file is located

linecount = 0
total = 0

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0

    for line in reader:
        if linecount == 0: # first row/ header row
            print (f"header: {line}\n-----------------------")
        else: # all subsequent rows
            print (f"row {linecount}: {line}")
            age = int(line[1]) 
            total += age
            linecount += 1
        
        print (f"average is {total/(linecount-1)}")
