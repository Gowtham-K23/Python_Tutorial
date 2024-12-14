no = 10

i = 1
while (i<=3):

    guess = int(input("Guess: "))

    if (guess == no):
        print("You win!")
        break

    i = i + 1
    if (i > 3):
        print("Sorry you have failed!")
