import random
number = random.randint(1, 20)

msg = input("Hello! What is your name?")
guessesTaken = 0
print('Well, ' + msg + ', I am thinking of a number between 1 and 20.' )

while guessesTaken < 6:
    print('Take a guess')
    guess = int(input())
    guessesTaken = guessesTaken + 1 
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break        
if guess == number:
    print('Good job,' + msg + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(number))