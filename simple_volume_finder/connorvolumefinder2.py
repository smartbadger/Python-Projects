#Connor's volume finder
answer = "Yes"
condition = True
while condition:
  if answer == "Yes":
    print "Welcome to the volume finder, this program will find the volume of the given dimensions"
    length = input("Please enter the length: ")
    width = input("Please enter the width: ")
    height = input("Please enterthe height: ")
    # Formula for volume
    volume = length * width * height
    print "The volume of the given area is ", volume, "cubic units."
    answer = raw_input("Would you like to find another volume? Y_N: ")
  elif answer == "No":
    condition = False
  

