import os
import csv
import pandas as pd
from IPython.display import display

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Steps needed:
# 1. Open ProQuest Results File
# 2. Open Comparison xx File
# 3. Extract ProQuest columns- if more tnan one, use separate lists
# 4. Extract Results in Common
# 5. For title in list, find corresponding row in ProQuest Results File
# 6. Extract only link from ProQuest Results
# 7. Store title, link as tuple
# 8. Dataframe to store info
# Create a function for extraction and storage
#   -Need one call for each ProQuest column and Results in Common


# Line counter to not extract header as title
numofLines = 0


# 
uniqueResults1 = []
uniqueResults2 = []
commonResults = []

links1 = []
links2 = []
links3 = []
   
# Opens ProQuest Results 
proquestResults = pd.read_csv(os.path.join(__location__, 'ProQuest Results sea grant AND acidification (with quotations).csv'), usecols=["Title", "DocumentUrl"], encoding="utf8")

proquestResultsDR = proquestResults.drop_duplicates(subset=["Title"], keep="first", inplace=False)

proquestResultsDR.to_excel("ProQuest Results Tester DR.xlsx", index = False)

# Opens titles
with open(os.path.join(__location__, 'Comparison 3 Test.csv'), 'r', encoding = "utf8") as csvfile:
    lines = csv.reader(csvfile, delimiter=",")
    for row in lines:
        if not row[0] == "" and numofLines > 0:
            uniqueResults1.append(row[0])
            numofLines += 1
        if not row[1] == "" and numofLines > 0:
            uniqueResults2.append(row[1])
            numofLines += 1
        if not row[2] == "" and numofLines > 0:
            commonResults.append(row[2])
            numofLines += 1
        else:
            numofLines += 1


for title1 in uniqueResults1:
    for titleDirectory in proquestResultsDR.Title:
        if title1 == titleDirectory:
            result1 = proquestResultsDR.loc[proquestResultsDR["Title"] == title1, "DocumentUrl"].values[0]
            links1.append(result1)
print(links1)

for title2 in uniqueResults2:
    for titleDirectory in proquestResultsDR.Title:
        if title2 == titleDirectory:
            result2 = proquestResultsDR.loc[proquestResultsDR["Title"] == title2, "DocumentUrl"].values[0]
            links2.append(result2)
print(links2)

for title3 in commonResults:
    for titleDirectory in proquestResultsDR.Title:
        if title3 == titleDirectory:
            result3 = proquestResultsDR.loc[proquestResultsDR["Title"] == title3, "DocumentUrl"].values[0]
            links3.append(result3)
print(links3)

linkedResultsDF = pd.DataFrame({'Factiva Titles: sea grant AND acidification (with quotations)': pd.Series(uniqueResults1), 
                              'Factiva Links': pd.Series(links1),
                              'ProQuest Titles: sea grant AND acidification (with quotations)': pd.Series(uniqueResults2), 
                              'ProQuest Links': pd.Series(links2),
                              'Common Results Title': pd.Series(commonResults), 
                              'Common Results Link:': pd.Series(links3)})

linkedResultsDF.to_excel("Tester Linker.xlsx", index=False)

display(linkedResultsDF)