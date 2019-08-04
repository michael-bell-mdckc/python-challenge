# Import dependencies
import os
import csv

# Identify the input .csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# Read the .csv file
with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

    # Lists
    date = []
    p_and_l = []
    p_and_l_change = []

    for row in csvreader:

        date.append(row[0])
        p_and_l.append(int (row[1]))

    print("Financial Ananlysis")
    print("-------------------")
    print("Total Months:", len(date))
    print("Total: $", sum(p_and_l))

    for i in range(1,len(p_and_l)):

        p_and_l_change.append(p_and_l[i] - p_and_l[i-1])
        average_p_and_l_change = sum(p_and_l_change) / len(p_and_l_change)
        greatest_p_and_l_change = max(p_and_l_change)
        least_p_and_l_change = min(p_and_l_change)

        greatest_p_and_l_change_date = date[p_and_l_change.index(greatest_p_and_l_change)]
        least_p_and_l_change_date = date[p_and_l_change.index(least_p_and_l_change)]

    print("Average Change: $", average_p_and_l_change)
    print("Greatest Increase in Profits:", str(greatest_p_and_l_change_date), greatest_p_and_l_change)
    print("Greatest Decrease in Profits:", str(least_p_and_l_change_date), least_p_and_l_change)
