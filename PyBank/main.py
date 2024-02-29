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
date_data = date
date_data.pop(0)

# we use a for loop to iterate throu the list and we add the number to the variablo net_total
for num in profiloss_num:
    net_total += int(num)
    
#Declare a new list to store the difference between each month 
changes = []
# in this section we subtract -1 to the total len of the list because the last value can't be compared
# in the for loop we subtract the the next value of the loop to the actual one 
# we append the result of the change to the new list

for i in range(len(profiloss_num)-1):
    change = int(profiloss_num[i+1]) - int(profiloss_num[i])
    changes.append(change)
    
# Calculate the average change using the sum function and the len function
averagechange = sum(changes)/len(changes)


# declare variables that would store the index and the greatest increase and decrease
greatestinc = 0
greatestdec = 0
index1 = 0
index2 = 0

# for loop that goes throu the changes list and evaluates every value of the list 

for value in changes:
    if value > greatestinc:
        greatestinc = value  
    
    if value < greatestdec:
        greatestdec = value
        
#another for loop to find where this index are, since in the creation of the changes list
#there is an offset of -1 in the index compared to the dates list so we add +1 to compensate
        
for i in range(len(changes)):
    
    if changes[i] == greatestinc:
        index1 = i + 1
    if changes[i] == greatestdec:
        index2 = i + 1

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')    
print(f'Total: ${net_total}')
print(f"Average Change: ${averagechange:.2f}")
print(f'Greatest Increase in Profits: {date_data[index1]} (${greatestinc})')
print(f'Greatest Decrease in Profits: {date_data[index2]} (${greatestdec})')

output_file = os.path.join( "analysis", "Financial_Analysis.txt")

with open(output_file, "w") as datafile:
    
    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write(f'Total Months: {total_months}\n')    
    datafile.write(f'Total: ${net_total}\n')
    datafile.write(f"Average Change: ${averagechange:.2f}\n")
    datafile.write(f'Greatest Increase in Profits: {date_data[index1]} (${greatestinc})\n')
    datafile.write(f'Greatest Decrease in Profits: {date_data[index2]} (${greatestdec})')