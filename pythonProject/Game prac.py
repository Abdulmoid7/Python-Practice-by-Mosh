secret_number = 9
wrong_number = 10

guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
     guess = int(input('Guess: '))
     guess_count += 1
if guess == secret_number:
     print('Congratulations! You won')

elif guess == wrong_number:
    print('Bad Luck! You failed')

if guess_count == guess_limit and guess != secret_number:
    print('Sorry! You are out of the guess')

print('Game Over')
