import csv
import os

election_csv = os.path.join( "Resources", "election_data.csv")

candidates=[]


# this section open the csv file and read the data and store into lists
with open(election_csv) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader: 
        
        candidates.append(row[2])

# because we only need the information and not the head column of the csv we pop the first
# entry of the list

candidates.pop(0)
print(len(candidates))