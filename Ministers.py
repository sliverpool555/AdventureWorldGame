# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 12:12:06 2021

@author: Samuel Gandy
"""

import tkinter
import tkinter as tk
from tkinter import * 
from PIL import ImageTk, Image
import random


"""
The ministers class is made of methods which are mini-games for the user to play within the rooms.

"""


class Guess_number(tk.Frame):
    """
    Guess_number class is built to create the mini-game Guess the number with a GUI built in so the user can intract easily
    
    Attributes:
        frame (tkinter object) : The frame for appilcation
        frame_enrty (tkinter object) : The frame for the entry
        frame _buttton (tkinter object): the frame for the button
        label_title (tkinter object): the label for the title
        label_info (tkinter object) : the label to show information
        button (tkinter object) : the button within the GUI
        entry (tkinter object) : the entry for the infomration input
        health (int) : the health of the player
        count (int) : couting the loops
        key (int) : the users can get this key when the the game is completed
    """
    def __init__(self, win, health):
        super().__init__(master=win)
        self.pack(fill=tk.BOTH, expand = 1)                                             # Create the GUI frame
        
        self.frame = Frame(win, width=500, height=100,  borderwidth=2)                  # create frame
        self.frame.pack_propagate(0)                                                    # Put to frame on window
        self.frame.pack()
        
        self.frame_entry = Frame(win, width=500, height=50,  borderwidth=2)             # create the entry
        self.frame_entry.pack_propagate(0)
        self.frame_entry.pack()
        
        self.frame_button = Frame(win, width=500, height=50,  borderwidth=2)            #create the button
        self.frame_button.pack_propagate(0)
        self.frame_button.pack()
        
        self.label_title = Label(self.frame, text="Guess the whole number number")      # create title label
        self.label_title.pack()
        
        self.label_info = Label(self.frame, text = "Please Select a number")            # create info label
        self.label_info.pack()
        
        self.button = Button(self.frame_button, text = "Enter", width=10, height=5,
                                        borderwidth=2, relief="groove", command = self.process_number) # create the button
        self.button.pack()
        
        self.entry = Entry(self.frame_entry, width = 20) # Entry 
        self.entry.pack()
        
        self.health = health                             #initialse the health, count, memory, target
        
        self.count = 0
        
        self.memory = []
        
        self.target = random.randrange(0, 100)  
        
        self.key = 0
   
    def process_number(self):
        """
        Process number checks the input from the entry. 
        If the input is higher it says too high and if too low the program says on the label.
        If he correct number then says and gives the key
        

        Returns
        -------
        None.

        """
        self.count = self.count + 1                                             # add one to count 
        
        if self.count <= 10:                                                    # if the count is below 10
            try:
                text = self.entry.get()                                         # text equals the entry information
                num = int(text)                                                 # set number equal 
                self.entry.delete(0, len(text))                                 # delete the data in the entry
                
                if num == self.target:                                          #if the num equals the target
                    print("Congrats you get the key")
                    self.label_info.config(text="Congrats you win key 1")       # add the key
                    self.key = 1
                
                else:
                    if num in self.memory:                                                      # if the number is in middle
                        self.label_info.config(text="You entered {} before".format(num))
                    
                    else:
                        if num > self.target:                                           # If the number is greater then target print too high
                            self.label_info.config(text="{} is too HIGH".format(num))   
                        if num < self.target:                                           # if the number is lower then target print too low
                            self.label_info.config(text="{} is too LOW".format(num))
            except ValueError:
                self.label_info.config(text="Please enter a whole number")  #if there is an error then update to handle
            
        
        else:
            print("You lost the game")
            self.key = 0
        
    def get_key(self):
        return self.key     #update the key 
    
    def get_health(self):
        return self.health  #allow access to the health from the game 
    
    
    def main(health):
        """
        The main runs through the program and is called from the main program

        Parameters
        ----------
        health : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        win = Tk()          #create the window
        win.title("Guess the Number")
        win.geometry("300x300")
        win.resizable(False, False)
        
        myApp = Guess_number(win, health) #create the app
        
        win.mainloop()
        

      

