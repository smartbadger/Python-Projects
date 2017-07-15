#Connor's Health Calculator


## FUNCTIONS ##

# Main Function #

def main():
    program = True
    counter = 0
    average = 0
    total = 0
    while program == True:    
        gender = raw_input("Please choose between male (M) or female (F)")
        counter += 1
        average += 1
        if gender == "M":
            cal = male()
            total += cal
            average = total/counter
            print "The number of calculation preformed are " + str(counter)
            print "The average number of calories burned are " +str(average)
            print " The total number of calories burned are " + str(total)
            answer = raw_input("Would you like to enter another calorie calculation? Y_N" )
            if answer == "Y":
              program = True
            elif answer =="N":
              program = False
              print "Goodbye..."
            else:
              print "You've entered an incorrect key"            
        elif gender =="F":
            cal = female()
            total += cal
            average = total/counter
            print "The number of calculation preformed are " + str(counter)
            print "The average number of calories burned are " +str(average)
            print " The total number of calories burned are " + str(total)
            answer = raw_input("Would you like to enter another calorie calculation? Y_N" )
            if answer == "Y":
              program = True
            elif answer =="N":
              program = False
              print "Goodbye..."
            else:
              print "You've entered an incorrect key"            
        else:
            
         print "You've entered and invalid answer, please retry"
         program = True 


# MALE FUNCTION #

def male():  
    age = input("Please enter your age.")
    weight = input("Next, you'll need to enter your weight in lbs.")
    hr = input("Now enter your heart rate; heart rate is the number of beats per minute.") #hr = heart rate
    time = input("Finally, enter the amount of time in mintues you exercized.")
                     #Formula for calories burned
    calories = (((age*0.2017)-(weight*0.09036)+(hr*0.6309)-55.0969)*time)/4.184
    print "The calories burned are ", calories
    return calories
   
    
    

# FEMALE FUNCTION 

def female():
    age = input("Please enter your age.")
    weight=input("Next, you'll need to enter your weight in lbs.")
    hr = input("Now enter your heart rate; heart rate is the number of beats per minute.") #hr = heart rate
    time = input("Finally, enter the amount of time in minutes you exercised.")
                   #Formula for calories burned
    calories = (((age*0.074)-(weight*0.05741)+(hr*0.4472)-20.4022)*time)/4.184
    print
    print "The calories burned are ", calories
    return calories
    
 

       #### START OF PROGRAM #####

print "Welcome to the Calorie Calculator!" 
pswd = raw_input("Please enter your password.  ")
if pswd == "FITBIT2015":
   main()
else:
   print "You've entered an incorrect password, Goodbye..."


