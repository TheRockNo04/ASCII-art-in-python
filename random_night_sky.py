import random

components = [
'。', 
'. ', 
'ﾟ ', 
', ', 
'☆ ', 
'．', 
'o ', 
'  ', 
'  ', 
'  ', 
'  ', 
'  ', 
'  ', 
'  ', 
'  ', 
'  ', 
'* ', 
'＋', 
'+ ', 
'´ ', 
'｡ ', 
'` ', 
'° ', 
'ｏ ',
'⭐ ',
'。', 
'. ', 
'ﾟ ', 
', ', 
'☆ ', 
'．', 
'o ', 
'  ', 
'  ', 
'  ', 
'  ', 
'  ', 
'  ', 
'  ', 
'  ', 
'  ', 
'* ', 
'＋', 
'+ ', 
'´ ', 
'｡ ', 
'` ', 
'° ', 
'ｏ '
]
#I am aware that they aren't all the same length, but they're close enough

length = 20
height = 20
previous = ""

for i in range(height):

    for x in range(length):
        if previous == " ":
            if random.randint(1, 10) >= 1:
                print(" ", end="")
            else:
                component_chosen = random.randint(0, len(components))
                print(components[component_chosen], end="")
                previous = " "

        else:
            component_chosen = random.randint(0,len(components)-1)
            print(components[component_chosen], end="")
            previous = component_chosen
        
    print()