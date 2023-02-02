from Room import Room
from Room import Chest
from Room import Stairs
from TextUI import TextUI
from User import Inventory
from User import User
from Ministers import Guess_number
from Ministers import Roll_dice
from Ministers import BlackJack
from Ministers import Match_numbers
from Ministers import LevelUp
from Ministers import Trivia


import tkinter
import tkinter as tk
from tkinter import * 


"""
    This class is the main class of the "Adventure World" application. 
    'Adventure World' is a very simple, text based adventure game.  Users 
    can walk around some scenery. That's all. It should really be extended 
    to make it more interesting!
    
    To play this game, create an instance of this class and call the "play"
    method.

    This main class creates and initialises all the others: it creates all
    rooms, creates the parser and starts the game.  It also evaluates and
    executes the commands that the parser returns.
    
    This game is adapted from the 'World of Zuul' by Michael Kolling
    and David J. Barnes. The original was written in Java and has been
    simplified and converted to Python by Kingsley Sage
"""


class Game:                                     #Create the game object 

    def __init__(self):                         #Initialise the game object
        """
        Initialises the game
        """
        self.create_rooms()                      #Create the rooms
        self.user = User()                      #create the user object
        self.current_room = self.middle_bottom    #Set the first current room
        self.textUI = TextUI()                  #Create the textUI object
        self.Boris_office = Chest("Me Boris Johnson the PM, You dont have the votes DO YOU?", None, "Boris_Johnson", "key")
        

    def create_rooms(self):
        """
            Sets up all room assets
        :return: None
        """
        
        self.hallway = Room("The hallway connects most of the rooms within the house", None, "hallway", "nogame")            #initialise all the rooms with the description and key
        
        self.left_top = Room("This is the Home Secretary office - Priti Patel \n", 5, "Priti_Patel", "higherorlower")
        self.middle_top = Room("This is the Deputy Prime Minster - Dommic Raab \n", 6, "dominic_raab", "dice")
        self.down_stairs = Stairs("Stairs to the PMs office", None, "downstairs", "nogame")
        
        self.left_middle = Room("This is Sajid Javid the Secretary of Health \n", 4, "Sajid_Javid", "numberline")
        self.hallway = Room("The hallway connects most of the rooms within the house \n", None, "hallway", "nogame")
        self.right_middle = Room("Welcome to Riki Sunaks office the Chancellor of the Exchequer \n", 2, "Rishi_Sunak", "blackjack")
        
        self.left_bottom = Room("Welcome to Micheal Goves Office the Secretary of Leveling UP \n", 3, "Michael_Goves", "levelup")
        self.middle_bottom = Room("Welcome to Downing Street. You need to collect all the votes from the cabinate. \n You will find the Secretarys in the rooms of downing street", None, "10_Downing_Street", "nogame")
        self.right_bottom = Room("O welcome to Jacob Rees Moggs Office \n", 1, "Jacob_Rees_Mogg", "trivia")
        
        self.up_stairs = Stairs("This is the up_stairs of Downing Street \n", None, "upstairs", "nogame")
        self.up_stairs_recption = Room("Welcome to the PMs Office \n", None, "desk", "nogame")
        self.Boris_office = Chest("Me Boris Johnson the PM, You dont have the votes DO YOU?\n", None, "Boris_Johnson", "key")
        
        self.offmap = Room("You are off the Map returning to last room", None, "hallway", "nogame")
        
        self.left_top.setExit("Right (Dommic Raab)", self.middle_top)                                 #Set all the exits for each room, these display in each room
        self.left_top.setExit("DOWN (Sajid Javid)", self.left_middle)
        
        self.middle_top.setExit("RIGHT (Stairs)", self.down_stairs)
        self.middle_top.setExit("LEFT (Priti Patel)", self.left_top)
        self.middle_top.setExit("DOWN (Hallway)", self.hallway)
        
        self.down_stairs.setExit("UP (PM Ofiice up Stairs)", self.up_stairs)
        self.down_stairs.setExit("LEFT (Dommic Raab)", self.middle_top)
        self.down_stairs.setExit("DOWN (Riki Sunaks)", self.right_middle)
        
        self.left_middle.setExit("RIGHT (Hallway)", self.hallway)
        self.left_middle.setExit("UP (Priti Patel)", self.left_top)
        self.left_middle.setExit("Down (Micheal Gove)", self.left_bottom)

        self.hallway.setExit("UP (MR Raab)", self.middle_top)
        self.hallway.setExit("LEFT (MR Javid)", self.left_middle)
        self.hallway.setExit("RIGHT (MR Sunak)", self.right_middle)
        self.hallway.setExit("DOWN (Start)", self.middle_bottom)
        
        self.right_middle.setExit("UP (Staris)", self.down_stairs) #The oppsite as the room is down the stairs
        self.right_middle.setExit("LEFT (Hallway)", self.hallway)
        self.right_middle.setExit("DOWN (Jacob Rees Mogg)", self.right_bottom) 
        
        self.left_bottom.setExit("Up (Sajid Javid)", self.left_middle)
        self.left_bottom.setExit("Right (Welcome Room)", self.middle_bottom)
        
        self.middle_bottom.setExit("UP (Hallway) ", self.hallway)
        self.middle_bottom.setExit("LEFT (Micheal Gove) ", self.left_bottom)
        self.middle_bottom.setExit("RIGHT (Jacob Rees Mogg) ", self.right_bottom)
        
        self.right_bottom.setExit("UP (Riki Sunak)", self.hallway)
        self.right_bottom.setExit("LEFT (Welcome Room)", self.middle_bottom)
        
        
        self.up_stairs.setExit("DOWN (PMs Office)", self.up_stairs_recption)
        self.up_stairs.setExit("UP (to go down_stairs)", self.down_stairs)
        
        self.up_stairs_recption.setExit(" (UP) (down_stairs)", self.up_stairs)
        self.up_stairs_recption.setExit(" DOWN (Boris Office)", self.Boris_office)
        
        self.Boris_office.setExit("UP (Recption)", self.up_stairs_recption)
        
        self.left_top.add_object("DYSON") #Adding items to each Room
        self.middle_top.add_object("AIRBUS")
        self.left_middle.add_object("BLOOMBERG")
        self.left_bottom.add_object("CITYLINK")
        self.right_middle.add_object("JPMORGAN")
        self.right_bottom.add_object("LNT")
        
        
        self.lowerFloor = [[0, 1, 2],
                           [3, 4, 5],
                           [6, 7, 8]]    #Declaring the lower floor 2D list
        
        self.upperFloor =  [[0, 1, 2],
                            [3, 4, 5],
                            [6, 7, 8]]   #Declaring the lower floor 2D list
        
        self.floor = False               #Set the boolean for floor
        
        self.coordinates = [2, 1]        #The starting Coordinates
        

    def play(self):
        
        """
        Calls all the functions in the correct order to run the game.
        All the commands are accessed and parsed from functions within this section.
        Quiting the game handles are within this part of the game
        
        """
        
        print("Start Game!!")
        
        p = 0                                                                   #Set the P variable which shows how many turns the user has had
        self.printWelcome()
        print("Welcome over")
        self.correct_keys = self.Boris_office.get_correct_keys()                 #Get the keys that win the game and show the user
        print(self.correct_keys)
        self.keys = self.user.print_keys()                                      #Print the empty keys that the user has
        
        finished = False                                                        #Set the finnished to False. This variable controls if the loop is active
        while (finished == False):                                              #If the finnished is False then loop
            
            self.textUI.printtoTextUI(" ")                                      #Print a space to break up the console to make it easier to see
            p = p + 1                                                           #Add one to the turns
            self.textUI.printtoTextUI(p)                                        #print the turns
            self.current_room = self.pick_room()                                 #Call the pick room function to set the current room
            self.textUI.printtoTextUI(self.current_room.getLongDescription())    #Print the description of the room
            self.textUI.printtoTextUI(self.current_room.return_objects())        #Print all the objects in the room
            print("Keys to get", self.Boris_office.get_correct_keys())
            print("Your Keys:", self.user.print_keys())
            print("Your Donors: ", self.user.donor)
            print("Campain Health: ", self.user.health)
            print("Your Weight: ", self.user.weight)
            self.showCommandWords()                                             #Show the command words on console
            
            command = self.textUI.getCommand()                                  # Returns a 2-tuple
            
            finished, self.coordinates = self.processCommand(command)           
            if finished == True:                                                #If finnished is True
                print("You are leaving Downing Street, Thank you for playing!") #Leaving message
                
            if self.current_room == self.Boris_office:                            #If the current room is the chest
                finished = self.Boris_office.check_keys(self.user.print_keys())  #Check to see if users keys match the wanted keys
                
            if self.user.health < 1:                                            #If the users health is below 1 then end the game as there campign is over
                self.textUI.printtoTextUI("Your Campain is over")
                finished = True
            
        
    def run_room(self, secondWord):                                             #Run the run room function which is common code used by all rooms
    
        """
        Runs the sequence of code that runs the through the functions all rooms use
        Sets the coordinates using the second word of the commonds. 
        
        The coordinates are returned
        """
    
        self.coordinates_memory = self.coordinates                              #Set the memory as the coordinates (Just in case the user goes off map)
        self.coordinates = self.user.moveRoom(self.coordinates,  secondWord)    #Use the move room fucntion and parse through the coordinates and second word
        print("run room function: ", self.coordinates)                          #print new coordinates
        return self.coordinates                                                 #return the coordinates
        

    def pick_room(self):                                                        #Pick the room function
        """
        Picks the room that the user is now within to the current room. 
        
        The method returns the current room
        """
            
        self.textUI.printtoTextUI("Pick Room")
        if self.coordinates == [0, 0] and self.floor == False:                  #If the coordinates is met and the floor is the correct boolean
            self.current_room = self.left_top                                     #set the current room accordingly (These two lines are for all rooms)
        
        elif self.coordinates == [0, 1] and self.floor == False:
            self.current_room = self.middle_top
            
        elif self.coordinates == [0, 2] and self.floor == False:
            self.current_room = self.down_stairs
            
        elif self.coordinates == [1, 0] and self.floor == False:
            self.current_room = self.left_middle
        
        elif self.coordinates == [1, 1] and self.floor == False:
            self.current_room = self.hallway
            
        elif self.coordinates == [1, 2] and self.floor == False:
            self.current_room = self.right_middle
            
        elif self.coordinates == [2, 0] and self.floor == False:
            self.current_room = self.left_bottom
        
        elif self.coordinates == [2, 1] and self.floor == False:
            self.current_room = self.middle_bottom
            
        elif self.coordinates == [2, 2] and self.floor == False:
            self.current_room = self.right_bottom
            
        elif self.coordinates == [0, 2] and self.floor == True:
            self.current_room = self.up_stairs
        
        elif self.coordinates == [1, 2] and self.floor == True:
            self.current_room = self.up_stairs_recption
            
        elif self.coordinates == [2, 2] and self.floor == True:
            self.current_room = self.Boris_office
            
        else: 
            self.textUI.printtoTextUI("You cannot go here! You can only access the rooms of downing street. Click stay") #If the movement is not met then print message you cannot go here
        
        return self.current_room         #return the new current room for all functions

        
    def choose_room(self, secondWord):                                          #Choose_room functon
        """
        If the coordinates and the floor equal a space within a matrix run the
        run_room function. 
        
        The coordinates are turned from the function
        """
        
        if self.coordinates == [0, 0] and self.floor == False:                  #If conditions are met for coordinates and the floor
            self.coordinates = self.run_room(secondWord)                        #run the run room function and return the new coordinates
            
            return self.coordinates                                             #Return the new coordinates
            
            
        elif self.coordinates == [0, 1] and self.floor == False:
            self.coordinates = self.run_room(secondWord)
            
            return self.coordinates
            
        elif (self.coordinates == [0, 2] or self.coordinates == [-1, 0]) and self.floor == False:   #If the user is in the stairs coordinates
            self.coordinates_memory = self.coordinates                                              #Set to the old coordinates
            
            self.movement = secondWord                                                              #set movement to second word
            
            self.coordinates = self.user.moveRoom(self.coordinates, self.movement)                  #User move room function is called and returns the new coordinates
            if self.movement.upper() == "UP":                                                       #If movement variable is equal to UP then
                self.floor = self.down_stairs.move_up()                                              #Call the move up function in teh stairs room
            
            return self.coordinates                                                                 #return the coordinates
            
        elif self.coordinates == [1, 0] and self.floor == False:
            self.coordinates = self.run_room(secondWord)
            return self.coordinates
            
        elif self.coordinates == [1, 1] and self.floor == False:
            self.coordinates = self.run_room(secondWord)
            return self.coordinates
            
        elif self.coordinates == [1, 2] and self.floor == False:
            self.coordinates = self.run_room(secondWord)
            return self.coordinates
            
        elif self.coordinates == [2, 0] and self.floor == False:
            self.coordinates = self.run_room(secondWord)
            return self.coordinates
            
        elif self.coordinates == [2, 1] and self.floor == False:
            self.coordinates = self.run_room(secondWord)
            return self.coordinates

            
        elif self.coordinates == [2, 2] and self.floor == False:
            self.coordinates = self.run_room(secondWord)
            return self.coordinates
        
        
        elif (self.coordinates == [0, 2] or self.coordinates == [-1, 0]) and self.floor == True:    #If the user is in the stairs
            self.coordinates_memory = self.coordinates                                              #Set the memory to current
            
            self.movement = secondWord                                                              #Set movement to the secondWord
            
            self.coordinates = self.user.moveRoom(self.coordinates, self.movement)                  #set the coordinates to the move function
            if self.movement.upper() == "UP":                                                       #If up go down_stairs
                self.floor = self.up_stairs.move_down()
                
            return self.coordinates                                                                 #Return the coordintes
                
        elif self.coordinates == [1, 2] and self.floor == True:                                     #If up_stairs and at [1,2] then you are in the PMs Office
            self.coordinates = self.run_room(secondWord)                                            #Run the room function and return coordinates
            return self.coordinates
            
        elif self.coordinates == [2, 2] and self.floor == True:
            self.coordinates = self.run_room(secondWord)
            return self.coordinates

                
        else:
            print("You have gone off the map going from {} to {} ".format(self.coordinates, self.coordinates_memory)) #If the user is off the map
            self.coordinates = self.coordinates_memory                                                                  #Set the coordinates to the memory
            
            return self.coordinates
            

    def printWelcome(self):                 #Print welcome message on the console
        """
            Displays a welcome message
        :return:
        """
        
        self.textUI.printtoTextUI("You are on the doors of Downing Street")
        self.textUI.printtoTextUI("You open the door to the game")
        self.textUI.printtoTextUI("You need to collect the votes from your secerterys to become PM ")
        self.textUI.printtoTextUI(f'Your command words are: {self.showCommandWords()}')

    def showCommandWords(self):
        """
            Show a list of available commands
        :return: None
        """
        return ['Help', 'Go', 'Quit', 'Grab', 'Eat', 'Place', 'Inventory','Play'] #Return the different commands

    def processCommand(self, command):
        """
            Process a command from the TextUI
        :param command: a 2-tuple of the form (commandWord, secondWord)
        :return: True if the game has been quit, False otherwise
        """
        commandWord, secondWord = command       #split up the two words
        if commandWord != None:                 #Convert both words to upper case if they are something, this makes the statements work correctly
            commandWord = commandWord.upper()
        
        if secondWord != None:
            secondWord = secondWord.upper()

        wantToQuit = False                      #want to Quit equals False
        if commandWord == "HELP":               #If help typed in then run the print help function
            self.doPrintHelp()
        elif commandWord == "GO":                           #If the Go function is pressed then the doGoCommand is called and the coordinates are returned
            self.coordinates = self.doGoCommand(secondWord)
        elif commandWord == "QUIT":                         #If the quit is typed in then the wantToQuit is set to True
            wantToQuit = True
        elif commandWord == "GRAB":                                             #if the grab is the firstword
            
            self.textUI.printtoTextUI("What would you like to Grab")
            self.textUI.printtoTextUI(self.current_room.return_objects())        #Pirnt the objects in the current room
            #secondWord = secondWord.upper()
            self.user.pick_up_object(secondWord)                                #Call the function to pick up object and parse through the second word
            self.current_room.remove_object(secondWord)                          #remove the object from the room
            self.textUI.printtoTextUI(self.user.donor)                          #Print the updated list
            wantToQuit = False                                                  #Set the want to Quit to False
            
        elif commandWord == "USE":                                              #If the use command is called then
            #Need access the inventory (Second word can be accessed here)
            self.textUI.printtoTextUI("What would you like to use")
            #secondWord = secondWord.upper()
            self.user.donor, self.user.weight = self.user.use_donor(secondWord) #Run the use function to remove the donor and adjust the weights and donors
            wantToQuit = False
            
        elif commandWord == "PLACE":                                                                                        #If the Plcae function is called then
            self.textUI.printtoTextUI("Putting Object down")          
            self.user.donor, self.current_room, self.user.weight = self.user.put_down_object(secondWord, self.current_room)   #Put down function and return donors, current room and the weight
            
        elif commandWord == "INVENTORY":
            self.textUI.printtoTextUI("Putting Object down") #Print the keys, donors and health
            self.textUI.printtoTextUI("Keys: ")
            self.textUI.printtoTextUI(self.user.keys) 
            self.textUI.printtoTextUI("Donors: ")
            self.textUI.printtoTextUI(self.user.donor)
            self.textUI.printtoTextUI("Health: ")
            self.textUI.printtoTextUI(self.user.health)

            
        else:
            self.textUI.printtoTextUI("Don't know what you mean")   #if the command is unknown print("Unknown") and set want to quit to False
            wantToQuit = False

        return wantToQuit, self.coordinates
            
            

    def doPrintHelp(self):                                          #Do help function prints help messages
        """
            Display some useful help text
        :return: None
        """
        self.textUI.printtoTextUI("This is the help suggestion")
        self.textUI.printtoTextUI("around the deserted complex.")
        self.textUI.printtoTextUI("")
        self.textUI.printtoTextUI(f'Your command words are: {self.showCommandWords()}')

    def doGoCommand(self, secondWord):                                      #Call the function doGoCommand
        """
            Performs the GO command
        :param secondWord: the direction the player wishes to travel in
        :return: None
        """
        if secondWord == None:                                              #If the secondword is None then Print please enter a second command
            # Missing second word ...
            self.textUI.printtoTextUI("Plese enter a second command")
            return self.coordinates                                         #Return teh coordinates
        else:
            self.coordinates = self.choose_room(secondWord)                 #set the coordinats by setting the choose room function and return coordinates
            return self.coordinates
            

def main():                     #The main body of code
    game = Game()               #Create the game object
    game.play()                 #Run the game
    

if __name__ == "__main__":      #Start the program
    main()                      #Run the main body of program
    
    
