# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 18:33:05 2021

@author: 253364
"""

import tkinter
import tkinter as tk
from tkinter import * 
from PIL import ImageTk, Image
import os
import random

from Room import Room
from Room import Chest
from User import Inventory
from User import User
from Game import Game
from user_log import User_log

from Ministers import Guess_number
from Ministers import Roll_dice
from Ministers import BlackJack
from Ministers import Match_numbers
from Ministers import LevelUp
from Ministers import Trivia
from Ministers import Place_holder
from Ministers import Key_compare


class App(tk.Frame):
    """
    The App is built to create the main GUI made of 6 frames which have the widgets that allows the user to intract with the game.
    The objects of the game are created to allow the game to functions to be used. The game can run the back ground. The userlog can also be accessed. 
    The app is the central part of the program and runs all the objects within.
    
    Attributes:
        user_log (user_log object) : the object that stores all the log data
        win (tkinter object) : Create the window for the maun GUI
        game (game object) : To create the game object and allow all variables within
        user (User object) : To create the user so all functions can be accessed but mostly used within the game
        Boris_offcie (Chest room) : The chest room which is the final outcome of the game
        current_room (Room object) : the current room is teh room the user is within
        myApp (Mini game object) : the mini game that is current within the game
        frame_img (tkinter object) : the frame which stores the image
        frame_user (tkinter object) : the frame stores the users GUI lables
        frame_title (tkinter object) : the title label is stored within 
        frame_room (tkinter object) : stores all the room information
        frame_game (tkinter object) : The frame with the button of the game
        frame_movement (tkinter object) : the frame with the movement buttons
        image (tkinter object) : the image
        resized_image : (tkinter object) : the resized image
        new_image : (tkinter object) : the adjusted image
        label_image : (tkinter object) : the label that shows the image
        parsing_info : (list) stores information on inputs
        up_button : (tkinter object) : the upwards button for movement
        down_button (tkinter object) : the downwards button for movement
        right_button (tkinter object) : the right button for movement
        left_buton (tkinte object) : the left buttoton for the movement
        label_user_key (tkinte object) : the label showing the keys
        label_user_donor (tkinter object) : the label showing the donors the user has 
        label_user_health (tkinter object) : shows the health of the user
        label_user_weight (tkinter object) : shows the weight of the user
        label_room_info (tkinter object) : show sthe room information
        label_room_keys (tkinter object) : shows the room keys
        label_room_description (tkinter object) : the label taht shows the rooms description
        entry (tkinter object) : The user can input text
        button_image (tkinter object) : the button with the image 
        
    """   
    
    def __init__(self, win):
        super().__init__(master=win)                                            #Inherit the win from the main function
        self.pack(fill=tk.BOTH, expand = 1)                                     #Declare the start of the frame
        
        self.user_log = User_log()                                              #create the user log object
        self.win = win                                                          #Set the attribute
        self.game = Game()                                                      #set the game object
        self.game.create_rooms()                                                #create the game rooms in the game and set to attribute
        
        self.user = User()                                                      #Setup the user object within the App
        self.Boris_office = self.game.Boris_office                              #getup the chest room within the game and as a attribute
        self.current_room = self.game.current_room                              #set the current room to the currentroom within the game
        self.myApp = Place_holder(win, self.game.user.health)                   #Create the mini game placeholder as myApp
        
        menubar = tk.Menu(master=win)                                           #Creating the menu bar
        menubar.add_command(label="Quit", command=self.close_game)
        menubar.add_command(label="Help", command=self.help_pop_up)
        self.master.config(menu=menubar)                                        #Add the menu bar to the GUI

        self.frame_img = tk.Frame(self, width=300, height=300,  borderwidth=2)  #setting up all six frames
        self.frame_img.pack_propagate(0)
        
        self.frame_user = tk.Frame(self, width=300, height=300,  borderwidth=2)
        self.frame_user.pack_propagate(0)
        
        self.frame_title = tk.Frame(self, width=300, height=300,  borderwidth=2)
        self.frame_title.pack_propagate(0)
        
        self.frame_room = tk.Frame(self, width=300, height=300, borderwidth=2)
        self.frame_room.pack_propagate(0)
        
        self.frame_game = tk.Frame(self, width=300, height=300, borderwidth=2)
        self.frame_game.pack_propagate(0)
        
        self.frame_movement = tk.Frame(self, width=300, height=300, borderwidth=2)
        self.frame_movement.pack_propagate(0)
        
        self.frame_img.grid(row=0, column=0)                                    #Putting all 6 frames in the correct place
        self.frame_user.grid(row=1, column=0)
        self.frame_title.grid(row=0, column=1)
        self.frame_room.grid(row=1, column=1)
        self.frame_game.grid(row=0, column=2)
        self.frame_movement.grid(row=1, column=2)

        self.image = Image.open("images\\10_Downing_Street.jpg")
        self.resized_image = self.image.resize((300, 200), Image.ANTIALIAS)     #Resize the image and put in the label_image within the image frame
        self.new_image = ImageTk.PhotoImage(self.resized_image)
        self.label_image = Label(self.frame_img, image=self.new_image)
        
        
        
        self.parsing_info = ["Start"]
        
        self.up_button = tk.Button(self.frame_movement, text = "UP", width=15, height=6,
                                borderwidth=2, relief="groove", command= self.up_button_func)       #Declare all the movement Buttons
        
        self.down_button = tk.Button(self.frame_movement, text = "DOWN", width=15, height=6,
                                borderwidth=2, relief="groove", command= self.down_button_func)
        
        self.right_button = tk.Button(self.frame_movement, text = "RIGHT", width=15, height=6,
                                borderwidth=2, relief="groove", command= self.right_button_func)
        
        self.left_button = tk.Button(self.frame_movement, text = "LEFT", width=15, height=6,
                                borderwidth=2, relief="groove", command= self.left_button_func)
        
        
        self.label_user_keys = tk.Label(self.frame_user, text = "User keys: {}".format(self.game.user.keys), width = 60, height = 2, borderwidth = 2, relief = "groove")        #Declare all labels for user and room on GUI
        
        self.label_user_donors = tk.Label(self.frame_user, text = "User donors: {}".format(self.game.user.donor), width = 60, height = 3, borderwidth = 2, relief = "groove")
        
        self.label_user_health = tk.Label(self.frame_user, text = "Health: {}".format(self.game.user.health), width = 60, height = 2, borderwidth = 2, relief = "groove")
        
        self.label_user_weight = tk.Label(self.frame_user, text = "Weight: {}".format(self.game.user.weight), width = 60, height = 2, borderwidth = 2, relief = "groove")
        
        self.label_user_info = tk.Label(self.frame_user, text = "User Informaton", width = 60, height = 2, borderwidth = 2, relief = "groove")
        
        self.label_room_info = tk.Label(self.frame_room, text = "Room Informaton", width = 60, height = 2, borderwidth = 2, relief = "groove")
        
        self.label_room_keys = tk.Label(self.frame_room, text = "Keys to get: {}".format(self.Boris_office.get_correct_keys()), width = 60, height = 2, borderwidth = 2, relief = "groove")
        
        self.label_room_description = tk.Label(self.frame_room, text = "{}".format(self.game.current_room.description), width = 60, height = 3, borderwidth = 2, relief = "groove")
        
        self.label_room_objects = tk.Label(self.frame_room, text = "{}".format(self.current_room.objects), width = 60, height = 2, borderwidth = 2, relief = "groove")
        
        self.label_room_placehold = tk.Label(self.frame_room, text = " ", width = 60, height = 2, borderwidth = 2, relief = "groove")
        
        self.entry = tk.Entry(self.frame_room, width = 80)
        
        self.button = tk.Button(self.frame_movement, text = "Confirm", width=15, height=6,
                                borderwidth=2, relief="groove", command= self.inputs_to_command)            #Initalise the button
        
        self.label_title = tk.Label(self.frame_title, text = "Keys to Downing Street", font=("Arial", 30))  #Initalise the Title
        
        self.button_image = Image.open("images\\nogame.jpg")
        self.button_resized_image = self.button_image.resize((300, 300), Image.ANTIALIAS)
        self.new_button_image = ImageTk.PhotoImage(self.button_resized_image)               #Initialise the image_button for mini games
        
        self.button_game = tk.Button(self.frame_game , text = "Confirm", image = self.new_button_image, command = self.play_button_func)
        
        self.label_image.grid(row=1, column=1)          #Put all labels onto the GUI
        self.label_user_info.grid(row=2, column=1)
        self.label_user_keys.grid(row=3, column=1)
        self.label_user_donors.grid(row=4, column =1)
        self.label_user_health.grid(row=5, column=1)
        self.label_user_weight.grid(row=6, column=1)
        
        self.label_title.grid(row=1, column=1)
        self.label_room_info.grid(row = 2, column = 1)
        self.label_room_keys.grid(row=3, column=1)
        self.label_room_description.grid(row=4, column=1)
        self.label_room_objects.grid(row=5, column=1)
        self.label_room_placehold.grid(row=6, column=1)
        
        self.entry.pack(side="bottom")                  #Add entry to the GUI
        
        self.button_game.pack()                         #Add all the buttons to the GUI
        self.up_button.grid(row = 1, column=2)
        self.left_button.grid(row = 2, column=1)
        self.button.grid(row=2, column=2)
        self.right_button.grid(row = 2, column = 3)
        self.down_button.grid(row = 3, column = 2)
        
        
    def close_game(self):
        """
        Closes the game down and adds the all the logs to the .txt file

        Returns
        -------
        None.

        """
        self.user_log.final_log() #When the game closes down run final log and close all windows
        self.master.destroy()
        
    def help_pop_up(self):              #Not working propperly
        pop = tk.Toplevel(self.win)             
        pop.title("HELP")               #Create the health pop up
        pop.geometry("800x150")
        pop_label = tk.Label(pop, text="""   \n       To move room please click the arrows and then
                                             click confirm. Possible functions are GO (Right, Left, Up, Down)
                                             Quit to leave the game. 
                                             Grab object
                                             use to use object to increase health.
                                             Place to put down an object from inventory
                                             play to play mini game in room""")
                             
        pop_label.pack()                #add the label
        
    def mini_game_info(self):
        """
        Getting all the information from the min game. This includes the key state and the health

        Returns
        -------
        None.

        """
        mini_health = self.myApp.get_health() #Check the health and key from the current mini game
        mini_key = self.myApp.get_key()
        
        
        if mini_key not in self.game.user.keys:     #If the key has already been added then
            self.game.user.add_key(mini_key)        #Add key and health
            
            
        self.display_user()                         #Update the GUI
        
    def up_button_func(self):
        """
        Adds go up to the parse list and then refreshes the key states and the health

        Returns
        -------
        None.

        """
        print("UP")                                 #Add the GO UP to the info list that the confirm button checks before the next move
        self.parsing_info.append("GO UP")
        self.mini_game_info()
    
    def down_button_func(self):
        """
        Adds go down to the parse list and then refreshes the key states and the health

        Returns
        -------
        None.

        """
        print("DOWN")                               #Add the GO DOWN to the info list that the confirm button checks before the next move
        self.parsing_info.append("GO DOWN")
        self.mini_game_info()
        
        
    def right_button_func(self):
        """
        Adds go right to the parse list and then refreshes the key states and the health

        Returns
        -------
        None.

        """
        print("RIGHT")                              #Add the GO RIGHT to the info list that the confirm button checks before the next move
        self.parsing_info.append("GO RIGHT")
        self.mini_game_info()
        
        
    def left_button_func(self):
        """
        Adds go left to the parse list and then refreshes the key states and the health

        Returns
        -------
        None.

        """
        print("LEFT")                               #Add the GO LEFT to the info list that the confirm button checks before the next move
        self.parsing_info.append("GO LEFT")
        self.mini_game_info()
        
        
    def play_button_func(self):
        """
        If the play button is pressed the game looks at what the current room and what game can be played. 
        
        Then runs the mini game. This means teh mini game pops up on the window for the user to play 

        Returns
        -------
        None.

        """
        print("Play")
        
        self.entry.delete(0, "end")                         #clear the entry
        self.entry.insert(0, "play")                        #insert the play
        
        
        if self.game.current_room == self.game.left_top:    #If the current room is the top left
            
            win = Tk()                                      #create the window and set the size
            win.title("Guess the Number")
            win.geometry("300x300")
            win.resizable(False, False)
            
            self.myApp = Guess_number(win, self.game.user.health) #Run the Mini game Guess the number
            
            #win.mainloop()
            
            self.mini_game_info()                           #Refersh the information

        
        if self.game.current_room == self.game.left_middle:
            
            win = Tk()
            win.title("Match Numbers")
            win.geometry("500x500")
            win.resizable(False, False)
            
            self.myApp = Match_numbers(win, self.game.user.health)
            
            self.mini_game_info()
            
        if self.game.current_room == self.game.left_bottom:
            win = Tk()
            win.title("Leveling Up")
            win.geometry("300x300")
            win.resizable(False, False)
            
            self.myApp = LevelUp(win, self.game.user.health)
            
            self.mini_game_info()
        
        if self.game.current_room == self.game.middle_top:
            win = Tk()
            win.title("Roll the Dice")
            win.geometry("300x300")
            win.resizable(False, False)
            
            self.myApp = Roll_dice(win, self.game.user.health)
            
            self.mini_game_info()
           
        if self.game.current_room == self.game.right_middle:
            
            win = Tk()
            win.title("Black Jack")
            win.geometry("600x200")
            win.resizable(False, False)
            
            self.myApp = BlackJack(win, self.game.user.health)
            
            self.mini_game_info()
            
        if self.game.current_room == self.game.right_bottom:
            win = Tk()
            win.title("Trivia")
            win.geometry("500x600")
            win.resizable(False, False)
            
            self.myApp = Trivia(win, self.game.user.health)
            
            self.mini_game_info()
        
        if self.game.current_room == self.game.Boris_office:
            win = Tk()
            win.title("Boris Office")
            win.geometry("500x500")
            win.resizable(False, False)
            
            correct_keys = self.Boris_office.get_correct_keys()
            print("KEY COMPARE: {} : {}".format(correct_keys, self.game.user.keys))
            
            self.myApp = Key_compare(win, self.game.user.health, self.Boris_office.get_correct_keys(), self.game.user.keys)
            
            self.mini_game_info()
            
            
        
        text = self.entry.get()             #text equals the text within the entry
        self.entry.delete(0, len(text))     #Delete the text in the entry
    
    def inputs_to_command(self):
        """
        Gets the inputs and converts them into the two command words within the game

        Returns
        -------
        commandWord : TYPE
            DESCRIPTION.
        secondWord : TYPE
            DESCRIPTION.

        """
        print("Parsing Information through")
        text = self.entry.get()                 #Get the entry text
        self.entry.delete(0, len(text))         #Delete the text in the entry
        self.mini_game_info()                   #Refresh the mini game information on the GUI
        
        if len(text) > 1:                       #If text length is greater then 1
            self.parsing_info.append(text)      #Add the text information to the list
        else:
            pass
        
        print(self.parsing_info[-1])
        
        commandWord, secondWord = self.getCommandString()   #get the command words from the get_command
        
        command = (commandWord, secondWord)                 #Make tuple command
        
        finished, self.coordinates = self.game.processCommand(command)      #find the coordinates
        if finished == True:                                                #If finnished is True
            print("You are leaving Downing Street, Thank you for playing!") #Leaving message
                
        if self.current_room == self.Boris_office:                            #If the current room is the chest
            finished = self.Boris_office.check_keys(self.user.print_keys())  #Check to see if users keys match the wanted keys
                
        if self.user.health < 1:                                            #If the users health is below 1 then end the game as there campign is over
            self.textUI.printtoTextUI("Your Campain is over")
            finished = True
        
        self.display_user()
        
        self.display_current_room()
        
        return (commandWord, secondWord)
    
    def display_user(self):
        """
        Displays the users values on the GUI. This includes refreshing 

        Returns
        -------
        None.

        """
        print("Update the users paramters on screen") #Diplay the users values
        
        self.label_user_keys.config(text = "User Keys: {}".format(self.game.user.keys))
        
        self.label_user_donors.config(text = "User donors: {}".format(self.game.user.donor))
        
        self.label_user_health.config(text = "Health: {}".format(self.game.user.health))
        
        self.label_user_weight.config(text = "Weight: {}".format(self.game.user.weight))
        
    def display_current_room(self):
        """
        Get all the information from the current room. Then search the directory can be searched through until the image matches
        If the image matches then that image is resized and shown  on the GUI.

        Returns
        -------
        None.

        """
        print("Update the Current Room") #Update the room values every time the room changes
        
        self.current_room = self.game.pick_room()
        
        self.label_room_description.config(text = "{}".format(self.current_room.getLongDescription()))
        self.label_room_objects.config(text = "{}".format(self.current_room.objects))
        
        self.current_room.politician
        
        
        for i in os.listdir("images\\"):                                #Loop through all the images within the image folder
            if i[:-4].lower() == self.current_room.politician.lower():  #If the name of the file match the politican 
                self.image = Image.open("images\\{}".format(i))
                self.resized_image = self.image.resize((300, 300), Image.ANTIALIAS)  #Resize the image
                self.new_image = ImageTk.PhotoImage(self.resized_image)
                self.label_image.config(image=self.new_image)                        #Update the image of politician
            
            if i[:-4].lower() == self.current_room.game.lower():                     #If the game file name is the same as the current_room game                     
                self.button_image = Image.open("images\\{}".format(i))
                self.button_resized_image = self.button_image.resize((300, 300), Image.ANTIALIAS)   #resize the image
                self.new_button_image = ImageTk.PhotoImage(self.button_resized_image)               #set as button
                self.button_game.config(image=self.new_button_image)                                #Button game update to new image
    

    def getCommandString(self):
        """
            Fetches a command (borrowed from old TextUI)
        :return: a 2-tuple of the form (commandWord, secondWord)
        """
        inputLine = self.parsing_info[-1]                   #The most recent information
        self.user_log.log_input(self.parsing_info[-1])      #add the input to the logs 
        self.user_log.log_health(self.game.user.health)
        word1 = None
        word2 = None
        if inputLine != "":                 #if there is an input
            allWords = inputLine.split()    #spilt the words up
            word1 = allWords[0]             #word1 is the first word
            if len(allWords) > 1:           #if there are more then 1 word then add a second
                word2 = allWords[1]
            else:
                word2 = None
            # Just ignore any other words
        return (word1, word2)               #return the two words in a tuple
    
        
    def main():
        
        win = tk.Tk()                       #Setup the window to a size of 1200 by 600 pixels
        win.title('Keys to Downing Street')
        win.geometry("1200x600")
        win.resizable(False, False)
        
        
        myApp = App(win)
        
        win.mainloop()
        
        
if __name__ == "__main__":      #Start the program
    App.main()                      #Run the main body of program
    
    
