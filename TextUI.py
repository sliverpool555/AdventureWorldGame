"""
    A simple text based User Interface (UI) for the
    Adventure World game
"""

class TextUI:                                                           #Create Object

    def __init__(self):                                                 #Initialise the textUI
        pass

    def getCommand(self):                                               #Initilise the getCommand Functionn
        """
            Fetches a command from the console
        :return: a 2-tuple of the form (commandWord, secondWord)
        """
        word1 = None                                                    #Set both words to equal none so if they are not set in a few lines there is still a handle
        word2 = None
        print('> ', end='')
        inputLine = input()                                             #Get input from the console
        if inputLine != "":                                             #If there is something in the string
            allWords = inputLine.split()                                #Split up the words into list
            word1 = allWords[0]                                         #the first word
            if len(allWords) > 1:                                       #If there is more then 1 word
                word2 = allWords[1]                                     #the second word is the second word after the split
            else:
                word2 = None                                            #If no second word then set second word to None
            # Just ignore any other words
        return (word1, word2)                                           #return Both words

    def printtoTextUI(self, text):
        """
        Prints the text to the Console
        """
        print(text)     #Prints the text to the console                 
