def main(): 
    userFile = raw_input("Enter the name of file to encrypt: ")#User Chooses File
    data = open(userFile,'r')#file is opened and read and data assinged to variable
    datalist = list(data)#turn data colleced into list
    data.close()#close file 
    data = open(userFile,'w')#reopen file to wipe all data 
    for eachlist in datalist:#data stored in list is then broken down
        for line in eachlist:#each item in list is then changed
            if ord(line) >= 97 and ord(line) < 122:#all lowercase letter 
                data.write(chr(ord(line)+1))#data written to file
            if line == 'z':#z changed to a
                data.write('a')
            if ord(line)<97 or ord(line)>=123: #all non lowercase letter
                data.write(line)#write them to the file!
                
    data.close()#close file
                        
main()#run main


