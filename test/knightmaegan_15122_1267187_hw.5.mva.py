x = int(input("Input positive x: "))
y = int(input("Input positive y: "))
z=x
iteration=0

if x>=0 and y>=0:
    print()
elif x<0 and y<0:
    print("Please input positive number for x \nPlease input positive number for y")
    exit()
elif x<0:
    print("Please input positive number for x")
    exit()
elif y<0:
    print("Please input positive number for y")
    exit()


while iteration<y:
    print("After iteration " + str(iteration + 1) + ": " + str(z))
    z+=x
    iteration+=1
    
if x>=0 and y>0:
    print("x*y = " + str(x*y))
    
    


         