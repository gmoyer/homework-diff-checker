import difflib
import re
import sys
import os


#I compare each line with its most similar line, and add up all the of the differences between them
#This scores two rearranged codes as the same
def listdiff(a, b):
    total = 0
    for i in range(len(a)):
        rowbest = float('inf')
        for j in range(len(b)):
            rowbest = min(rowbest, linediff(a[i], b[j]))
        total += rowbest
    return total

#Damerau-Levenshtein Distance Algorithm
#transcribed from pseudocode on https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
def linediff(a, b):
    n = len(a)
    m = len(b)
    d = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        d[i][0] = i
    for j in range(m+1):
        d[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(
                d[i-1][j] + 1, #deletion
                d[i][j-1] + 1, #insertion
                d[i-1][j-1] + cost #subsitution
                )
            if i > 1 and j > 1 and a[i-1] == b[j-2] and a[i-2] == b[j-1]:
                d[i][j]= min(
                    d[i][j], #the same if the other doesn't make it better
                    d[i-2][j-2] + 1 #transposition
                    )
    return d[n][m]

def listInsert(l, x):
    #l = list
    #x = touple to insert
    #compares the first item in the touple
    i = 0
    while i < len(l) and l[i][0] < x[0]:
        i += 1
    l.insert(i, x)


#with open('hirschlauren_9552_1267170_hw5-1.py') as file1:
#    text1 = file1.readlines()

#with open('lowelukas_9473_1267525_hw_05.py') as file2:
#    text2 = file2.readlines()

path = input("Enter directory to compare: ")

directory = [(file, open(os.path.join(path, file)).readlines()) for file in os.listdir(path)]

out = []

for i in range(len(directory)):
    for j in range(i+1, len(directory)):
        comp = listdiff(directory[i][1], directory[j][1])
        listInsert(out, (comp, directory[i][0], directory[j][0]))

print(out)

with open('out.txt', 'w') as outFile:
    for line in out:
        for detail in line:
            outFile.write(str(detail) + ',')
        outFile.write('\n')




