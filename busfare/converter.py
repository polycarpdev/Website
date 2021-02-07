                #WEEK 2 PROJECT
from math import*


#####function  prompts the user to enter his/her name and says hi to them
def greet_user(name):
    
    print("\n Hello " + name.upper() + " !")##display te name in caps
name= input("\n Please input your name: ") ##get the name as input from the user
greet_user(name)

## asks the user to choose which operation they want to perform ##

operation= input("\n Choose the operation you wanna perform (reply with number 1,2,3,4 or 5) \n 1. Percent to Letter grade \n 2. Hours to seconds \n 3. Meters to kilometers \n 4. Distance to speed \n 5. Steps ran to Calories\n \n Operation Number: ")
gradeError= 'Sorry ' + name.upper() + ', your input is Out of range!'
###### I use the IF statement to choose among the 5 operations to perform ###
if operation == "1":
    print ("\n CONVERTING PERCENT TO LETTER GRADE\n")
    percent= float(input('Enter the percentage:  '))
    if percent >=80 and percent <100 :
        grade="A"

    elif percent >=70 and percent <80 :
        grade='B'

    elif percent  >=60 and percent <70:
        grade='C'

    elif percent >= 50 and percent <60:
        grade='D'
    elif percent >= 20 and percent <40:
            grade='E'
    elif percent >= 0 and percent <20:
            grade='F'
    else:
        grade= gradeError
    print ('Your Grade: ' + grade)
    print("\n Thats all, " + name + ".")

elif operation == "2":

    print('\nCONVERTING HOURS TO MINUTES\n')

    hours = float(input('Enter time in Hours: '))
    print( str(hours) + ' hrs = ' + str(hours*60) + ' minutes')
    print("\n Thats all, " + name + ".")

elif operation == "3":
    print('\nCONVERTING METERS TO KILOMETERS\n')

    meters = float(input('Enter length in Meters: '))
    print( str(meters) + 'm = ' + str(meters/1000) + ' kms')
    print("\n Thats all, " + name + ".")

elif operation == "4":
    print('\nCONVERTING DISTANCE TO SPEED\n')

    distance = float(input('Enter distance in kilometers: '))
    time = float(input('Enter time in hrs: '))
    
    print( 'speed used = ' + str(distance/time) + ' km/h')
    print("\n Thats all, " + name.upper() + ".")

elif operation == "5":
    print('\nCONVERTING steps TO CALORIES BURNED\n')

    weight = float(input('Enter your weight in Kgs: '))
    steps = int(input('Enter the number of steps made: '))
    if weight >=60:
        print( ' Congrats! You burned ' + str(steps*25) + ' km/h')
    else:
        print( ' Congrats! You burned ' + str(steps*20) + ' km/h')
    print("\n Thats all, " + name + ".")

else: print(gradeError)
print("\n Thats all, " + name + ".")

