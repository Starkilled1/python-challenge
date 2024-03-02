import csv
import os

election_csv = os.path.join( "Resources", "election_data.csv")

candidates=[]
candidates_names=[]
count_per_name=[]

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
    
    # we append the candidate name alphabetically 
    candidates_names.append(name)
    # we count the number of times the name of each candidate appears inside this loop
    # this loop will only iterate per unique name and each time we store the count function
    # result in a new list that will correspond to the names list
    count_per_cand = candidates.count(name)
    # store the each count in a list which is going to contain the number of votes
    count_per_name.append(count_per_cand)
    
print(count_per_name)

print("Election Results") 
print("-------------------------")
print("Total Votes: " + str(len(candidates)))    
print("-------------------------")