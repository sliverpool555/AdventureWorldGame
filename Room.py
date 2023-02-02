"""
    Create a room described "description". Initially, it has
    no exits. 'description' is something like 'kitchen' or
    'an open court yard'
"""

import random                                                                  #Import random librayr to acces the features
from TextUI import TextUI

class Room:                                                                    #Create the class Room so it can be accessed in the game program
        

    def __init__(self, description, key, politician, game):                    #Initalise the varibals within the room object and pass through the decription and key
        """
            Constructor method
        :param description: text description for this room
        """
        self.description = description                                         #set the description to equal the description within the object
        self.exits = {}                                                        #Set the exits to a dictionary
        self.key = key                                                         #Set the objects key to the key being passed into the function
        self.objects = []                                                      #Initilise the objects for the room as a empty list
        self.textUI = TextUI()
        self.politician = politician
        self.game = game
        
        
        
    def setExit(self, direction, neighbour):                                   #set the set exit function
        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room)
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour                                      #The exit key equals the neighbour

    def getShortDescription(self):                                             #Declare the getShortDescription function
        """
            Fetch a short text description
        :return: text description
        """
        
        return self.description                                                #return the description

    def getLongDescription(self):                                              #Declare the getLongDescription
        """
            Fetch a longer description including available exits
        :return: text description
        """
        return f'Location: {self.description}, Exits: {self.getExits()} '      #return the description and the exits within a non dynamic string

    def getExits(self):                                                        #Initialse the get exits function
        """
            Fetch all available exits as a list
        :return: list of all available exits
        """
        allExits = self.exits.keys()                                           #All exits equals all the keys in the dictionary
        return list(allExits)                                                  #return list of all the keys

    def getExit(self, direction):                                              #get one exit
        """
            Fetch an exit in a specified direction
        :param direction: The direction that the player wishes to travel
        :return: Room object that this direction leads to, None if one does not exist
        """
        if direction in self.exits:                                            #if teh direction is in the exits
            return self.exits[direction]                                       #Return the exit in that direction
        else:
            return None                                                        #return nothing if not in list
    
    
    def add_object(self, obj):                              #Define the add object function and pass through the object variable from game
        """
        Adds an object to the list
        """
        self.objects.append(obj)                            #Add object to the room function
        
    def remove_object(self, obj):                           #Remove object function and pass through object
        """
        Remove the object in the inventory.
        if no object then print no object
        """
        try:                                                #Run code and if error then there is no object
            self.objects.remove(obj)
        except:                                             #except handles the error if there is no object
            self.textUI.printtoTextUI("Object not there")
        
    def return_objects(self):                               #Retrun the objects list from room
        """
        Returns objects list
        """
        return self.objects

"""
The chest class is a room which checks the checks of the user to the
random chect keys so the game is easily replayable
"""

class Chest(Room):                                          #initialise the chest room and inherit everything from the room class
    
    def __init__(self, description, objects, politician, game):               #initiialise the Chest and add the description and object
        """
        Initalise the chest room and inherit from the room class. 
        Nothing is returned
        """
        super().__init__(description, objects, politician, game)              #Pass through the vairbales from the perent class    
        self.correct_keys = random.sample(range(1, 7), 3)   #Set 3 random keys that are required to get to win the game and they are not repeats of each other
        self.count = 0                                      #Set the count to 0
        self.exits = {}
        
    def check_keys(self, keys):                             #Initisise the check Key function
        """
        Looks through the keys of user and then the chests keys
        If all the keys are met then return True to end game.
        If user does not have the keys then return False to keep game going
        """
        for key in keys:                                    #Loop through all the keys in the key list
            if key in self.correct_keys:                    #if the key is in the correct keys list
                self.count = self.count + 1                 #Count is incremented by 1
                if self.count == 3:                         #If the count equals 3 then
                    print("GAME COMPLETE: ", self.count)    #You win the game
                    return True                             #Return False to close the game
        return False                                        #If the keys are not met then return False so the game doesnt quit

                
    def get_correct_keys(self):                             #Rteurn the correct keys
        """
        Returns the correct keys
        """
        return self.correct_keys                            #Return the correct keys
    
"""
The stairs classes inherits all functions from the room class
 but has extra abilies with going up and down stairs
"""


class Stairs(Room):                                         #Initise the Stairs object and inherit fromm Room
    
    def __init__(self, description, objects, politician, game):               #Initises the varaibles and pass through description and objects
        """
        Initialising the stairs and inherit from the Room class
        Nothing is returned
        """
        super().__init__(description, objects, politician, game)              #Pass through the vairbales from the perent class 
        self.floor = False                                  #Set the floor to False as the first step is always on the lower floor
        self.exits = {}                                     #Exits as dictionaries
    
    def move_up(self):          #Move up function
        """
        Return the floor to be True
        """
        self.floor = True       #Set the floor to True so moving up stairs
        return self.floor       #Rteurn the floor (The floor is set above as well because the object needs to know the floor)
    
    def move_down(self):        #The move down function the oppsite to the move up function
        """
        Return the floor as False
        """
        self.floor = False
        return  self.floor
    
    


