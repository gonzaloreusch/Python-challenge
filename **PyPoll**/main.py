import os
import csv
# Path to collect data
election_data = os.path.join("Resources","election_data.csv")
#set to cero
Totvotes = 0
candidate = ""
Wvotes = 0
Winner = ""
Candvotes = {}
Cperct = {}
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    #loop for votes
    for row in csv_reader:
        Totvotes = Totvotes + 1
        candidate = row[2]
        if candidate in Candvotes:
            Candvotes[candidate] = Candvotes[candidate] + 1
        else:
            Candvotes[candidate] = 1
# loop for percentages
for 

      