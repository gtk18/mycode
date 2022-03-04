#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 11:18:29 2022

@author: lastg
"""

"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""
#***************************************************
#***************************************************
#***************************************************

#                   MY CHANGES
#added a 2nd item to hallway.
#added rooms, such as the back room,west rpom, etc.
#added descriptions to each room.
#added descriptions to items when picked up.
#added another loss condition via trapdoor...

#***************************************************
#***************************************************
#***************************************************
import time
import random
import sys
# Replace RPG starter project with this code when new instructions are live

def main():
    while True:
        def showInstructions():
            """Show the game instructions when called"""
            #print a main menu and the commands
            ('''
            RPG Game
            ========
            Commands:
              go [direction]
              get [item]
            ''')
            # sys.stdout.write('Lets test how fast this types')
            # sys.stdout.flush()
            # openingString = "Lets see how slow these words print"
            # for word in openingString.split():
            #         print(word, end = ' ')
            #         time.sleep(.5)
        def endGame():
            while True:
                break
            
        def printSpaces(): #prints 10 spaces
            print("\n"*15)
            
        def playAgain():
            # currentRoom = 'Hall'
            # print("Would you like to play again?")
            while True:
                playerAction = input("Do you dare to try again? Yes/No? >>>")
            # playerAction = input("Would you like to play again? >>>")
            # while True:
                if playerAction.lower() == "yes" :
                        # showInstructions()
                        print('here we go')
                        main()
                            # clear20()        
                                # main()
                if playerAction.lower().strip() != "yes": #
                        clear20()
                        print("GOODBYE for now...")
                        time.sleep(5)
                        sys.exit()
                        # endGame()
            # while False:
                # break
                
                
        
        
        def showStatus():
            """determine the current status of the player"""
            #print the player's current status
            print('-------------------------------')
            print('-------------------------------')
            print("\033[1;33;11mYou are standing in the \033[0;0m" + currentRoom +"\033[1;33;11m ... \033[0;0m")
            #-------------------------------------------------
            # Room Descriptions, aka room statuses
            if currentRoom == 'Hall':
                openSentence = "This hallway seems to smell. You don't remember how you got here, but you know you need to get out."
                for word in openSentence.split():
                    print(word, end = " ")
                    time.sleep(.05)
                openSentence2 = "You notice that you can go east, west, or south. But the south looks completely dark."
                for word in openSentence2.split():
                    print(word, end = " ")
                    time.sleep(.05)
                print()                
                time.sleep(.5)
            if currentRoom == 'West Room':
                print("The room is rather empty.")
                print("But after scanning some time...you notice a cellar door on the floor in the corner...")
                print("You can do down or east...")
            if currentRoom == 'Kitchen' : 
                print("You have made a grave mistake...")
            if currentRoom == 'Dining Room' : 
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
            print('--------------------------------')
            
            
        def clear20():
            print("\n"*20)
        clear20()    
        
        #start the player in the Hall
        currentRoom = 'Hall'
        # print('\n')#; print( ' You  are standing in a narrow hallway. You see that you can go east, west, or south.')
        #an inventory, which is initially empty
        inventory = []
        
        #a dictionary linking a room to other rooms
        rooms = {
        
                    'Hall' : { 
                          'south' : 'Kitchen',
                          'east' : 'Dining Room',
                          'west' : "West Room",
                          'item' : 'key',
                          'item2' : 'lamp',
                          
                        },
                    'West Room' :{
                        'east' : 'Hall',
                        'item' : 'plate',
                        'down' : 'Cellar',
                        },
                    'Cellar' : { 
                        
                        },
        
                    'Kitchen' : {
                          'north' : 'Hall',
                          'item' : 'monster',
                        },
                    'Dining Room' : {
                        'west' : 'Hall',
                        'south': 'Back Room',
                        'item' : 'potion',
                        },
                    'Back Room' :{
                        'north' : 'Dining Room',
                    }
        
                 }
      
         
      
        showInstructions()
    
        #loops while condition is True
        while True:
            showStatus()      
            #get the player's next 'next_action'
            #.split() breaks it up into an list array
            #eg typing 'go east' would give the list:
            #['go','east']
            next_action = ''
            while next_action == '':  
                next_action = input('What do you want to do now? >')
                clear20()
            
            # split allows an items to have a space on them
            # get golden key is returned ["get", "golden key"]          
            next_action = next_action.lower().split(" ", 1) # delimiter here is a space, and a max split of 1
          
            #if they type 'go' first
            if next_action[0] == 'go':
                # print(next_action) #added to view output
                # print(next_action[1]) #added to view output as well
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
                        print("\033[1;36;11m The key glows as you pick it up... \033[0;0m")
                    if next_action[1] == 'potion':
                        print("*************")
                        # print("\033[1;36;11m The potion shakes in your hand and mysteriously starts to fill on it's own... \033[0;0m")
                        potionStory = "\033[1;36;11m The potion shakes in your hand and mysteriously starts to fill on it's own... \033[0;0m"
                        for word in potionStory.split():
                            print(word, end = " ")
                            time.sleep(.05)
                        time.sleep(3)
                        print('\n',"*************")
                    #display a helpful message
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
                    print('Can\'t get ' + next_action[1] + '!')
            
        ## If a player enters a room with a monster
            if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
                print("")
                print('A monster emerges and drags you off into the darkness... \n\033[1;31;11m      GAMEOVER!!! \033[0;0m')
                playAgain()
                clear20() 
                
            ## Define how a player can win
            if currentRoom == 'Back Room' and 'key' in inventory and 'potion' in inventory:
                print('You throw the magic potion at the wall to reveal a hidden locked door. You use the key and escape the house... YOU WIN!')
                playAgain()
                clear20() 
        
            if currentRoom == 'Cellar' :
                print("The ladder breaks as you start to climb down.")
                print("You fall flat on your face!")
                print("There is a growling noise...and SNAP!!! A creature clamps on to your leg and drags you deep into the cellar. It's over for you... GG!")
                playAgain()
                clear20() 
                
if __name__ =='__main__':
       main()   

