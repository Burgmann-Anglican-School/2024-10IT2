import weakref
import os

class Room:
    roomInstances = []
    def __init__(self, name, description, coord_x, coord_y):
        self.name = name
        self.description = description
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.location = (self.coord_x, self.coord_y)
        self.__class__.roomInstances.append(weakref.proxy(self))

tavern = Room("the tavern", "a dingey tavern",0,0)
street = Room("a dark street", "a dark street outside a tavern",1,0)

currentRoom = tavern
whereyouwanttobe = 0,0

def checkInput(a):
    if a == "north":
        global whereyouwanttobe
        whereyouwanttobe = currentRoom.location[0], currentRoom.location[1] + 1
        return whereyouwanttobe
    
def checkMovement(b):
    os.system('cls' if os.name == 'nt' else 'clear')
    for instance in Room.roomInstances:
        if b == instance.location:
            canMove = True
            global currentRoom
            currentRoom = instance
            print(f'moved to {currentRoom.name}')
            break
        else:
            canMove = False
    if not canMove:
        print("you can't move in that direction")

while True:
    print(f'You are in {currentRoom.name}')
    print(currentRoom.description)
    command = input('Enter a command').lower()
    location = checkInput(command)
    checkMovement(location)
   