import random

def sum():
    first_dice = random.randint(1,6)
    second_dice = random.randint(1,6)
    sum_of_dice = first_dice + second_dice
    return sum_of_dice
point = 0
sum_of_dice = sum()
print(sum_of_dice)
if (sum_of_dice == 7 or sum_of_dice == 11):
    if(point == 0 and sum_of_dice == 7):
        print("Lose")
    print("Wins")
elif (sum_of_dice ==2 or sum_of_dice == 3 or sum_of_dice == 12):
    print("Lose")
else:
    point = sum_of_dice
    sum = sum()
    print(sum)
    if(sum == point):
        print("wins")
    else:
        print("Lose")
