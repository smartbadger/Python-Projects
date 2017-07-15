#Connor's Health Calculator

## FUNCTIONS ##

# Main Function #

def main():
    program = True # 1st time force start
    counter = 0 #counter used to find averages
    average = 0 #average calories (total/counter)
    total = 0
    x =0 #FILLER VARIABLE FOR STATSREPORT FUNCTION
    group1=0 #inital group values
    group2=0
    group3=0
    group4=0
    while program == True:    
        gender = raw_input("Please choose between male (M) or female (F)")
        counter += 1
        average += 1
        
        if gender == "M":           # IF MALE IS CHOSEN
            cal = male()            # cal is calories computed from the function
            total += cal            #total number of calories
            average = total/counter # average calories
            print
            print "Here are your statistics so far..."
            print
            print "The number of calculation preformed are " + str(counter)
            print "The average number of calories burned are " +str(average)
            print " The total number of calories burned are " + str(total)
            x, group1, group2, group3, group4 = statsReport(cal,group1,group2,group3,group4)# incremental statsReport function, "x" is filler variable
            print
            answer = raw_input("Would you like to enter another calorie calculation? Y_N" ) #RETRY?
            if answer == "Y":
              program = True
            elif answer =="N":
              program = False
              print "Goodbye..."
            else:
              print "You've entered an incorrect key"            
        elif gender =="F":                                #IF FEMALE IS CHOSEN
            cal = female()
            total += cal # cal is calories computed from the function
            average = total/counter
            print
            print "Here are your statistics so far..."
            print 
            print "The number of calculation preformed are " + str(counter)
            print "The average number of calories burned are " +str(average)
            print " The total number of calories burned are " + str(total)
            x, group1, group2, group3, group4 = statsReport(cal,group1,group2,group3,group4) # incremental statsReport function, "x" is filler variable
            print
            answer = raw_input("Would you like to enter another calorie calculation? Y_N" )  # RETRY?
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
#     
# Password Function

def ThePassword():
    
    counter = 0 # original value of counter set to 1 for 1st given attempt before loop 
    while counter <3:
         counter += 1
         pswd = raw_input("Please enter your password.  ") #password 
         if pswd == "FITBIT2015":
            main()
         elif pswd != "FITBIT2015":
            print "You have entered an inccorect password"
            
            
    print "Too many inccorect attemps, Goodbye..."
    quit

         
# Range of Grouping Function

def statsReport(cal,group1,group2,group3,group4,):

    if cal >=100 and cal <=249.99: # variable cal called and used to find what range it fits into
        group1+=1                  # group1 is first range variable, group2 is second, etc...    
    elif cal >=250 and cal <=319.99:
        group2+=1
    elif cal >=320 and cal <=399.99:
        group3 +=1
    else:
        group4+=1
    print
    print "Listed below are the number of people in the given categories"  # Chart for easy reading of tallied ranges
    print
    print "| CALORIES BURNED |  100-249.99  |  250-319.99  |  320-399.99  |    >400     |"
    print "|   # of PEOPLE   |      ",group1,"     |      ",group2,"     |      ",group3,"     |     ",group4,"     |"
    return (cal,group1,group2,group3,group4)


       #### START OF PROGRAM #####

print "Welcome to the Calorie Calculator!"

ThePassword()



