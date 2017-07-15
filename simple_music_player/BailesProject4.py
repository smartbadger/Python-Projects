#Author: Connor Bailes
#Date Created: April 1st 2017
#Purpose: shows music in a list format and shows the standard deviation

# Label example
from Tkinter import *
import math

class Node(object):

    def __init__(self, musicID, musicCategory, musicRating, next=None):
        self.musicID = musicID
        self.musicCategory = musicCategory
        self.musicRating = musicRating
        self.next = next

class GUIForMusicDB(Frame):

    def __init__(self):

        #### LIST ###
        self.first = None
        self.current = None

        #Sets up the window, GUI, and widgets
#--------------------------------------------------------------------------#        
        Frame.__init__(self)
        self.master.title("Music Database")
        self.grid()               # set layout manager to grid layout

        #ID ENTRY
        self.musicIDVar = StringVar()
        self.musicIDEntry = Entry(self,
                                 textvariable = self.musicIDVar)
        self.musicIDEntry.grid(row=0, column=1)
        self.musicIDLabel = Label(self, text = "Music ID:")
        self.musicIDLabel.grid(row=0, column=0)

        #Category Entry
        self.musicCategoryVar = StringVar()
        self.musicCategoryEntry = Entry(self,
                                   textvariable = self.musicCategoryVar)
        self.musicCategoryEntry.grid(row=1, column=1)
        self.musicCategoryLabel = Label(self, text = "Music Category:")
        self.musicCategoryLabel.grid(row=1, column=0)

        #Rating Entry
        self.musicRatingVar = StringVar()
        self.musicRatingEntry = Entry(self,
                                   textvariable = self.musicRatingVar)
        self.musicRatingEntry.grid(row=2, column=1)
        self.musicRatingLabel = Label(self, text = "Music Rating:")
        self.musicRatingLabel.grid(row=2, column=0)

        # buttons
        self.btnAddMusic = Button(self,text="Add A Music File",command=self.addMusicFile)
        self.btnAddMusic.grid(row=3,column=0)    # position the button on window's grid

        self.btnDeleteMusic = Button(self,text="Delete A Music File",command=self.deleteMusicFile)
        self.btnDeleteMusic.grid(row=3,column=1)    # position the button on window's grid

        self.btnChangeMusic = Button(self,text="Change A Music File",command=self.changeMusicFile)
        self.btnChangeMusic.grid(row=4,column=0)    # position the button on window's grid

        self.btnNextMusic = Button(self,text="Next Music File",command=self.nextMusicFile)
        self.btnNextMusic.grid(row=4,column=1)    # position the button on window's grid

        self.btnPrint = Button(self,text="?",command=self.printTheList)
        self.btnPrint.grid(row=4,column=2)    # position the button on window's grid

        self.btnStats = Button(self,text="Show Stats",command=self.showStat)
        self.btnStats.grid(row=4,column=3)    # position the button on window's grid

        #Info
        self.info = Label(self, text = "Info")
        self.info.grid(row=0, column = 2)

        self.infoCurrentID = Label(self, text = "Current: ")
        self.infoCurrentID.grid(row=1, column = 2)

        self.infoRating = Label(self, text = "Rating: ")
        self.infoRating.grid(row=2, column = 2)

        self.infoCategory = Label(self, text = "Category: ")
        self.infoCategory.grid(row=3, column = 2)



        #Stats
        self.statVar = StringVar()
        self.statVar.set("Stats")
        self.stats = Label(self, text = "Stats")
        self.stats.grid(row=0, column = 3)

        self.avg = Label(self, text = "Avg: ")
        self.avg.grid(row=1, column = 3)

        self.std = Label(self, text = "Std Dev: ")
        self.std.grid(row=2, column = 3)
