import random 

looping = True
secret = random.randint(1, 100)

while looping:
    guess = input("What is your guess? (q for quit) >> ")
    if guess == 'q':
        break
    if not guess.isdigit():
        print("Number from 1-100 only or q please.")
        continue
    
    guess = int(guess)
    if secret == guess:
        print("You got it!")
        break
    if guess < secret:
        print("Too low")
    else:
        print("Too high")
    if not 1 <= guess <= 100:
        print("It's between 1 and 100")
        
print("Game over")
