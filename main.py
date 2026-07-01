import random
print("----- Number Guessing Game -----")

secret_num=random.randint(1,100)

guess_num=int(input("Enter your guess no (1-100): "))
print("Guess no: ", guess_num)

attempt=1

while guess_num != secret_num and attempt<7:
    if guess_num< secret_num:
        print("Too Low!! Try Again.")

    else:
        print("Too High!! Try Again.")

    guess_num=int(input("Enter your guess number again: "))
    attempt+=1

if guess_num == secret_num:
    print("Hurrey!! You guessed it right ")
    print("Secret number was: ", secret_num)
    print("Attempts: ", attempt)

else:
    print("Game over!!")
    print("You have used all your attempts.")
    print("Secret number was: ",secret_num)

option=input("Want to play again? (Y/N): ")
if option == "Y" or option == "y":
    print("Play Again!")
    
else:
    print("Thanks for playing!.")