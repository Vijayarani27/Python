#Guessing Game

number = 100
count = 0
guess=int(input("Enter the value:"))
while count<3:
    if guess<number:
        print("Your guess is lesser")
    elif guess>number:
        print("Your guess is greater")
    else:
        print("correct answer")
        break
    if count<2:
        guess=int(input("Enter the value:"))
    count = count+1   
else:
    print("Game Over")
    raise ValueError("You exceeded the minimum attempts")
