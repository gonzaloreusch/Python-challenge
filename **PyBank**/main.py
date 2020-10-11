import os
import csv

# Path to collect data
budget_data = os.path.join("Resources","budget_data.csv")
#set to cero
revchanges = []
months = []
count_month = 0
profit = 0
curmonth = 0
prevmonth = 0
revchange = 0
#open/read file
with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    next(csv_reader)
     #loop for changes in rev and index
    for row in csv_reader:
         count_month = count_month + 1
         months.append(row[0])
         curmonth = int(row[1])
         profit = profit + curmonth
         if count_month > 1:
             revchange = curmonth - prevmonth
             revchanges.append(revchange)
         prevmonth = curmonth
 #calc. & index.     
sumat = sum(revchanges)
Achange = round(sumat / len(revchanges),2)
Max_change = max(revchanges)
Min_change = min(revchanges)
# +1 for the difference on the cell for the month!!
monthindmax = revchanges.index(Max_change) + 1 
monthindmin = revchanges.index(Min_change) + 1
monthmax = months[monthindmax]
monthmin = months[monthindmin]
#print results. Thanks Gary pointing out what I was missing!!!
print("Financial analysis")
print("*-------------------------------------------*")
print(f"number of months: {len(months)}")
print(f"profit: ${profit}")
print(f"Average change: ${Achange}")
print(f"greatest increase: {monthmax} (${Max_change})")
print(f"greatest decrease: {monthmin} (${Min_change})")
#save to text, Thanks Kylie, for the help!!!
savefile = budget_data.strip(".csv") + "results.txt"
filepath = os.path.join("." , savefile)
with open (filepath,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("--------------------------------------" + "\n")
    text.write(f"number of months: {len(months)}" + "\n")
    text.write(f"profit: ${profit}" + "\n")
    text.write(f"Average change: ${Achange}" + "\n")
    text.write(f"greatest increase: {monthmax} (${Max_change})" + "\n")
    text.write(f"greatest decrease: {monthmin} (${Min_change})" + "\n")