class Roll_dice(tk.Frame):
    
    """
    Roll the dice is built around the user and AI taking it turns to roll the dice and who gets more wins that round.
    If you win three rounds then you win.
    
    Attributes:
        frame (tkinter object) : The frame for appilcation
        frame_enrty (tkinter object) : The frame for the entry
        frame _buttton (tkinter object): the frame for the button
        label_title (tkinter object): the label for the title
        label_info (tkinter object) : the label to show information
        label_AI (tkinter object) : the label that shows the AI dice roll
        button (tkinter object) : the button within the GUI
        entry (tkinter object) : the entry for the infomration input
        health (int) : the health of the player
        count (int) : couting the loops
        key (int) : the users can get this key when the the game is completed
        user_roll (list) : the rolls are stored within the list
        AI_roll (list) : the AIs rolls are stored within a list
    """
    
    def __init__(self, win, health):
        super().__init__(master=win)                # inherit the window
        self.pack(fill=tk.BOTH, expand = 1)         # pack the window
        
        self.frame = Frame(win, width=500, height=200,  borderwidth=2)          #create the frame, buttons, labels and then pack them in
        self.frame.pack_propagate(0)
        self.frame.pack()
        
        self.frame_button = Frame(win, width=500, height=200,  borderwidth=2)   
        self.frame_button.pack_propagate(0)
        self.frame_button.pack()
        
        self.label_title = Label(self.frame, text="Roll the Dice")              
        self.label_title.pack()
        
        self.label_info = Label(self.frame, text = "Click the button to roll the dice")
        self.label_info.pack()
        
        self.button_roll = Button(self.frame_button, text = "ROLL", width=10, height=5,
                                        borderwidth=2, relief="groove", command = self.process_roll)
        
        self.button_roll.pack()
        
        self.label_user = Label(self.frame, text = "User rolls:")               # Label user
        
        self.label_AI = Label(self.frame, text = "AI rolls:")
        
        self.label_user.pack()
        self.label_AI.pack()
        
        
        self.health = health    # declare variables
        
        self.count = 0          
        
        self.memory = []        
        
        self.key = 0            
        
        self.user_roll = []
        self.AI_roll = []
        
        self.count = [0]
   
    def process_roll(self):
        """
        The process roll function rolls the dice for both the AI and the user. Then accesses which one is higher through summing the totals.
        After the totals have been accessed the program addds the key is three rounds have been won or reduces the health of the player. 
        Throughout this function the labels are updated using the config.
        Returns
        -------
        None.

        """
        for c in range(0, len(self.count), 1):                                  # loop through the amount of times 
            self.user_roll.append(random.randrange(1, 6))                       #add a random to the users list and add to othe label
            self.label_user.config(text="User roll: {}".format(self.user_roll))
            
            self.AI_roll.append(random.randrange(1, 6))                         #generate a random number and  add to label
            self.label_AI.config(text="AI Roll: {}".format(self.AI_roll))
        
        self.user_roll_sum = sum(self.user_roll[(len(self.user_roll) - len(self.count)) : len(self.user_roll)]) #sum up the newest rolls
        print(self.user_roll_sum)
        
        self.AI_roll_sum = sum(self.AI_roll[(len(self.AI_roll) - len(self.count)) : len(self.AI_roll)])
        print(self.AI_roll_sum)
        
        if self.user_roll_sum > self.AI_roll_sum: #if the user gets higher then the AI roll
            self.count.append(0)
        else:
            self.health = self.health - 2                       #reduce the health by 5
            self.user_roll = self.user_roll[:-len(self.count)]  #user remove the newest rolls efor the user and the aAI
            self.AI_roll = self.AI_roll[: -len(self.count)]
        
        if len(self.count) == 4:                                    #If the forth roll is reached
            self.label_info.config(text="You win and get the key")  #print on GUI you win and reset the rolls
            self.user_roll = []
            self.AI_roll = []
            self.count = []
            
            self.key = 2    #set teh key to 2
    
    def get_key(self):
        return self.key
    
    def get_health(self):
        return self.health
    
    def main(health):
        win = Tk()                      #create the window 300 by 300
        win.title("Roll the Dice")
        win.geometry("300x300")
        win.resizable(False, False)
        
        myApp = Roll_dice(win, health) #create the roll dice mini-game object
        
        win.mainloop()      #run the loop
        
        
        
