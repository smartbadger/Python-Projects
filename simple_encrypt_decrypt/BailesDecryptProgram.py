
userFile = raw_input("Enter the name of file to Decrypt: ") #User Enters File
data = open(userFile,'r')#Data read from file assigned to variable 
datalist = list(data)#Data converted to list and assigned to variable
data.close() 
data = open(userFile,'w')#File Re-opened and wiped for write
for item in datalist:
    for line in item:
        if ord(line) > 97 and ord(line) <= 122:#all lowercase
            data.write(chr(ord(line)-1))#decrypted            
        if line == 'a':#a changed to z
            data.write('z')
        if ord(line) < 97 or ord(line)>=123:#all non lowercase
            data.write(line)#write data to file 
data.close()#close file
                        



