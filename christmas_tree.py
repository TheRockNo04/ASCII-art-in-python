"""
          ♢
         ---
        ** **
       -------
      **** ****
     -----------
    ****** ******
   ---------------
  ******** ********
 -------------------
********** **********
        █████
        █████
"""
import random

height = int(input('Enter height : '))
print()

characters = ["*", "✪","※","❆","❄︎","⚙︎","✵", "*","*","*","*","*","*","*","*","*","*","*","*"]

for i in range(height):
    print(" ", end="")
print("⚝")


for row in range(height):
    for i in range(height -row -1):
        print(' ', end='')
    for i in range(row+1):
        if row%2 == 1:
            print(characters[random.randint(0, len(characters)-1)], end='')
        else:
            print('-', end='')
    if row%2 == 1:
        print(' ', end='')
    else:
        print('-', end="")
    for i in range(row+1):
        if row%2 == 1:
            print(characters[random.randint(0, len(characters)-1)], end='')
        else:
            print('-', end='')
    print()


for x in range(2):
    for i in range(height - 2):
        print(" ", end="")
    for i in range(5):
        print("█", end="")
    print()

print()