# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:29:26 2021

@author: 253364
"""

import os

class User_log():
    """
    The user log is designed to store all the information on the users actions throughout the game
    Attributes:
        user_input (list) : Stores all the inputs that the user enters into the game
        user_keys (list) : the keys are stored in this list
        user_health (list) : stores all the keys at the current time to the list
    
    """
    
    def __init__(self):
        self.user_input = ["Start"] #Set all the attributes
        self.user_keys = ["Start"]
        self.user_health = ["Start"]
        
    def log_input(self, log):
        self.user_input.append(log) #log the input
        
    def log_health(self, log):
        self.user_health.append(log) #log the current health 
        
    def final_log(self):
        """
        Writes all the logs to a .txt file. In this process the lists are converted to lists and 
        then the strings to the .txt

        Returns
        -------
        None.

        """
        self.user_input.append("END")  #Add end to the end of the lists
        self.user_health.append("END")
        
        datastr = ""                        #create the datastring
        for d in self.user_input:           #Iterate through all the user input list
            datastr = datastr + d + ", "    #Add the next data to the end of datastr
            
        healthstr = ""                      #repeat for the health but add str( number) tp convert number to string
        for h in self.user_health:
            healthstr = healthstr + str(h) + ", "
        
        files = os.listdir("userlogs")                              #find all files in the userlogs
        file_name = "userlogs\\user_log_{}.txt".format(len(files))  #Add amount of files to the to number in the file to add another log file
        with open(file_name, 'w') as f:                             #open the file and write all the data into the notepad file
            f.write(datastr)
            f.write("\n")
            f.write(healthstr)
            
    
    