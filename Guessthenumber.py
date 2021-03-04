'''Exercise - Guess the number: Guess a number selected by the programmer. Number of guesses are limited 5. Also, print the number of guesses remaining.
Print game over if the user has exhausted all his trials'''

my_num=10
i=1
while i<6:
    user_num =int(input('Guess a number:')) #asking input from a user
    if my_num==user_num:
        print('Congrats, you won!')
        print('You won in',i, 'attempts') #the number of attempts to guess the right number
        break
    elif i<10:
        print('You have entered a smaller number')
        print('number of guesses remaining:', 5-i) #this will print the number of guesses remaining for the user
        i=i+1
        continue
    else:
        print('You have entered a larger number')
        print('number of guesses remaining:', 5 - i)
        i=i+1
        continue
print('Game Over! You have exhausted all your available attempts')
