# Import dependencies
import os
import csv

# Identify the input .csv file
csvpath = os.path.join("Resources", "election_data.csv")

# Read the .csv file
with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

    # Variables
    Khan_vote = 0
    Correy_vote = 0
    Li_vote = 0
    Otooley_vote = 0

    # Lists
    voter_id = []
    candidate = []

    for row in csvreader:

        voter_id.append(row[0])
        candidate.append(row[2])

    print("Election Results")
    print("----------------")
    print("Total Votes:", len(voter_id))
    print("----------------")

    for i in range(len(voter_id)):

        if candidate[i] == str("Khan"):
            Khan_vote = Khan_vote + 1
        elif candidate[i] == str("Correy"):
            Correy_vote = Correy_vote + 1
        elif candidate[i] == str("Li"):
            Li_vote = Li_vote + 1
        else:
            Otooley_vote = Otooley_vote + 1

    Khan_percentage = (Khan_vote / len(voter_id)) * 100
    Correy_percentage = (Correy_vote / len(voter_id)) * 100
    Li_percentage = (Li_vote / len(voter_id)) * 100
    Otooley_percentage = (Otooley_vote / len(voter_id)) * 100

    Winner = [Khan_vote,Correy_vote,Li_vote,Otooley_vote]

    #     p_and_l_change.append(p_and_l[i] - p_and_l[i-1])
    #     average_p_and_l_change = sum(p_and_l_change) / len(p_and_l_change)
    #     greatest_p_and_l_change = max(p_and_l_change)
    #     least_p_and_l_change = min(p_and_l_change)

    #     greatest_p_and_l_change_date = date[p_and_l_change.index(greatest_p_and_l_change)]
    #     least_p_and_l_change_date = date[p_and_l_change.index(least_p_and_l_change)]

    print("Khan:", Khan_percentage, Khan_vote)
    print("Correy:", Correy_percentage, Correy_vote)
    print("Li:", Li_percentage, Li_vote)
    print("O'Tooley:", Otooley_percentage, Otooley_vote)
    print("----------------")
    print("Winner:", max(Winner))