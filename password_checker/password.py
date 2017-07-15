def checkPassword(password):
    # local variables
    points = 8
    hasChar = False
    hasCap = False
    hasLow = False
    specialChar = ['%','&','!']
    #checking for password requirements
    if len(password) < 4:
        points -= 2
        print "no len"
    for letter in password:
        if letter in specialChar:
            hasChar = True
        if ord(letter) > 64 and ord(letter) < 123:
            if letter == letter.upper():
                hasCap = True
            else:
                hasLow = True
    # deducting points if req not met
    if hasLow == False or hasCap == False:
        points -=2
    if hasChar == False:
        points -=1
    # return password value
    if points < 4:
        return "Weak"
    elif points >= 4 and points <=6:
        return "OK"
    else:
        return "Strong"
    
