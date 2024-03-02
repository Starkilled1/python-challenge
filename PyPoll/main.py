import csv
import os

election_csv = os.path.join( "Resources", "election_data.csv")

candidates=[]
candidates_names=[]


# this section open the csv file and read the data and store into lists
with open(election_csv) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader: 
        
        candidates.append(row[2])
        

# because we only need the information and not the head column of the csv we pop the first
# entry of the list

candidates.pop(0)

# in order to know how many candidates are and what their name is we need to sort them 
# in alphabetical order and removing the duplicates of the list with set in a for loop

for name in sorted(set(candidates)):
    
    candidates_names.append(name)
    count_per_cand = candidates.count(name)
    

print("Election Results") 
print("-------------------------")
print("Total Votes: " + str(len(candidates)))    
print("-------------------------")