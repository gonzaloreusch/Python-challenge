import os
import csv
# Path to collect data . Thank you Jennifer Powell for showing me this form for path finding.
election_data = "//Users//gonzaloreusch//Desktop//DA&V Commits //Python-challenge//**PyPoll**//Resources//election_data.csv"
#set to cero
Totvotes = 0
candidate = ""
Wvotes = 0
Winner = ""
Candvotes = {}
Cperct = []
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    #loop for votes
    for row in csvreader:
        Totvotes = Totvotes + 1
        candidate = row[2]
        if candidate not in Candvotes: #Gracias Emilio!!!
            Candvotes[candidate] = 1
        else:
            Candvotes[candidate] += 1
        # if candidate in Candvotes:    ***old ver that did not work***
        #     Candvotes[candidate] = Candvotes[candidate] + 1
        # else:
        #     Candvotes[candidate] = 1
# loop for percentages

for k, v in Candvotes.items():
    Cperct += f'{k}: {"{:.3%}".format(v/Totvotes)} ({v}) \n'
    if v > Wvotes:
        Wvotes = v
        Winner = k
  
dashbreak = "---------------------------------------"
print("election result")
print(dashbreak)
print(f"Total votes: {Totvotes}")
print(dashbreak)
print(f"winner")
print(dashbreak)
#save to text, Thanks Kylie, for the help!!!
savefile = election_data.strip(".csv") + "results.txt"
filepath = os.path.join("." , savefile)
with open (filepath,'w') as text:
    text.write("dashbreak" + "\n")
    text.write(f"total votes: {Totvotes}" + "\n")
    text.write("dashbreak" + "\n")
    for name, votecount in Candvotes.items():
        text.write(f"{name}: Cperct[name](votecount)" + "\n")
        text.write("dashbreak" + "\n")
        text.write(f"Winner:" + "\n")
        text.write("dashbreak" + "\n")