class BlackJack(tk.Frame):
    """
    Black Jack is a card game. The aim of the game is to get closest to 21 but cannot be above. The user gets two cards at the start
    then can stick (stay with these cards) or twist (Add another card). Each card has a set value betwene 1 to 11. The user goes againist the 
    AI. The AI can twist under a threshold.
    
    Attributes:
        frame (tkinter object) : The frame for appilcation
        frame_enrty (tkinter object) : The frame for the entry
        frame _buttton (tkinter object): the frame for the button
        label_title (tkinter object): the label for the title
        label_info (tkinter object) : the label to show information
        label_AI (tkinter object) : the label that shows the AI dice roll
        button (tkinter object) : the button within the GUI
        entry (tkinter object) : the entry for the infomration input
        health (int) : the health of the player
        count (int) : couting the loops
        key (int) : the users can get this key when the the game is completed
        deck (dict) : the deck stores all the cards and allows the random function to randomise the order
        dealer (list) : the dealer list is there to store the cards of the dealer
        user (list): the user list stores all the cards by the user
    """
    def __init__(self, win, health):
        super().__init__(master=win)
        self.pack(fill=tk.BOTH, expand = 1)                                         #create the frames, label, buttons and entry
        
        self.frame = Frame(win, width=500, height=100,  borderwidth=2)
        self.frame.pack_propagate(0)
        self.frame.pack()
        
        self.frame_button = Frame(win, width=500, height=100,  borderwidth=2)
        self.frame_button.pack_propagate(0)
        self.frame_button.pack()
        
        self.label_title = Label(self.frame, text="Black Jack")
        self.label_title.pack()
        
        self.label_cards = Label(self.frame, text="Cards shown here")
        self.label_cards.pack()
        
        self.label_AI_cards = Label(self.frame, text="AI Cards Hidden")
        self.label_AI_cards.pack()
        
        self.button_twist = Button(self.frame_button, text = "Twist", width=10, height=5,
                                        borderwidth=2, relief="groove", command = self.twist) # create the function and when pressed run the twist function
        
        self.button_stick = Button(self.frame_button, text = "Stick", width=10, height=5,
                                        borderwidth=2, relief="groove", command = self.stick) # create the function and when pressed run the stick function
        
        self.button_twist.grid(row=1, column=1)
        
        self.button_stick.grid(row=1, column=3)
        
        self.health = health
        
        self.key = 0
        
        clubs = [(i, "clubs") for i in range(1,14)]                 #A list comprehension to create 14 numbers 0 to 14
        spades = [(i, "spades") for i in range(1,14)]
        diamonds = [(i, "diamonds") for i in range(1,14)]
        hearts = [(i, "hearts") for i in range(1,14)]
    
        for c in range(11,13):                                      #loop through 10 to 13 to change the
            clubs[c] = (10, "clubs")                                #Change the elements to (10, and the club)
            spades[c] = (10, "spades")
            diamonds[c] = (10, "diamoids")
            hearts[c] = (10, "hearts")
        
        
        self.deck = clubs + spades + diamonds + hearts                   #Add all the clubs into one array
        
        random.shuffle(self.deck)
        
        self.dealer = [self.deck[0], self.deck[2]]                            #dealer equals the first and thrid in the deck
        self.user = [self.deck[1], self.deck[3]]    
        
        self.show_cards()
        
    def show_cards(self):
        self.label_cards.config(text="Your cards: {}".format(self.user)) #show the users cards
    
    
    def stick(self):
        """
        If the stick button is pressed then the users and AI cards are compared. 
        This happens when both card totals are added up. These total amounts are compared with each other.
        if the user gets more value but lower then 21 then the user wins. 
        if teh AI gets more then the user and is below 21 then the AI wins

        Returns
        -------
        None.

        """
        self.label_cards.config(text="Your cards: {}".format(self.user))    #update the cards on label
        self.label_AI_cards.config(text="AI cards: {}".format(self.dealer))
        
        self.user_total = sum([i for i, j in self.user])    #loop through all the cards and sum them up
        self.dealer_total = sum(i for i, j in self.dealer)
        
        if self.dealer_total < 14:                                                  #if the dealer gets less then 14 twist again
            self.dealer.append(self.deck[int(len(self.dealer) + len(self.user))])   #add the next card on the deck
            self.dealer_total = sum(i for i, j in self.dealer)
        
        if self.user_total > 21:
            self.label_cards.config(text="You lose you had greater then 21 with: {}".format(self.user)) #update both labels to the winner and loser
            self.label_AI_cards.config(text="Winner with: {}".format(self.dealer))          
            
        if self.user_total <= int(21):                                              #if the user total is less then or equal to  21
            if self.user_total > self.dealer_total and self.dealer_total < 22:      #if user total is greater then the dealer
                self.label_cards.config(text="Winner with: {}".format(self.user))   #user wins
                random.shuffle(self.deck)                                           #reshuffle the deck and return the key           
                self.key = 3

            else:
                self.label_cards.config(text="You lose with: {}".format(self.user))     #The user loses and updatethe labels to match and the health reduced
                self.label_AI_cards.config(text="Winner with: {}".format(self.dealer))
                random.shuffle(self.deck)
                self.health - 2

                
    
    def twist(self):
        """
        Add another card to the users cards

        Returns
        -------
        None.

        """
        self.user.append(self.deck[int(len(self.dealer) + len(self.user))]) #add the next card on the deck to the user
        self.show_cards()
        
    def get_key(self):      #functins for the game to allow the user to update
        return self.key
    
    def get_health(self):
        return self.health
    
    def main(health):
        win = Tk()                  #create the window
        win.title("Black Jack")
        win.geometry("600x200")
        win.resizable(False, False)
        
        myApp = BlackJack(win, health) #creat ethe mini game
        
        win.mainloop() #run the window
        

        

