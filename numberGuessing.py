import random
print("Number Guessing Game")
number = random.randint(1,9)
chance = 0
print("Guess a number between 1 and 9: ")

while chance < 5:
    guess = int(input("Enter you number: "))


    if guess == number:
        print("Congratulations, you won !")
        break
    elif guess < number:
        print("You guess was too low, Guess a number higher than" , guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)

    chance = chance + 1

if not chance < 5:
    print("Ooof, you lost this ez pz game, git gud")
    print("Btw, the number was ", number)