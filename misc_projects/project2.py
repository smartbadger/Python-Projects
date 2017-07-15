#Program: Play Song
#Description: it plays a song
#Author: Connor Bailes
#Date: 2/17/17
#

import pygame
import sys

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
        print "Weak"
        sys.exit()
    elif points >= 4 and points <=6:
        print "OK"
        sys.exit()
    else:
        print "Strong"
    

def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    pygame.display.set_mode((50,50)) 
    try:
        pygame.mixer.music.load(music_file)
        print "Music file %s loaded!" % music_file
    except pygame.error:
        print "File %s not found! (%s)" % (music_file, pygame.get_error())
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)
        volume = 1.00
        pause = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print "key Pressed"
                if event.key == pygame.K_u:
                    volume +=0.1
                    pygame.mixer.music.set_volume(volume)
                if event.key == pygame.K_d:
                    volume -=0.1
                    pygame.mixer.music.set_volume(volume)
                if event.key==pygame.K_SPACE:
                    if pause == False:
                        pygame.mixer.music.pause()
                        pause = True
                    else:
                        pygame.mixer.music.unpause()
                        pause = False
def checkValidity(minRange, maxRange, dataType):
    while True:
        if dataType == "File":
            while True:
                music_file = raw_input("Enter the name of the song: ")
                if ord(music_file[0]) > 64 and ord(music_file[0]) < 91:
                    if len(music_file) < 15:
                        count = 0
                        for character in music_file:
                            if ord(character) == 46:
                                count+=1
                        if count == 1:
                            if ".mp3" in music_file or ".ogg" in music_file:
                                return music_file
                            else:
                                print "Must be .mp3 or .ogg"
                        else:
                            print "Can only contain one '.'"  
                    else:
                        print "File over 14 character length"
                else:
                    print "First Letter not capitalized"
        else:
            invalid = False
            userInput = raw_input("Enter " + str(dataType) + " : ")
            for i in userInput:
                if ord(i) < 48 or ord(i) > 58:
                    print "Invalid entry! Must be integer value"
                    invalid = True
            if invalid == False:
                userInput = int(userInput)
                if userInput < minRange or userInput > maxRange:
                    invalid = True
                    print "Invalid entry! Must be in range ("+str(minRange)+"-"+str(maxRange)+")"
                else:
                    return userInput
      
#Runs the music player
def main():
    
    checkPassword(raw_input("Enter a Password: "))
    
    #set initial values and check their validity
    music_file = checkValidity(0, 0, "File")
    freq = checkValidity(20, 50000, "Frequency")
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = checkValidity(2048, 4096, "Buffer Size")

    #init mixer with values
    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.set_volume(1.00)

    #start mixer
    try:
        play_music(music_file)
        
                    
    except KeyboardInterrupt:
        # if user hits Ctrl/C then exit
        # (works only in console mode)
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        raise SystemExit

   
        
#############################################
main()
