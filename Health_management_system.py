# create separate files for all the activities
# do not run this with the main program as the write function will keep overwriting the entered logs

s=open('shags.txt','w')
s.close()
g=open('gun.txt','w')
g.close()
a=open('ank.txt','w')
a.close()


s1=open('shags_diet.txt','w')
s1.close()
g1=open('gun_diet.txt','w')
g1.close()
a1=open('ank_diet.txt','w')
a1.close()



print(‘’’ Health Management System
		-  Created by Shagun Singh\n\n’’’)

def log_data():
    '''This function logs the data in already created text files'''

    # While loop below insures that the name entered are essentially of the selected clients
    while True:
        client=input('Enter your name:')
        if client=='Shagun' or client=='Gunjan' or client=='Ankur':
            break
        else:
            print("This plan is only for Shagun,Gunjan and Ankur!\n")
            continue
 
    # While loop below insures that the activities  entered is either Diet or Exercise   
    while True:
        activity=input('Enter your activity:')
        if activity=='Exercise' or activity=='Diet':
            break
        else:
            print("I consider only 'Exercise' or 'Diet' as an activity\n")
            continue
            
    def getdate():
        '''This function will capture the date and time when the log was entered'''

        my_log=[]
        import datetime
        x= datetime.datetime.now()
        date=x.strftime('%d-%b-%Y')
        time=x.strftime('%I:%M')
        my_log.append(date)
        my_log.append(time)

        return my_log
    
    time= getdate()


    # The if-else loop below will log the activities of Shagun in the shagun’s  text files 
 
    if client=='Shagun':
        if activity=='Exercise':
            shagun_exercise=open('shags.txt','a')
            login_kro=shagun_exercise.write(str(time))
            lo_pri=shagun_exercise.write(':')
            loggin_kr=shagun_exercise.write(input('What did you do?'))
            lo_pri=shagun_exercise.write('\n')
            shagun_exercise.close()
            
        else:
            
            shagun_diet=open('shags_diet.txt','a')
            login_kro=shagun_diet.write(str(time))
            lo_pri=shagun_diet.write(':')
            loggin_kr=shagun_diet.write(input('What did you eat?'))
            lo_pri=shagun_diet.write('\n')
            shagun_diet.close()
    

    # The if-else loop below will log the activities of gunjan in the gunjan’s  text files 
        
    if client=='Gunjan':
        if activity=='Exercise':
            
            gunjan_exercise=open('gun.txt','a')
            login_kro1=gunjan_exercise.write(str(time))
            lo_pri=gunjan_exercise.write(':')
            loggin_kr1=gunjan_exercise.write(input('What did you do?'))
            lo_pri=gunjan_exercise.write('\n')                                 
            gunjan_exercise.close()
            
        else:
            
            gunjan_diet=open('gun_diet.txt','a')
            login_kro1=gunjan_diet.write(str(time))
            lo_pri=gunjan_diet.write(':')
            loggin_kr1=gunjan_diet.write(input('What did you eat?'))
            lo_pri=gunjan_diet.write('\n')
            gunjan_diet.close()
            
     # The if-else loop below will log the activities of Ankur in the ankur’s  text files 
    
    if client=='Ankur':
        if activity=='Exercise':
            
            ankur_exercise=open('ank.txt','a')
            login_kro=ankur_exercise.write(str(time))
            lo_pri=ankur_exercise.write(':')
            loggin_kr=ankur_exercise.write(input('What did you do?'))
            lo_pri=ankur_exercise.write('\n') 
            ankur_exercise.close()
            
        else:
            
            ankur_diet=open('ank_diet.txt','a')
            login_kro=ankur_diet.write(str(time))
            lo_pri=ankur_diet.write(':')
            loggin_kr=ankur_diet.write(input('What did you eat?'))
            lo_pri=ankur_diet.write('\n')
            ankur_diet.close()

def retrieve_data():
    '''This function will retrieve the data logged by client'''
    client_retrieve=input('Whose file do you want to retrieve?: ')
    activity_retrieve= input('What activity do you want to retrieve?: ')
    
    
    # this if-else statement retrieves data from Shagun’s file
    if client_retrieve=='Shagun':
        if activity_retrieve=='Exercise':
            r= open('shags.txt')
            print(r.read())
        else:
            r=open('shags_diet.txt')
            print(r.read())


    # this if-else statement retrieves data from Gunjan’s file
    if client_retrieve=='Gunjan':
        if activity_retrieve=='Exercise':
            r= open('gun.txt')
            print(r.read())
        else:
            r=open('gun_diet.txt')
            print(r.read())


    # this if-else statement retrieves data from Gunjan’s file
    if client_retrieve=='Ankur':
        if activity_retrieve=='Exercise':
            r= open('ank.txt')
            print(r.read())
        else:
            r=open('ank_diet.txt')
            print(r.read())

# this part of code will ask the action a client wants to perform
action=input('Do you want retrieve data or log data?: ')

if action=='log data':
    log_data()
elif action=='retrieve data':
    retrieve_data()
else:
    print('Enter either "log data" or "retrieve data"')