class Match_numbers(tk.Frame):
    """
    Match numbers is a simple game built around a number which is set as a target. The user has to press lock on the individual numbers
    to lock them in place. Once all three numbers are locked in the key is given to the user.
    
    Attributes:
        frame (tkinter object) : The frame for appilcation
        frame_enrty (tkinter object) : The frame for the entry
        frame _buttton (tkinter object): the frame for the button
        label_title (tkinter object): the label for the title
        label_info (tkinter object) : the label to show information
        button_lock (tkinter object) : the button within the GUI
        button_lock2 (tkinter object) : the button within the GUI
        button_lock3 (tkinter object) : the button within the GUI
        entry (tkinter object) : the entry for the infomration input
        health (int) : the health of the player
        count (int) : couting the loops
        key (int) : the users can get this key when the the game is completed
        user_final (list) : stores the states of the numbers
        """
    def __init__(self, win, health):
        super().__init__(master=win)
        self.pack(fill=tk.BOTH, expand = 1)     #create the window 
        
        self.frame = Frame(win, width=500, height=200,  borderwidth=2)  #create th frame, button, titles, targets
        self.frame.pack_propagate(0)
        self.frame.pack()
        
        self.frame_button = Frame(win, width=500, height=200,  borderwidth=2) #frame button 
        self.frame_button.pack_propagate(0)
        self.frame_button.pack()
        
        self.label_title = Label(self.frame, text="Match Numbers")
        self.label_title.pack()
        
        self.label_info = Label(self.frame, text = "Click the button to find random numbers and if they match you win") 
        self.label_info.pack()
        
        self.label_final = Label(self.frame, text = "Your fixed numbers will be here")
        self.label_final.pack()
        
        self.target = [random.randrange(1, 9), random.randrange(1, 9), random.randrange(1, 9)] #create three random numbers as a target
        
        self.label_target_numbers = Label(self.frame, text = "Target Numbers: {}".format(self.target)) # label target with the target variables
        self.label_target_numbers.pack()
        
        self.label_users_numbers = Label(self.frame, text = "Click the button to find random numbers and if they match you win") 
        self.label_users_numbers.pack()
        
        self.button_roll = Button(self.frame_button, text = "Roll", width=5, height=5,
                                        borderwidth=2, relief="groove", command = self.process_roll) #create all the buttons
        
        self.button_lock1 = Button(self.frame_button, text = "Lock 1", width=5, height=5,
                                        borderwidth=2, relief="groove", command = self.process_lock1)
        
        self.button_lock2 = Button(self.frame_button, text = "Lock 2", width=5, height=5,
                                        borderwidth=2, relief="groove", command = self.process_lock2)
        
        self.button_lock3 = Button(self.frame_button, text = "Lock 3", width=5, height=5,
                                        borderwidth=2, relief="groove", command = self.process_lock3)
        
        
        
        self.button_lock1.grid(row=1, column=1) #put all the buttons within the frame
        self.button_lock2.grid(row=1, column=2)
        self.button_lock3.grid(row=1, column=3)
        self.button_roll.grid(row=2, column=2)
        
        self.health = health #Set all the varibales health, count, key and users final numbers
        
        self.count = 0
        
        self.memory = []
        
        self.key = 0
        
        self.user_final = [0, 0, 0]
   
    def process_roll(self):
        """
        The process the roll. This function creates 3 random number. 
        If the target is met the key is given to the user.

        Returns
        -------
        None.

        """
        self.user_new_numbers = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)] #generate three random integers
        
        self.label_users_numbers.config(text="Your numbers: {}".format(self.user_new_numbers)) #update the numbers
        
        if self.user_final == self.target:                  #if the user gets all the random numbers in order
            self.label_info.config(text="You win the key")
            self.key = 4                                    #the user gets the key

        
    def process_lock1(self):
        """
        The user can lock in the first number

        Returns
        -------
        None.

        """
        self.user_final[0] = self.user_new_numbers[0]                           # if the user locks teh first number the set the first number to the final 
        self.label_final.config(text="Fixed Numbers: {}".format(self.user_final)) #update the user numbers
        
        if self.user_final == self.target:                  #if user final  equals target
            self.label_info.config(text="You win the key")
            self.key = 4                                    #key equals 4 (same for all teh lock functions but the index changes)

    
    def process_lock2(self):
        """
        The process lock 2 allows the user to lock the second number.
        If the second number is the final lock then the the  user gets the key.

        Returns
        -------
        None.

        """
        self.user_final[1] = self.user_new_numbers[1] 
        self.label_final.config(text="Fixed Numbers: {}".format(self.user_final))
        
        if self.user_final == self.target:
            self.label_info.config(text="You win the key")
            self.key = 4
    
    def process_lock3(self):
        """
        The process lock 3 allows the user to lock the second number.
        If the thrid number is the final lock then the the  user gets the key.

        Returns
        -------
        None.

        """
        self.user_final[2] = self.user_new_numbers[2]
        self.label_final.config(text="Fixed Numbers: {}".format(self.user_final))
        
        if self.user_final == self.target:
            self.label_info.config(text="You win the key")
            self.key = 4
        
    def get_key(self):
        return self.key
    
    def get_health(self):
        return self.health 
    
    def main(health):
        win = Tk()                  #create the window
        win.title("Levelling Up")
        win.geometry("500x500")
        win.resizable(False, False)
        
        myApp = Match_numbers(win, health) #run the appilcation
        
        win.mainloop()
        
        print("Helath level", myApp.health)
        print("Keys: ", myApp.key)

    


