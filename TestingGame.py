# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 15:42:17 2021

@author: 253364
"""

import unittest
from User import User
from Game import Game
from Room import Room
from Room import Chest
from user_log import User_log

from Ministers import LevelUp
from demo import App

import tkinter
import tkinter as tk
from tkinter import *

"""
Testing object is created to test the program with the unittest functions.
The testing is designed to make sure the program is working correctly. The test object inherits the unittest object allowing 
access to functions.
"""

class TestGame(unittest.TestCase):              #Create Testing object and inherit the unittesting objects
    
    def set_up(self):                            #Setup the game and user objects to access functions
        """
        Setting up the object enviroments
        user: instants of a user object
        game: instants of a game object
        """
        self.user = User()
        self.game = Game()
        
    def test_user(self):                        #Start the test user and parse through the game and user objects
        """
        Testing the users functions with the game functions
        keys: list
        objects: list
        """
        self.user.add_key(1)
        self.user.add_key(2)
        
        keys = self.user.print_keys()           #Get the keys
        
        print(self.assertEqual(keys, [1,2]))    #Test that all the keys where added
        
        self.user.pick_up_object('AIRBUS')      #Add airbus key
        self.user.pick_up_object('LNK')         #Spelt wrong so wont be added
        
        objects = self.user.donor               #Get the objects
        
        print(objects)                          #Print the objects
        
        print(self.assertEqual(objects, ['AIRBUS']))            #Check if only AIRBUS was added into the objects
        
        self.user.pick_up_object('DYSON')                       #User pick up Dyson object
        
        objects = self.user.donor                               #Set the objects now to test multiple objects

        print(self.assertEqual(objects, ['AIRBUS', 'DYSON']))   #print the result to if the multiple objects equal 
        
        self.user.put_down_object('DYSON')                      #put down the object
        
        objects = self.user.donor                               #Refrest the objects
        
        print(self.assertEqual(objects, ['AIRBUS']))            #Check if the object was removed
        
        
    def test_Room(self):                                        #Initialise the test room
        """
        Test the room functions with the user intracting a small amount
        key: list
        """
        
        self.test_Room = Room("This is a test Room", 7)         #setup the test room
        self.test_Room.add_object('AIRBUS')                     #Add object to the room 
        print(self.test_Room.getShortDescription())             #print the short and long decriptions of the room
        print(self.test_Room.getLongDescription())
        
        self.user.add_key(self.test_Room.key)                   #Add the key from the room
        key = self.user.print_keys()                            #Set the key equal the users keys
        print(key)
        
        print(self.assertEqual(key, [7]))                       #Check the key has been added correctly
    
        
    
    def test_chest(self):                                       #Check the chest
        """
        test the chest room fucntions. This tests the keys
        correct_keys: list
        
        """
        self.chest = Chest("This is the chest get the keys", None)
        
        correct_keys = self.chest.get_correct_keys()            #Get the correct keys
        print(correct_keys)
        
        self.user.add_key(1)                                    #Add all the possible keys to the user
        self.user.add_key(2)
        self.user.add_key(3)
        self.user.add_key(4)
        self.user.add_key(5)
        self.user.add_key(6)
        
        print(self.user.print_keys())                           #Check all keys have been added
        
        self.assertTrue(self.chest.check_keys(self.user.print_keys())) #Check the keys met the required keys
        
    
    def test_log(self):
        self.log = User_log()
        
        print(self.log.user_health, self.log.user_input)
        
        self.log.log_health(self.game.user.health)
        
        self.assertEqual(self.log.user_health, ['Start', 10])
        
        self.log.log_input('Go right')
        
        self.log.log_input('Go left')
        
        self.assertEqual(self.log.user_input, ['Start', 'Go right', 'Go left'])
        
        self.log.final_log()


    def test_movement(self):
        
        self.game.user.moveRoom([2,1], "RIGHT")
        
        self.game.pick_room()
        
        print(self.game.coordinates)
        
        self.game.user.moveRoom([2,1], "RIGHT")
        
        self.game.pick_room()
        
        print(self.game.current_room.description)

    
        
        
        
        
        
        
        


test = TestGame() #Run through the code
test.set_up()
test.test_log()
test.test_movement()



