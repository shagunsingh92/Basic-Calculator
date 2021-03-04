import random
i=1
you_won=0
you_lost=0
my_list=['snake','water','gun']
print('''Snake-Water-Gun game!
            - Created by Shagun Singh\n''')
while i<5:

    a= random.choice(my_list) # random.choice method is used here in order to select random element from a sequence
    b= input('What do you want to become: snake,water or gun?:')
    if b=="snake" or b=="water" or b=="gun":
        pass
    else:
        print('\nI take only snake,gun and water as an input\n')
        continue
    if a==b:
        print('you won!\n')
        you_won=you_won+1
        i=i+1
    else:
        print('you lost:(\n')
        you_lost=you_lost+1
        i=i+1
        
print(f'The total number of times you won is:{you_won}\n')
print(f'The total number of times you lost is:{you_lost}\n')
