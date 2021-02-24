print(''' Astrologer's star pattern
        - Created by Shagun Singh\n\n''')

my_variable = '*'
my_list=[] #this list is needed to reverse the pattern

while True:# this will decide the number of rows
    n =int(input('Enter a number between 4 to 6:'))
    if n<4:
        print('You have entered a number smaller than 4\n')
        continue
    elif n>6:
        print('You have entered a number greater than 6\n')
        continue
    else:
        break

while True:
    #This loop will ensure that the boolean number entered is either 0 or 1. 
    #This was done because bool always returns true except when int(0) is passed to it
    
    my_num=int(input('\nEnter either 1 or 0: ')) #keep asking for 0 or 1 until given
    if my_num==0 or my_num==1: 
        break
    else:
        continue
        
my_bool=bool(my_num) #turns int into true or false

print("\nHere is your Astrologer's star pattern:\n")

if my_bool==True:
    for num in range(1,n+1):
        print(my_variable*num)# rows will get changed automatically as print takes an end operator whose default value is \n
        
else:
    for num in range(1,n+1):
        my_list.append(my_variable*num)# keep appending the * to empty list so that it can be reversed later
        
my_new=my_list[::-1]
for num in range(0,len(my_new)):
    print(my_new[num]) # printed the reversed list of *
