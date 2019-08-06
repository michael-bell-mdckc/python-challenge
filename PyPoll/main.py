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
    print("Total Votes:" + str(len(voter_id)))
    print("----------------")

    #Vote counter
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

    votes = [Khan_vote, Correy_vote, Li_vote, Otooley_vote]

    #Winner
    if max(votes) == Khan_vote:
        winner = str("Khan")
    elif max(votes) == Correy_vote:
        winner = str("Correy")
    elif max(votes) == Li_vote:
        winner = str("Li")
    else:
        winner = str("O'Tooley")

print("Khan: " + str("{0:.2f}".format(Khan_percentage)) + "%" + " (" + str(Khan_vote) + ")")
print("Correy: " + str("{0:.2f}".format(Correy_percentage)) + "%" + " (" + str(Correy_vote) + ")")
print("Li: " + str("{0:.2f}".format(Li_percentage)) + "%" + " (" + str(Li_vote) + ")")
print("O'Tooley: " + str("{0:.2f}".format(Otooley_percentage)) + "%" + " (" + str(Otooley_vote) + ")")
print("----------------")
print("Winner: " + winner)

#Print to file
txtfile = "output.txt"

with open(txtfile, "w") as output_file:

    output_file.write("Election Results")
    output_file.write("\n")
    output_file.write("----------------")
    output_file.write("\n")
    output_file.write("Total Votes: " + str(len(voter_id)))
    output_file.write("\n")
    output_file.write("----------------")
    output_file.write("\n")
    output_file.write("Khan: " + str("{0:.2f}".format(Khan_percentage)) + "%" + " (" + str(Khan_vote) + ")")
    output_file.write("\n")
    output_file.write("Correy: " + str("{0:.2f}".format(Correy_percentage)) + "%" + " (" + str(Correy_vote) + ")")
    output_file.write("\n")
    output_file.write("Li: " + str("{0:.2f}".format(Li_percentage)) + "%" + " (" + str(Li_vote) + ")")
    output_file.write("\n")
    output_file.write("O'Tooley: " + str("{0:.2f}".format(Otooley_percentage)) + "%" + " (" + str(Otooley_vote) + ")")
    output_file.write("\n")
    output_file.write("----------------")
    output_file.write("\n")
    output_file.write("Winner: " + winner)