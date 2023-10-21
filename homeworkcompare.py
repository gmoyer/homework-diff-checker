import os


#I compare each line with its most similar line, and add up all the of the differences between them
#This scores two rearranged codes as the same
def listdiff(a, b):

    if len(a) > len(b): #swap so larger gets compared to smaller
        list1 = a
        list2 = b
    else:
        list1 = b
        list2 = a

    
    total = 0
    for i in range(len(list1)):
        rowbest = float('inf')
        for j in range(len(list2)):
            rowbest = min(rowbest, linediff(list1[i], list2[j]))
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
    return d[n][m]

def listInsert(l, x):
    #l = list
    #x = touple to insert
    #compares the first item in the touple
    i = 0
    while i < len(l) and l[i][0] < x[0]:
        i += 1
    l.insert(i, x)

path = input("Enter directory to compare: ")

directory = [(file, [item.replace(" ", "") for item in open(os.path.join(path, file)).readlines() if item != '\n']) for file in os.listdir(path)]

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




