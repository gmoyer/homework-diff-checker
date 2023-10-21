

x = int(input("input positive x:"))
y = int(input("input positive y:"))

if y >= 0:
    print()
else:
    print("please input positive number for y")
    
if x >= 0:
    print()
else:
    print("please input positive number for x")
    exit()

iteration=0
z = x

while iteration < y:
    print("After iteration " + str(iteration+1) + ": " + str(z))
    iteration +=1
    z += x
    
    
if x>= 0 and y>0:
    print("x * y = " + str((x*y))) 


    