class LevelUp(tk.Frame):
    """
    LevelUp is a simple true and false question. There are two buttons true and false
    if they select true the game is complete if they chose false then they lose health
    
    Attributes:
        frame (tkinter object) : The frame for appilcation
        frame _buttton (tkinter object): the frame for the button
        label_title (tkinter object): the label for the title
        label_info (tkinter object) : the label to show information
        button_true (tkinter object) : the button within the GUI
        button_false (tkinter object) : the button within the GUI
        entry (tkinter object) : the entry for the infomration input
        health (int) : the health of the player
        count (int) : couting the loops
        key (int) : the users can get this key when the the game is completed
    """
    
    def __init__(self, win, health):
        super().__init__(master=win)
        self.pack(fill=tk.BOTH, expand = 1)                 #create the window
        
        self.frame = Frame(win, width=500, height=100,  borderwidth=2)
        self.frame.pack_propagate(0)
        self.frame.pack()
        
        self.frame_button = Frame(win, width=500, height=50,  borderwidth=2)
        self.frame_button.pack_propagate(0)
        self.frame_button.pack()
        
        self.label_title = Label(self.frame, text="Leveling Up Game")
        self.label_title.pack()
        
        self.label_info = Label(self.frame, text = "Is 4.8 Billion enough for the north") #print the question on the window 
        self.label_info.pack()
        
        self.button_true = Button(self.frame_button, text = "True", width=10, height=5,
                                        borderwidth=2, relief="groove", command = self.process_true) #create the buttons
        
        self.button_false = Button(self.frame_button, text = "False", width=10, height=5,
                                        borderwidth=2, relief="groove", command = self.process_false) 
        
        self.button_true.grid(row=1, column=1)
        
        self.button_false.grid(row=1, column=3 )
        
        self.health = health #set all the inital values of into attributes
        
        self.count = 0
        
        self.memory = []
        
        self.key = 0
   
    def process_true(self):
        self.label_info.config(text = "Congrats You understand leveling UP") #print you win and give the user the key
        self.key = 5    #if true the key is given to user 
    
    def process_false(self):
        self.health = self.health - 5 #return the health - 5
        
    def get_key(self):
        return self.key
    
    def get_health(self):
        return self.health
    
    def main(health):
        win = Tk()                  #create the window 
        win.title("Levelling Up")
        win.geometry("300x300")
        win.resizable(False, False)
        
        myApp = LevelUp(win, health) #run the leveling up application 
        
        win.mainloop()
        

        
