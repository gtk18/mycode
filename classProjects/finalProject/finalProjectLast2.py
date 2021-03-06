# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 23:22:23 2022

@author: lastg
"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 11:18:29 2022

@author: lastg
"""

"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""
#***************************************************

import time
# import random
import sys
import os

# from os import system
# =============================================================================
# def showRules():
#    print("These are the rules...")  
#    print('''
#     If you want to survive...
#     Movement
#     Actions
#     ''')
# showRules()
# 
# 
# def showInstructions(): #defining function
#     print('''
#     Text-Based Adventure Game
#     ========
#     Commands:
#       go [direction]    example: go west
#       get [item]        example: get item
#     ''')
# time.sleep(1)    
# showInstructions()
# 
# def introName():
#     print(input("What is your name? >>>"))
#     user_name = input
#     print("Welcome adventurer...")
# introName()
# 
# =============================================================================



def main():
# =============================================================================
#     ### user_input = input("What would you like to do? Game or Research?")
#     ### if user_input = "Game"
# =============================================================================
        # def showRules():
        #    print("These are the rules...")  
        #    ('''
        #     Movement
        #     Actions
        #     ''')
# while True: #while condition is true, runs while loop
        # os.system('cls')
        # os.system('clear')
        # showRules() 
        # time.sleep(5)
# =============================================================================
#         def showInstructions(): #defining function
#             print('''
#             Text-Based Adventure Game
#             ========
#             Commands:
#               go [direction]    example: go west
#               get [item]        example: get item
#             ''')
#         time.sleep(1)    
#         showInstructions()        
# =============================================================================
# =============================================================================
#             # sys.stdout.write('Lets test how fast this types')
#             # sys.stdout.flush()
#             # openingString = "Lets see how slow these words print"
#             # for word in openingString.split():
#             #         print(word, end = ' ')
#             #         time.sleep(.5)
# =============================================================================
# =============================================================================
#         def endGame():
#             while True:
#                 sys.out()
# =============================================================================
        def clrscr():
            "testing the os clear screen method..."
    # Check if Operating System is Mac and Linux or Windows
            if os.name == 'posix':
                _ = os.system('clear')
            else:
      # Else Operating System is Windows (os.name = nt)
                _ = os.system('cls')
    
            print("Screen Cleared")
        clrscr()    
        
        def printSpaces(): #prints 15 spaces
            print("\n"*15)
            
        def playAgain(): #function to start game over at the main room
            # currentRoom = 'Main Room'
            # print("Would you like to play again?")
            while True:
                playerAction = input("\033[1;33;11mDo you dare to try again? Yes/No? >>>\033[0;0m")
            # playerAction = input("Would you like to play again? >>>")
            # while True:
                if playerAction.lower() == "yes" :
                        # showInstructions()
                        clear25()
                        print('Herrreee we go!!!')
                        time.sleep(1)
                        main()
                if playerAction.lower().strip() != "yes": #does not matter how yes is typed or white spaces
                        clear25()
                        print("\033[1;31;11mGOODBYE\033[0;0m...for now...")
                        time.sleep(5)
                        sys.exit() #calls the function from sys to exit out of program if answered no.
                        
        def showStatus(): #defined function that describes the current status of player
            print('-------------------------------')
            print("\033[1;33;11mYou are standing in the \033[0;0m" + currentRoom +"\033[1;33;11m ... \033[0;0m") #print main words in yellow, [type,fg,bg]]
            #-------------------------------------------------
            # Room Descriptions, aka what room statuses
            if currentRoom == 'Main Room': #if Main room then run this loop...
                openSentence = "You don't remember how you got here, but you know you need to get out."
                for word in openSentence.split(): #splits the string into a list[x,y,z]
                    print(word, end = " ") #removes the default newline and prints one word after another
                    time.sleep(.05) #adds a delay on the words being printed out. the higher the slower the words are printed
                openSentence2 = "You notice that you can go east, west, south, or upstairs. Beware, the south looks completely dark."
                for word in openSentence2.split():# same as above lines
                    print(word, end = " ")
                    time.sleep(.05) #delay of words
                print()                
                # time.sleep(.5) #delay before next loop
            if currentRoom == 'West Room':
                print("The room is rather empty.")
                print("But after scanning some time...you notice a cellar door on the floor in the corner...")
                print("You can do down or east.")
            if currentRoom == 'Kitchen' : 
                print("You have made a grave mistake...")
            if currentRoom == 'Laboratory' : 
                print("This place looks like some sort of lab.")
                print("You can go west or south.")
            if currentRoom == 'Back Room':
                print("This looks like a dead end, but almost as if one of the walls should have a door...")
                print("You can only go north.")
            #-------------------------------------------    
            #print the current inventory
            print('\033[3;36;11mInventory\033[0;0m ' + str(inventory))
            #print an item if there is one
            if "item" in rooms[currentRoom]:
              print('You see a ' + rooms[currentRoom]['item'])
            # print("---------------------------")
            if "item2" in rooms[currentRoom]:
                print('You see a ' + rooms[currentRoom]['item2'])
            print("--------------------------------")  
                    
        def clear25():
            print("\n"*35)
            # os.system('clear')
        # os.system('clear')
        clear25()    
        
        #start the player in the Main Room
        currentRoom = 'Main Room'
        # print('\n')#; print( ' You  are standing in a narrow Main Roomway. You see that you can go east, west, or south.')
        
        #starting inventory that is empty
        inventory = []
        #dictionary that links all rooms in one way or another
        rooms = {
        
                    'Main Room' : {           #MAIN LEVEL, LOWER LEVEL
                          'south' : 'Kitchen',
                          'east' : 'Laboratory',
                          'west' : "West Room",
                          'item' : 'key',
                          'item2' : 'lamp',
                          'upstairs': 'Upstairs Hallway'
                        },
                                      
                    'West Room' :{
                        'east' : 'Main Room',
                        'item' : 'plate',
                        'down' : 'Cellar',
                        },
                    'Cellar' : { 
                        
                        },
        
                    'Kitchen' : {
                          'north' : 'Main Room',
                          'item' : 'monster',
                        },
                    'Laboratory' : {
                        'west' : 'Main Room',
                        'south': 'Back Room',
                        'item' : 'potion',
                        },
                    'Back Room' :{
                        'north' : 'Laboratory',
                        },
# =============================================================================
#                     #UPPER LEVEL     
# =============================================================================
                    # 'Main Room' : {          USE FOR REFERENCE ONLY For DOWNSTAIRS
                    #     'upstairs': 'Upstairs Hallway'

                    'Upstairs Hallway' : { 
                          'downstairs' : 'Main Room',
                          'east': 'Guest Bedroom1',
                          'northeast' : 'Guest Bedroom2',
                          'south' : 'Large Balcony',
                          'west' : 'Main Bedroom',
                        },
                    'Main Bedroom' : { 
                         'east' : 'upstairs hallway',
                         'south' : 'Balcony',
                        },
                    'Guest Bedroom1' : {
                        'west' : 'Upstairs Hallway',
                        },
                    'Guest Bedroom2' : {
                        'southwest' : 'Upstairs Hallway',
                        },
                    'Large Balcony' : {
                        'north' : 'Upstairs Hallway',
                        'west' : 'Balcony',
                        },
                    
                    # 'Spare Bedroom' : { 
                    #      'west' : 'upstairs hallway',
                    #     },  
                }
      
         
      
        # showInstructions()
    
        #loops while condition is True
        while True:
            showStatus()      
            #get the player's next 'next_action'
            #.split() breaks it up into an list array
            #for example, 'go east' would give the list:['go','east']
            next_action = ''
            while next_action == '':  
                next_action = input('\033[1;33;11mHow does thou wish to proceed? >>>\033[0;0m')
                clear25()
                             
            next_action = next_action.lower().split(" ", 1) # delimiter here is a space, and a max split of 1
            #if they type 'go' as their first action
            if next_action[0] == 'go':
# =============================================================================
#                 # print(next_action) #added to view output
#                 # print(next_action[1]) #added to view output as well
# =============================================================================
                #check that they are allowed wherever they want to go
                if next_action[1] in rooms[currentRoom]:
                    #set the current room to the new room
                    currentRoom = rooms[currentRoom][next_action[1]]
                    print("")
                #there is no door (link) to the new room
                else:
                    print('You can\'t go that way!')
          
            #if they type 'get' first
            if next_action[0] == 'get' :
                #if the room contains an item, and the item is the one they want to get
                if "item" in rooms[currentRoom] and next_action[1] in rooms[currentRoom]['item']:
                    #add the item to their inventory
                    inventory += [next_action[1]]
                    if next_action[1] == 'key':   #if item picked up is key, will print the next message...
                        print("\033[1;36;11m The key glows as you pick it up... \033[0;0m") #prints in light blue
                    if next_action[1] == 'potion': #if second attribute is called this
                        print("*************")
                        # print("\033[1;36;11m The potion shakes in your hand and mysteriously starts to fill on it's own... \033[0;0m")
                        potionStory = "\033[1;36;11m The potion shakes in your hand and mysteriously starts to fill on it's own... \033[0;0m"
                        for word in potionStory.split(): #splits the string into separate items
                            print(word, end = " ") #prints without new lines
                            time.sleep(.05)
                        time.sleep(3)
                        print('\n',"*************")
                    print(next_action[1] + ' item taken!')
                    #delete the item from the room
                    del rooms[currentRoom]['item']
                
                    
                #otherwise, if the item isn't there to get
                elif 'item2' in rooms[currentRoom] and next_action[1] in rooms[currentRoom]['item2']:
                    inventory += [next_action[1]]
                    print(next_action[1] + 'taken!')
                    del rooms[currentRoom]['item2'] #removes item if taken
                else:
                    #tell them they can't get it
                    print("\033[1;31;11mCan't get that\033[0;0m " + next_action[1] + "\033[1;31;11m!\033[0;0m")
            
        #LOSS condition if monster 'item' is in the current room
            if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
                print("")
                print('A monster emerges and drags you off into the darkness... \n\033[1;31;11m      GAMEOVER!!! \033[0;0m')
                playAgain()
                clear25() 
            if currentRoom == 'Cellar' :
                print("The ladder breaks as you start to climb down.")
                print("You fall flat on your face!")
                print("There is a growling noise...and SNAP!!! A creature clamps on to your leg and drags you deep into the cellar. It's over for you... GG!")
                playAgain()
                clear25()        
         #WIN condtions
            if currentRoom == 'Back Room' and 'key' in inventory and 'potion' in inventory:
                print('\033[1;34;11mYou throw the magic potion at the wall to reveal a hidden locked door. You use the key to break free...\033[0;0m \033[1;32;11mWinner Winner, Chicken Dinner!\033[0;0m')
                playAgain()
                clear25() 
        
           
                
if __name__ =='__main__':
       main()   

