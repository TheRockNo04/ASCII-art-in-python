#you will need to install termcolor with pip

"""        🦈🦈                  🦈🐟    🦈
      🐬        🐡            🐟        
          🐟🐟        🐬    🐟          
  🐟    🐠                            🐬
                            🐡          
                        🐡🐡    🐟  🐡  
      🐟              🐟                
🐡                                      
                  🐟                    
                                        
🐠          🐟                  🐠      
⁓⁓      ⁓⁓  ⁓⁓⁓⁓⁓⁓⁓⁓    ⁓⁓⁓⁓⁓⁓    ⁓⁓    
      ⁓⁓  ⁓⁓    ⁓⁓⁓⁓⁓⁓  ⁓⁓⁓⁓⁓⁓⁓⁓  ⁓⁓  ⁓⁓
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""" #the actual output should have colours

import random
import sys
from termcolor import colored, cprint

print()
length = 20
height = 20

sand = "░░"
water= "  "
waves= "⁓⁓"

starting_height = random.randint(10,17)

character = [
"🐟",
"🐟",
"🐠",
"🐡",
"🐬",
"🦈",
]
#I'm aware that emojis aren't part of ascii


for i in range(height):

    if i == starting_height:
        for y in range(length):
            if random.randint(0,1) == 1:
                print(colored(sand, 'blue', "on_yellow"), end="")
            else:
                print(colored(sand, 'blue', "on_yellow", attrs=["dark"]), end="")


    elif i > starting_height:
        for x in range(length):
            
            print(colored(sand, 'yellow', "on_grey"), end="")



    elif i < starting_height:

        if starting_height - i <= random.randint(2,3):
            for d in range(length):
                if random.randint(0,1) == 1:
                    print(colored(waves, 'white', "on_blue"), end="")
                else:
                    print(colored(water, 'white', "on_blue"), end="")
        else:

            for z in range(length):
                if random.randint(1,10) == 3:
                    print(colored(character[random.randint(0, len(character)-1)], "white", 'on_blue'), end="")
                else:
                    print(colored(water, "white", 'on_blue'), end="")
                    


    print()



print()