class Trivia(tk.Frame):
    """
    The trivia game has three political questions to the user. These questions each have three questions. 
    The three answers have one correct. If all three are correct the key is released to the user. 
    
    Attributes:
        frame (tkinter object) : The frame for appilcation
        frameQ (tkinter object): the frame for the question
    	frameA (tkinter object): the frame for the answers
    	frameQ2 (tkinter object): the frame for the question
    	frameA2 (tkinter object): the frame for the answers
    	frameQ3 (tkinter object): the frame for the question
    	frameA3 (tkinter object): the frame for the answers
        label_title (tkinter object): the label for the title
        label_Q (tkinter object) : the label to show the question
    	label_Q2 (tkinter object) : the label to show the question
    	label_Q3 (tkinter object) : the label to show the question
    	Button_Q1_A (tkinter object) : The correct answer function is run
    	Button_Q1_B (tkinter object) : The incorrect answer function is run
    	Button_Q1_C (tkinter object) : The incorrect answer function is run
    	Button_Q1_A (tkinter object) : The incorrect answer function is run
    	Button_Q2_B (tkinter object) : The correct answer function is run 
    	Button_Q3_C (tkinter object) : The incorrect answer function is run
    	Button_Q1_A (tkinter object) : The incorrect answer function is run
    	Button_Q2_B (tkinter object) : The incorrect answer function is run
        ton_Q3_C (tkinter object) : The correct answer function is run
        entry (tkinter object) : the entry for the infomration input
        health (int) : the health of the player
        count (int) : couting the loops
        key (int) : the users can get this key when the the game is completed
    """
    
    def __init__(self, win, health):
        super().__init__(master=win)        
        self.pack(fill=tk.BOTH, expand = 1)     #create the wndow 
        
        self.frame = Frame(win, width=500, height=50,  borderwidth=2) #create all teh frames for questions and answers
        self.frame.pack_propagate(0)
        self.frame.pack()
        
        self.frameQ = Frame(win, width=500, height=50,  borderwidth=2)
        self.frameQ.pack_propagate(0)
        self.frameQ.pack()
        
        self.frameA = Frame(win, width=500, height=200,  borderwidth=2)
        self.frameA.pack_propagate(0)
        self.frameA.pack()
        
        self.frameQ2 = Frame(win, width=500, height=50,  borderwidth=2)
        self.frameQ2.pack_propagate(0)
        self.frameQ2.pack()
        
        self.frameA2 = Frame(win, width=500, height=200,  borderwidth=2)
        self.frameA2.pack_propagate(0)
        self.frameA2.pack()
        
        self.frameQ3 = Frame(win, width=500, height=50,  borderwidth=2)
        self.frameQ3.pack_propagate(0)
        self.frameQ3.pack()
        
        self.frameA3 = Frame(win, width=500, height=200,  borderwidth=2)
        self.frameA3.pack_propagate(0)
        self.frameA3.pack()
        
        self.label_title = Label(self.frame, text = "TRIVIA", font=("Arial", 30)) #create the label title and below create all the labels and the buttons
        self.label_title.pack()
        
        self.label_Q1 = Label(self.frameQ, text="First Quetsion. What colour is the Tory Party?", width = 60, height = 2, borderwidth = 2, relief = "groove")
        self.label_Q1.pack()
        
        self.Button_Q1_A = Button(self.frameA, text = "BLUE", width=10, height=5,
                                borderwidth=2, relief="groove", command = self.first_correct)       #if teh correct button is pressed then run correct function

        self.Button_Q1_B = Button(self.frameA, text = "RED", width=10, height=5,
                                        borderwidth=2, relief="groove", command = self.first_incorrect) #if the incorrect button then run the incorrect function
        
        self.Button_Q1_C = Button(self.frameA, text = "YELLOW", width=10, height=5,
                                        borderwidth=2, relief="groove", command = self.first_incorrect)
        
        
        self.Button_Q1_A.grid(row=1, column=1)
        self.Button_Q1_B.grid(row=1, column=2)
        self.Button_Q1_C.grid(row=1, column=3)
        
        self.label_Q2 = Label(self.frameQ2, text="Next Quetsion... Who is the leader of the oppsition? ", width = 60, height = 2, borderwidth = 2, relief = "groove")
        self.label_Q2.pack()
        
        self.Button_Q1_A2 = Button(self.frameA2, text = "Boris Johnson", width=10, height=5,
                                        borderwidth=2, relief="groove", command = self.second_incorrect)
        
        self.Button_Q1_B2 = Button(self.frameA2, text = "Keir Starmer", width=10, height=5,
                                        borderwidth=2, relief="groove", command = self.second_correct)
        
        self.Button_Q1_C2 = Button(self.frameA2, text = "Jeremy Corbyn", width=11, height=5,
                                        borderwidth=2, relief="groove", command = self.second_incorrect)
        
        
        self.Button_Q1_A2.grid(row=1, column=1)
        self.Button_Q1_B2.grid(row=1, column=2)
        self.Button_Q1_C2.grid(row=1, column=3)
        
        self.label_Q3 = Label(self.frameQ3, text="Final Quetsion... What political Party represents Brigton? ", width = 60, height = 2, borderwidth = 2, relief = "groove")
        self.label_Q3.pack()
        
        self.Button_Q1_A3 = Button(self.frameA3, text = "Conversitives", width=10, height=5,
                                borderwidth=2, relief="groove", command = self.thrid_incorrect)

        self.Button_Q1_B3 = Button(self.frameA3, text = "Labour", width=10, height=5,
                                        borderwidth=2, relief="groove", command = self.thrid_incorrect)
        
        self.Button_Q1_C3 = Button(self.frameA3, text = "Green Party", width=10, height=5,
                                        borderwidth=2, relief="groove", command = self.thrid_correct)
        
        self.Button_confirm = Button(self.frameA3, text = "SUBMIT", width=10, height=5,
                                        borderwidth=2, relief="groove", command = self.process)
        
        self.Button_Q1_A3.grid(row=1, column=1) # add all the buttons to the frames for teh thrid question
        self.Button_Q1_B3.grid(row=1, column=2)
        self.Button_Q1_C3.grid(row=1, column=3)
        self.Button_confirm.grid(row=2, column=2)
        
        self.results = [0, 0, 0]
        
        self.health = health
        
        self.key = 0
    
    def first_correct(self):
        self.results[0] = 1     #if correct then make the result 1 
        
    def second_correct(self):
        self.results[1] = 1
    
    def thrid_correct(self):
        self.results[2] = 1
        
    def first_incorrect(self):
        self.results[0] = 0     #if the incorrect then set to 0
        
    def second_incorrect(self):
        self.results[1] = 0
        
    def thrid_incorrect(self):
        self.results[2] = 0
        
    def process(self):
        """
        the process collects all the results and finds the total of all the questions.
        if all three questions are right the game is complete. If not there is a lose in health

        Returns
        -------
        key (int)
        health (int)

        """
        
        print("Final Process")
        print("Results: ", self.results)
        
        self.result = sum(self.results) #sum up teh results
        
        if self.result == 3:            #if the reuslts sum up to 3 give key to user
            self.key = 6
            self.master.destroy()       #close down all the windows
            return self.key, self.health
        else:
            self.key = 0
            self.health = self.health - 5 #if not all answers are correct then reduce health and keep key at 0
            return self.key, self.health
        
    def get_key(self):
        return self.key         #Allow the game program to access the key
    
    def get_health(self):
        return self.health
    
    
    def main(health):
        win = Tk()      #create the window
        win.title("Trivia")
        win.geometry("500x600")
        win.resizable(False, False)
        
        myApp = Trivia(win, health) #myApp is set to the Trivia mini-game
        
        win.mainloop()
        
        print("Helath level", myApp.health)
        print("Keys: ", myApp.key)
    
   
