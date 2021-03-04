print("""Guess the magic number!
    -Created by Shagun Singh\n\n""")
print("You have to guess the magic number in 6 attempts!\n\n")
my_magic= 369
# this is my magic number
i=0
num=[]
while i<6:

    your_num= int(input('Guess a number between 300 to 400:\n')) #input your number here
    
    if your_num>400 or your_num<300:
        print('Please enter a number between 300 to 400\n')
        num.append('m')
        i=i+1
        continue
        
        
    elif your_num!=my_magic:
        print('Not a good guess :(')
        
        if your_num<my_magic:
            print('Please enter a larger number\n')
        else:
            print('Please enter a smaller number\n')
        num.append('m')
        i=i+1
        
    else:
        print('You are a genius :) \n')
        break
        
        
print('You have guessed the correct answer in:',num.count('m')+1, 'attempts!\n')
print('Game over!')
