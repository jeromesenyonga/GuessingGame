secret_number = 9 #var to store our secret number
guess_count = 0 #this represents the number of guesses the user has made
guess_limit = 3
while guess_count < guess_limit: #our condition
    guess = int(input("Guess: ")) #we get the guess from the user's input and store it in a variable
    guess_count += 1
    if guess == secret_number:
        print("You Won!")
        break

else:
    print("Sorry, you failed!")