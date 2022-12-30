import random
print()
length = 40
height = 20

sand = "█"
water = " "
waves = "⁓"

starting_height = random.randint(3,15)





for i in range(height):

    if i == starting_height:
        for y in range(length):
            if random.randint(0,1) == 1:
                print(waves, end="")
            else:
                print(" ", end="")


    elif i > starting_height:
        for x in range(length):
            print(sand, end="")
    elif i < starting_height:

        if starting_height - i <= 2:
            for d in range(length):
                if random.randint(0,1) == 1:
                    print(waves, end="")
                else:
                    print(" ", end="")
        else:

            for z in range(length):
                print(water, end="")


    print()



print()