import random as rn

height = 10#int(input('Enter height : '))

#Star
print(" " * height + "★")

#Tree
for row in range(height):
    print(' ' * (height-row-1), end='')
    
    for _ in range(row + 1):
        if row%2 == 1: 
            print(rn.choice(['*', chr(rn.randint(33,47))]), end='')
        else:
            print('-', end='')
    
    if row%2 == 1: print(' ', end='')
    else: print('-', end='')
    
    for _ in range(row+1):  
        if row%2 == 1: print(rn.choice(['*', chr(rn.randint(33,47))]), end='')
        else: print('-', end='')
    print()

#Trunk
for _ in range(2):
    print(" " * (height - 2) + "█" * 5)