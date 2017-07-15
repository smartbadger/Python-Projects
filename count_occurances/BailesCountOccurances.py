def main():
    userfile = raw_input("Enter Name of File: ")# user inputs the name of the file to have occurances counted
    openedfile =  open(userfile, 'r')#user file is opened and values assigned to a variable
    data = openedfile.read()#data read is assigned to a variable
    ifcount=0#number of ifs counted
    whilecount=0#number of whiles counted
    comparecount=0#number of == counted 
    elsecount=0#number of else's counted
    lines = data.count('\n')#total number of breaks in program counted
    for line in data.split():#break data apart and alnalyze each line
    #conditions
        if line == "if": #look for "if"
            ifcount+=1#if counter
        if line == "==":#look for "=="
            comparecount+=1#compare counter
        if line == "while":#look for "while"
            whilecount+=1# while counter
            #else counter
        if line == "else":#look for "else"
            elsecount+=1

    percent = (float(ifcount)/float(lines))*100 #values changed to float so it will calculate
    #Number of Occurances
    print "The total number of 'if' occuring: ",ifcount 
    print "The total number of '==' occuring: ",comparecount
    print "The total number of 'while' occuring: ",whilecount
    print "The total number of 'else' occuring: ",elsecount        
        
    print "Percent of if's in the file: ", percent,"%"

    print "Total number of lines in the file: ", lines
main()
