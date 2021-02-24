print("""\nThis is a basic calculator
                - created by Shagun Singh""") 


def operator_check():  
    num1= int(input('\nenter your first num:'))
    num2= int(input('\nenter your second num:'))
    operator = input('\nenter your operator:')
    if operator in ['+','-','','*','%','/']:
        if operator=='+':
            print(f'{num1}+{num2}=',(num1+num2))
        elif operator=='-':
            print(f'{num1}-{num2}=',(num1-num2))
        elif operator=='/':
            print(f'{num1}/{num2}=',(num1/num2))
        elif operator=='%':
            print(f'{num1}%{num2}=',(num1%num2))
        elif operator=='*':
            print(f'{num1}*{num2}=',(num1*num2))
        elif operator=='**':
            print(f'{num1}*{num2}=',(num1*num2))
        again()
    else:
        print('''\n\nThis calculator doesn't perform this function.
            Enter another operand.''')
        again()

def again():
    choice=input('''\nDo you want to make more calculations?
            type 'y' for yes and 'n' for no: ''')
    if choice=='y':
        operator_check()
    else:
        print('\nbad me milenge')
operator_check()
