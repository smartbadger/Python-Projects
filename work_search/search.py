import os
import sys

def replaceFile(nameOfFile, searchTerm, replaceTerm):
    
    currentFile = open(nameOfFile, 'r')
    temp = currentFile.read()
    temp = temp.replace(searchTerm, replaceTerm)
    currentFile = open(nameOfFile, 'w')
    currentFile.write(temp)
    currentFile.close()
    

def main():

    count = 0
    if sys.argv.count > 2:
        search = raw_input("Enter search term: ")
        replace = raw_input("Enter replacement term: ")
        for filename in os.listdir(os.getcwd()):
            replaceFile(filename, search, replace)
            count += 1
    else:
        for filename in os.listdir(os.getcwd()):
            replaceFile(filename, sys.argv[1], sys.argv[2])
            count += 1
        
    sys.stdout.write("DONE! " + str(count) + " files changed")                     
main()
