secret_number = 9
guessing_count = 0
guess_limit = 3
while guessing_count < guess_limit:
    guess = int(input("Guess: "))
    guessing_count += 1
    if guess == secret_number:
        print ("Well done! ")
        break
else:
    print("You failed! ")



