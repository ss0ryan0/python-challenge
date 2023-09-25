import os
import csv
csvpath = os.path.join('Resources','budget_data.csv')

#1
with open(csvpath, encoding='UTF-8') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  months = [row[0] for row in csvreader] # creating an empty list of months for extraction
  total_months = len(months[1:]) #counts number of months excluding the header row
  print(f'Total Months: {total_months}')

#2
with open(csvpath, encoding='UTF-8') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')   
  profitwheader = [row[1] for row in csvreader] # define the profit/loss column
  profitstr = profitwheader[1:] #ignore the header
  profit = [eval(n) for n in profitstr] # turn strings into int
  net = sum(profit)
  print(f'Net Profit/Loss: ${net}')

#3 # define first profit
  change = [profit[i] - profit[i - 1] for i in range(1, len(profit))] # list comp to iterate through the changes
  avg = float(sum(change) / (len(profit)-1)) # average of those changes
  print(f'Average Change: ${avg}')

  #find extremes
  ouzouka = max(change) # greatest increase in profit (date & amount)
  ougenshou = min(change)

  #obtain index of change
  csvreader = csv.reader(csvfile, delimiter=',')  
  imax = change.index(ouzouka)
  imin = change.index(ougenshou)
  
  with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    datewheader = [row[0] for row in csvreader]
    date = datewheader[2:] #skip the header and the first date (since no change happened yet)
    print(f'Greatest Increase: {date[imax]} ({ouzouka})')
    print(f'Greatest Decrease: {date[imin]} ({ougenshou})')
    