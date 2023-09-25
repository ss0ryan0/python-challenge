import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
with open (csvpath, encoding='UTF-8') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  #1 total number of votes cast
  votes = [row[0] for row in csvreader]
  total_votes = len(votes) - 1 
  print('Election Results')
  print(f'Total Votes: {total_votes}')

  #2 list the candidates by name
  with open (csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    unsorted_candidates = [row[2] for row in csvreader]
    
    candidates = []
    for i in range(1, total_votes):

      if unsorted_candidates[i+1] != unsorted_candidates[i] and unsorted_candidates[i+1] not in candidates: #if the prev name != the next name, and the name hasn't already been added, add it to the list
        candidates.append(unsorted_candidates[i+1])

    #assign names in list to the name variable
    DeGette = candidates[0] 
    Doane = candidates[1]
    Stockham = candidates[2]
    
    #3 the total amount of votes each canditate won using collections
    import collections #will be used to tally votes
    freq = collections.Counter() 
    for name in unsorted_candidates:
      if name in candidates:
        freq[name] += 1
    DeGetters = freq.get(DeGette)
    Stockhammers = freq.get(Stockham)
    Doaners = freq.get(Doane)

    #the % of votes each candidate won
    dgp = (DeGetters / total_votes) * 100
    sp = (Stockhammers / total_votes) * 100
    dp = (Doaners / total_votes) * 100

    print(f'{Stockham}: {sp}% ({Stockhammers})')
    print(f'{DeGette}: {dgp}% ({DeGetters})')
    print(f'{Doane}: {dp}% ({Doaners})')

    #find winner using itemgetter
    from operator import itemgetter
    results = [(Stockham, sp), (DeGette, dgp), (Doane, dp)]
    winner = max(results, key = itemgetter(1))[0]
    print(f'Winner: {winner}')
