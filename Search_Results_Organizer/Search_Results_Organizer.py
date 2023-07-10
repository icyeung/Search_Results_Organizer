import os
import csv
import pandas as pd
from IPython.display import display

# Used to help open files in Python code folder
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Line counter to not extract header as title
numofLines = 0

# Lists to hold original data
searchTerm1 = []
searchTerm2 = []
commonResults = []

# Lists to hold data without duplicates
searchTerm1DR = []
searchTerm2DR = []

# Lists to hold unique results
unique1 = []
unique2 = []


with open(os.path.join(__location__, 'Factiva & ProQuest Comparison (4).csv'), 'r', encoding = "utf8") as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')

    # Gets rid of empty cells within column lists
    # Does not extract header as a title
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


# Removes duplicates for first search term
for result in searchTerm1:
    if result not in searchTerm1DR:
        searchTerm1DR.append(result)

# print(searchTerm1DR)

# Removes duplicates for second search term
for result in searchTerm2:
    if result not in searchTerm2DR:
        searchTerm2DR.append(result)


print("Number of Results for Search Term 1 After Duplicates Removed: ", len(searchTerm1DR))
print("Number of Results for Search Term 2 After Duplicates Removed: ", len(searchTerm2DR))


# Looks for matching results between two dearch terms
for result2 in searchTerm2DR:
    if result2 not in searchTerm1DR:
        unique2.append(result2)
    else:
        commonResults.append(result2)

for result1 in searchTerm1DR:
    if result1 not in commonResults:
        unique1.append(result1)
            
# Creates dataframe to display unique links and links in common for search terms
searchFilteredDF = pd.DataFrame({'sea grant ocean acidification': pd.Series(unique1), 'sea grant coastal acidification': pd.Series(unique2), 'Results in Common': pd.Series(commonResults)})

# Saves dataframe as an excel with specified name "Comparison __.xlsx"
searchFilteredDF.to_excel("Comparison 4.xlsx", index=False)

display(searchFilteredDF)