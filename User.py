# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 12:19:25 2021

@author: Samuel Gandy
"""

from TextUI import TextUI

"""
Inventory object is used to store objects the user is carying. 
"""

class Inventory:
    
    def __init__(self):
        """
        Initisaling the inventory object
        keys: list
        donor: list
        donor: dictionary
        weight: int
        """
        self.keys = []
        self.donor = []
        self.donor_list = {'DYSON': (3, 1), 'AIRBUS': (5, 1), 'BLOOMBERG': (3, 1), 'CITYLINK': (3, 1), 'JPMORGAN': (2, 1), 'LNT': (2, 1)} #Key is the name of donor, the first item is health increase and second item is weight
        self.weight = 0
    
    def add_key(self, key):                 #Add key function
        """
        Add Key function
        keys: list
        key: int
        """
        if key != None and key != 0:        #If key is not equal to None or 0
            self.keys.append(key)           #Add the key
        
    def print_keys(self):                   #Print keys function
        print(self.keys)                    #print keys and return the keys
        return self.keys
            
    def check_weight(self): 
        print(self.weight)                  #prints the weight of the backpack
    
    def return_donor(self):                 #Return the donors which increase the campain health
        return self.donor
    
"""
User Object is used for the user to intract with the game.
The user object inherits functions from the inventory
"""    


class User(Inventory):                                                          #The user object inhirets from the inventory
    
    def __init__(self):
        """
        Initialise the User object
        health: int
        inventory: inventory object
        keys: list
        donor: list
        donor_list: dictionary
        weight = 0
        object_list: dictionary
        textUI: TextUI Object
        """
        self.health = 10                                                        #The health of the users campain to start with is 10
        self.inventory = Inventory()                                            #Initislses an inventory within the object
        self.keys = []                                                          #The user starts with no keys
        self.all_keys = [1,2,3,4,5,6]                                           #All keys array has the numbers of the keys to compare later on
        self.donor = []                                                         #The donnor list. This is where all the donors picked up are stored
        self.donor_list = {'DYSON': (3, 1), 'BLOOMBERG': (5, 1), 'AIRBUS': (3, 1), 'CITYLINK': (3, 1), 'JPMORGAN': (3, 1), 'LNT': (2, 1)} #Key is the name of donor, the first item is health increase and second item is weight
        self.weight = 0                                                         #Set the inital weight to 0
        self.object_list = {}                                                   #initise the object list
        self.textUI = TextUI()              #Create the textUI object
        
    def use_donor(self, imp):                                                   #Apply the donor to increase campagin health
        """
        Use Donor: Uses the user object and inventory. 
        imp: input as a string
        
        returns the donor and weight
        """
        
        if imp in self.donor:                                                   #if input is in the donor list
            print("Your using ", imp)                                           
            f = self.inventory.donor_list.get(imp)[0]                           #Using the input as key to find the weight
            if (self.health + f) < 20:                                          #if the users health is less then 20
                self.health = self.health + f                                   #Increase the health
                self.weight = self.weight - self.inventory.donor_list.get(imp)[1]    #remove wieght in inventory
                print("Removing ", imp)                                         #remove the object
                self.donor.remove(imp)                                          
                return self.donor, self.weight                                  #Return the upeded donor list and the weight                                                     
            else:
                self.textUI.printtoTextUI("Health Bar Full") 
                return self.donor, self.weight                                  #return the non updeated donor list and weight
        else:
            self.textUI.printtoTextUI("You do not have that campign donor")
            return self.donor, self.weight
                
    def pick_up_object(self, obj):                                              #Pick up the object function and pass through the object
        """
        Pick up object prasing through obj
        object are added to the user but nothing returned into the game
        """
        if self.donor == None:                                                  #If the donor list is None reset back to a empty list
            self.donor = []
            
        if obj in self.donor_list.keys():                                       #If the object is one of the keys in the donor list
            print("Picking up ", obj)
            self.donor.append(obj)                                              #Add the object to the users order
            self.textUI.printtoTextUI(self.donor)
            f = self.donor_list.get(obj)[1]                                     #The object is the key in the donor list and then look at the second bit of data
            if self.weight < 20:                                                #If data is less then 20
                self.weight = self.weight + f                                   #Add the weight
            else:
                self.textUI.printtoTextUI("Backpack is too heavy")
        
        elif obj in self.object_list:
            print("Picking up Onject", obj)
            
        elif obj in self.all_keys:
            self.textUI.printtoTextUI("Add key")
            
        else:
            self.textUI.printtoTextUI("Cannot pick up that object")
        
    def put_down_object(self, obj, currentRoom):                                #declare the put_down_object
        """
        InpitsL obj and currentroom parsed into the function
        currentRoom adds the object and the object is removed from the user. 
        Then the weight is changed
        """
        if obj in self.donor:                                                   #if the object is in the users donor list
            currentRoom.objects.append(obj)                                     #Add the object to the current rooms objects
            self.donor.remove(obj)                                              #remove the object from the users donor list
            self.weight = self.weight - self.inventory.donor_list.get(obj)[1]   #find the weight (Mentioned above) then take away the weight to the weight of item
            return self.donor, currentRoom, self.weight                         #Return the donor, current room and weight
        else:
            self.textUI.printtoTextUI("You dont have object to put down")
            
            
    
    def show_health(self):                  #The function to show the health
        self.textUI.printtoTextUI(self.health)                  #print health
        
    def reduce_health(self, damge):         #reduce health function
        """
        reduce health: parses through the damage and adjust health accordingly
        """
        self.health = self.health - damge   #The health is reduced as much as the damge
        if self.health < 1:                 #if the user reduces less then 1 then the users campagin ends
            self.textUI.printtoTextUI("Your Campign is over!!!")
        else:
            self.textUI.printtoTextUI("Be careful")
        
       
    def moveRoom(self, coordinates, movement):                      #Move room function parsing through the current coordinates and movement
        """
        Move room:
            input: coordinates and movement
            return: the adjusted coordinates
        
        """
        self.textUI.printtoTextUI("Movement")
        #if movement in Exits:
        if movement.upper() == "RIGHT":                             #If the movement is right
            coordinates =[coordinates[0], (coordinates[1] + 1)]     #Keep the coordinates on the first element the same and plus the second by 1 and set it equal to the coordinates
            self.textUI.printtoTextUI("WE ARE GOING RIGHT")
            
        if movement.upper() == "LEFT":                              #If left and then the second element - 1
            coordinates = [coordinates[0], (coordinates[1] - 1)]    
            self.textUI.printtoTextUI("Going Left")
                
        if movement.upper() == "UP":                                #If up then decrease by 1 on the first coordinate
            coordinates = [(coordinates[0] - 1), coordinates[1]]
            self.textUI.printtoTextUI("GOING UP")

                
        if movement.upper() == "DOWN":                              #If up then increase by 1 on the first coordinate
            coordinates = [(coordinates[0] + 1), coordinates[1]]
            self.textUI.printtoTextUI("GOING DOWN")
            
        if movement.upper() == "STAY":                              #If stay then stay in the same place
            coordinates = coordinates
        
        return coordinates
        