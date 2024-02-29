import csv
import os

budget_csv = os.path.join( "Resources", "budget_data.csv")

date = []
date_data = []
profiloss = []
profiloss_num = []


with open(budget_csv) as csvfile:
    
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        
        date.append(row[0])
        
        profiloss.append(row[1])
        
# To calculate the total amount of months you have see the len of the list and 
# subtract 1 because the first variable of the list is the header of the column 
total_months = len(date)-1

net_total = 0
# copy the list to another list and the second one we delete the first element of the list

profiloss_num = profiloss
profiloss_num.pop(0)

# we use a for loop to iterate throu the list and we add the number to the variablo net_total
for num in profiloss_num:
    net_total += int(num)

print(net_total)