import operator

'''Exercise: My_faulty_computer
this calculator will give correct computational result for all the numbers except [45*3 = 555, 56+9=77
56/6=4]
'''

def my_faulty():
    allowed_operator = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    # ask the user for an input
    a = int(input('give me a number:'))
    b = int(input('give me another number:'))
    opp = input('What operation do you want to perform: ')
    if a == 45 and b == 3 and opp == '*':
        print(555)
    elif a == 56 and b == 9 and opp == '+':
        print(77)
    elif a == 56 and b == 6 and opp == '/':
        print(4)
    # https://docs.python.org/3/library/operator.html check the documentation on operators
    # operator.add(a,b) is the basic representation

    elif opp in ['+', '-', '*', '/']:
        result = allowed_operator[opp](a, b)
        print(result)
    else:
        print('I am not capable of performing that computation.')

while True:
    my_faulty()
    command = input('Do you want to calculate more? ')
    if command == 'Yes':
        continue
    else:
        break