#--------------------------------------------------------------------------#
#                               METHODS
#--------------------------------------------------------------------------#
    #checks if feilds are empy
	def check4Null(self, addMusic = False):
        if addMusic:
            if self.musicIDVar.get() == "" or self.musicCategoryVar.get()== "" or self.musicRatingVar.get() == "" or self.rateMusicValid() == False:
                print "Must enter valid value for all fields"
                return False
            return True 
        else:
            if self.musicIDVar.get() == "":
                print "Must enter ID"
                return False
            return True
    #is the music rate field 1-4 or invalid
    def rateMusicValid(self):
        if len(self.musicRatingVar.get()) > 1:
            return False
        if ord(self.musicRatingVar.get()) < 48 or ord(self.musicRatingVar.get()) > 52:
            return False
        else:
            return True
	# goes through tehe music files and add it to the right place
    def cycleThrough(self):
        self.current = self.first
        while self.current.musicID <= self.musicIDVar.get():
            if self.current.musicID == self.musicIDVar.get():
                print "Already in List"
                return
            else:
                if self.current.next != None:
                    self.current = self.current.next
                else:
                    self.current.next = Node(self.musicIDVar.get(), self.musicCategoryVar.get(), self.musicRatingVar.get())
                    return
     #called when the user hits the add button   
    def addMusicFile(self):
        
        if self.check4Null(True):    
            if self.first == None:       
                self.first = Node(self.musicIDVar.get(), self.musicCategoryVar.get(), self.musicRatingVar.get())
                print "empty list, first node entered"
            else:
                if self.first.musicID > self.musicIDVar.get():
                    temp = self.first
                    self.first = Node(self.musicIDVar.get(), self.musicCategoryVar.get(), self.musicRatingVar.get(), temp)
                else:
                    self.cycleThrough()
    #called wehn the use hits the delete button
    def deleteMusicFile(self):
        if self.first != None:
            self.current = self.first
            if self.check4Null():
                if self.first.musicID == self.musicIDVar.get():
                    if self.first.next == None:
                        self.first = None
                    else:
                        self.first = self.first.next
                else:
                    while self.current.musicID != self.musicIDVar.get():
                        if self.current.next == None:
                            print "FILE NOT FOUND"
                            return
                        else:
                            temp = self.current
                            self.current = self.current.next                
                    temp.next = self.current.next

    #changes the rating            
    def changeMusicFile(self):
        if self.first != None:
            self.current = self.first
            if self.check4Null(True):
                while self.current.musicID != self.musicIDVar.get():
                    if self.current.next == None:
                        print "FILE NOT FOUND"
                        return
                    else:
                        self.current = self.current.next
                    self.current.musicCategory = self.musicCategoryVar.get()
                    self.current.musicRating = self.musicRatingVar.get()
                        
                

    def showStat(self):
        rateSum = 0
        count = 0
        intArray = []
        if self.first != None:
            self.current = self.first
            while self.current != None:
                rateSum += int(self.current.musicRating)
                intArray.append(self.current.musicRating)
                count += 1     
                self.current = self.current.next
            
			
			
			#for finding mean
			print "sum: " +str(rateSum)
            avg = rateSum / count
            self.avg.config(text='AVG: '+ str(avg))
            print "avg: " +str(avg)
            rateSum = 0
            
			#for finding standard deviation
            for item in intArray:
                rateSum += math.pow(float(item)-float(avg), float(item))
            avg = rateSum/count
            print "mu: " +str(avg)
            print math.sqrt(avg)
            self.std.config(text='Std Dev: '+str(avg))   
	
	#displays next music file
    def nextMusicFile(self):
        if self.first != None:
            if self.current == None:
                self.current = self.first
            else:
                if self.current.next == None:
                    self.current = self.first
                else:
                    self.current = self.current.next

            # update info #
            self.infoCurrentID.config(text='Current: ' + self.current.musicID)
            self.infoRating.config(text='Rating: ' +self.current.musicRating)
            self.infoCategory.config(text='Category: '+self.current.musicCategory)

    def printTheList(self):
        
        current = self.first
        while current != None:
            print current.musicID
            current = current.next
        print "--------------------------------------------"
        print

def main():
    """Instantiate and pop up the window."""
    GUIForMusicDB().mainloop()

main()

