

#a = [5, 8, 9, 1, 1, 0, 8, 8]
#a = [5, 4, 0, 5, 6, 4, 0, 5]
a = [5, 5, 4]
a1 = []
b1 = []

n = len(a)

def ave(a):
    t = 0
    for e in a:
        t += e
    return t/len(a)

def f(x, ave):
    return 2 ** (-x+ave)

modifier = 1
totalModifier = 0
average = ave(a)

for i in range(0, n):
    modifier *= f(a[i], average)
    totalModifier += modifier

print(totalModifier)
print(average/totalModifier)
