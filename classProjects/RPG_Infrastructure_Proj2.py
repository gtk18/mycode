#!/usr/bin/env python3
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

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #-------------------------------------------------
    # Room Descriptions, aka room statuses
    if currentRoom == 'Hall':
        print("This hallway seems to smell. You don't remember how you got here, but you know you need to get out.")
        print("You notice that you can go east, west, or south. But the south looks completely dark.")
    if currentRoom == 'West Room':
        print("The room is rather empty.")
        print("But after scanning some time...you notice a cellar door on the floor in the corner...")
        print("You can do down or east...")
    if currentRoom == 'Kitchen' : 
        print("You have made a grave mistake...")
    if currentRoom == 'Dining Room' : 
        print("You can go west or south.")
        print("This place looks like some sort of lab.")
    if currentRoom == 'Back Room':
        print("This looks like a dead end, but almost as if one of the walls should have a door...")
        print("You can only go north.")
    #-------------------------------------------    
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    # print("---------------------------")
    if "item2" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item2'])
    print("---------------------------")  


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

#start the player in the Hall
currentRoom = 'Hall'#; print( ' You  are standing in a narrow hallway. You see that you can go east, west, or south.')


showInstructions()

#loop forever
while True:
    showStatus()
  
    #get the player's next 'next_action'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    next_action = ''
    while next_action == '':  
        next_action = input('What do you want to do now? >')
    
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
                print("The key glows as you pick it up...")
            if next_action[1] == 'potion':
                print("*************")
                print("The potion begins to rattle in your hand and myseteriously fills with an unknown liquid.")
                print("*************")
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
        print('A monster has got you... GAME OVER!')
        break
    ## Define how a player can win
    if currentRoom == 'Back Room' and 'key' in inventory and 'potion' in inventory:
        print('You throw the magic potion at the wall to reveal a hidden locked door. You use the key and escape the house... YOU WIN!')
        break

    if currentRoom == 'Cellar' :
        print("The ladder breaks as you start to climb down.")
        print("You fall flat on your face!")
        print("There is a growling noise...and SNAP!!! A creature clamps on to your leg and drags you deep into the cellar. It's over for you... GG!")
        break
