import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
with open (csvpath, encoding='UTF-8') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
    #total number of votes cast
  total_votes = len(row[0] for row in csvreader) 
  print(f'Total Votes: {total_votes}')
  #unsorted_candidates = [row[3] for row in csvreader]
  #candidates = [profit[i] - profit[i - 1] for i in range(1, len(profit))]
    #count all the candidates by name

    #the % of votes each candidate won
    #the total amount of votes each canditate won
    #the winner