class Key_compare(tk.Frame):
    """
    The check compare compares the users key to the keys of the chest class.
    There is a GUI that runs this pop up
    
    Attributes:
        frame (tkinter object) : The frame for appilcation
        frame (tkinter object): the frame for the question
    	frame2 (tkinter object): the frame for the answers
    	label_title (tkinter object) : the label to show the title
    	label_info (tkinter object) : the label to show the information
    	button_check_keys (tkinter object) :The button to check the keys
        health (int) : the health of the player
        count (int) : couting the loops
        key (int) : the users can get this key when the the game is completed
    	correct_keys (list) : the keys required to get
    	user_keys (list) : the users keys
    """
    def __init__(self, win, health, correct_keys, user_keys):
        super().__init__(master=win)                                        #create the windo and inherit the window
        self.pack(fill=tk.BOTH, expand = 1)
        
        self.frame = Frame(win, width=500, height=30,  borderwidth=2)       #create the two frames 
        self.frame.pack_propagate(0)
        self.frame.pack()
        
        self.frame2 = Frame(win, width=500, height=200,  borderwidth=2)
        self.frame2.pack_propagate(0)
        self.frame2.pack()
        
        self.label_title = Label(self.frame, text="DO YOU HAVE THE KEYS", width = 60, height = 2, borderwidth = 2, relief = "groove") #label title
        self.label_title.pack()
        
        self.label_info = Label(self.frame2, text="Please show your keys", width = 60, height = 2, borderwidth = 2, relief = "groove")
        self.label_info.pack()
        
        self.button_check_keys = self.Button_Q1_A3 = Button(self.frame2, text = "Check Keys", width=10, height=5,
                                borderwidth=2, relief="groove", command = self.check_keys)                              #create the button and run function check key when pressed
        
        self.button_check_keys.pack()
        
        self.key = 0
        self.health = health
        self.count = 0 
        
        self.correct_keys = correct_keys
        self.user_keys = user_keys
        
    def check_keys(self):
        """
        Looks through the keys of user and then the chests keys
        If all the keys are met then return True to end game.
        If user does not have the keys then return False to keep game going
        """
        print("CORRECT KEYS: {} , YOUR KEYS: {}".format(self.user_keys, self.correct_keys))
        for key in self.user_keys:                          #Loop through all the keys in the key list
            if key in self.correct_keys:                    #if the key is in the correct keys list
                self.count = self.count + 1                 #Count is incremented by 1
                print("Got key")
                if self.count == 3:                         #If the count equals 3 then
                    print("GAME COMPLETE: ", self.count)    #You win the game
                    self.label_info.config(text = "Well I see you have won the game and now have the UK GOVEMENT")
            else:
                self.label_info.config(text = "Me Boris Johnson is still your leader.")                                       #If the keys are not met then return False so the game doesnt quit
    
    def get_key(self):
        return self.key
    
    def get_health(self):
        return self.health 

    def main(health):
        win = Tk()                          #create the wndow 500 by 500 
        win.title("Boris Johnsons Office")
        win.geometry("500x500")
        win.resizable(False, False)
        
        myApp = Trivia(win, health) #create trivia app and run 
        
        win.mainloop()
    


class Place_holder(tk.Frame):               #create the place holder function
    """
    The place holder mini game is there so the main app can call uponit in the rooms that do not have a minigame
    
    Attributes:
        key (int) : this stores the key at value 0
        health (int) : the health of the user
    """

    def __init__(self, win, health):
        super().__init__(master=win)
        self.pack(fill=tk.BOTH, expand = 1)
        
        self.key = 0                    #declare the key and the health
        self.health = health
        
    def get_key(self):      #methods to access the key and health
        return self.key
    
    def get_health(self):
        return self.health
        