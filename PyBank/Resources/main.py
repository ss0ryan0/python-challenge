import os
import csv
csvpath = os.path.join('python-challenge', 'PyBank', 'Resources', 'budget_data.csv')
with open (csvpath, encoding='UTF-8') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=', ')
