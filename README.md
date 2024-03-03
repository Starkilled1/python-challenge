# Python-challenge

This repository contains two folders:
 1. Pybank
 
 2. Pypoll

## Pybank

The Pybank folder contains scripts to analyze budget data from a CSV file spanning from 2010 to 2017. The main script in this folder opens a CSV file, captures the date and budget data, and then processes the data to derive several key insights:

 - Total Number of Months: Calculates the total number of months
   included in the dataset.
 - Net Total Amount of "Profit/Losses": Calculates the net total amount 
   of "Profit/Losses" over the entire period.
 - Changes in "Profit/Losses" over the Entire Period: Calculates the changes   in "Profit/Losses" over the entire period and then computes  
   the average of those changes.
 - Greatest Increase in Profits: Identifies the date and amount   
   corresponding to the greatest increase in profits over the entire   
   period.
 - Greatest Decrease in Profits: Identifies the date and amount   
   corresponding to the greatest decrease in profits over the entire   
   period.

After the data is collected and processed, it is printed on the terminal, and a text file with the same results format as the terminal is created.

  

## Pypoll

The Pypoll folder contains scripts to analyze election data from a CSV file. The resources file contains ballot ID, county, and candidate names. The main script in this folder reads through the CSV file, organizes the information into lists and dictionaries, and processes the data to obtain the following insights:

  

 - Total Number of Votes Cast: Calculates the total number of votes
   cast.
 - List of Candidates Who Received Votes: Provides a complete list of
   candidates who received votes.
 - Percentage of Votes Each Candidate Won: Calculates the percentage of
   votes each candidate won.
 - Total Number of Votes Each Candidate Won: Calculates the total number
   of votes each candidate won.
 - Winner of the Election Based on Popular Vote: Determines the winner
   of the election based on the popular vote.
   
 After processing the data, the results are printed to the terminal,
 and a text file with the same results format is created.

 This code can work with many candidate names since the code searches for each name, and from then on, it performs the analysis.
