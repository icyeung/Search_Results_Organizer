import os
import csv
import pandas as pd
from IPython.display import display

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


numofLines = 0

searchTerm1 = []
searchTerm2 = []
commonResults = []


searchTerm1DR = []
searchTerm2DR = []

with open(os.path.join(__location__, 'TesterFile.csv'), 'r', encoding = "utf8") as csvfile:
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

print("Number of Results for Search Term 1 Originally: ", len(searchTerm1))
print("Number of Results for Search Term 2 Originally: ", len(searchTerm2))

for result in searchTerm1:
    if result not in searchTerm1DR:
        searchTerm1DR.append(result)

print(searchTerm1DR)

for result in searchTerm2:
    if result not in searchTerm2DR:
        searchTerm2DR.append(result)

print(searchTerm2DR)

print("Number of Results for Search Term 1 After Duplicates Removed: ", len(searchTerm1DR))
print("Number of Results for Search Term 2 After Duplicates Removed: ", len(searchTerm2DR))

for result1 in searchTerm1DR:
    for result2 in searchTerm2DR:
        if result1 == result2:
            print(result1)
            commonResults.append(result1)
            searchTerm2DR.remove(result1)
            searchTerm1DR.remove(result1)
            

searchFilteredDF = pd.DataFrame({'sea grant AND acifification (with quotations)': pd.Series(searchTerm1DR), 'sea grant ocean acidification': pd.Series(searchTerm2DR), 'Results in Common': pd.Series(commonResults)})

searchFilteredDF.to_excel("Test.xlsx", index=False)

display(searchFilteredDF)