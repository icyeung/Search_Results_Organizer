import os
import csv
import pandas as pd

__location__ = os.path.realpath(os.join(os.getcwd(), os.path.dirname(__file__)))


numofLines = 0

searchTerm1 = []
searchTerm2 = []

searchFilteredDF = pd.DataFrame()

with open(os.path.join(__location__, 'Factiva & ProQuest Comparison (1)'), 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
        if not row[0] == "" and numofLines > 0:
            searchTerm1.append(row[0])
            numofLines += 1
        if not row[1] == "" and numofLines > 0:
            searchTerm2.append(row[1])
            numofLines += 1
        else:
            numofLines += 1

for result2 in searchTerm2:
    for result1 in searchTerm1:
        if result1 == result2:
            searchTerm2.remove(result1)

searchFilteredDF['sea grant AND acidification'] = searchTerm1
searchFilteredDF['sea grant ocean acidification'] = searchTerm2

display(searchFilteredDF)