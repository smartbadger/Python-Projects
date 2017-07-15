#Connor's Health Calculator


def main():
    print "Welcome to the calories calculator"
    age = input("Please enter your age.") 
    weight = input("Next, you'll need to enter your weight in lbs.")
    hr = input("Now enter your heart rate; heart rate is the number of beats per minute.") #hr = heart rate
    time = input("Finally, enter the amount of time in mintues you exercized.")
                     #Formula for calories burned
    calories = (((age*0.2017)-(weight*0.09036)+(hr*0.6309)-55.0969)*time)/4.184
    print "The calories burned are ", calories

   

       #### START OF PROGRAM #####

print "Welcome to the Calorie Calculator!" 
pswd = raw_input("Please enter your password.  ")
if pswd == "FITBIT2015":
   main()
else:
   print "You've entered an incorrect password, Goodbye..."


