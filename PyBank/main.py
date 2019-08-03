# Import dependencies
import os
import csv

# Input the .csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# Read the .csv file
with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)