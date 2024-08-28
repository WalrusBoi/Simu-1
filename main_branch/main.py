import random
import sys
import time
import bpy
import math

# Deselect all objects
bpy.ops.object.select_all(action='DESELECT')

# Select all objects
bpy.ops.object.select_all(action='SELECT')

# Delete selected objects
bpy.ops.object.delete()


GRID_LENGTH = 10 # self explanatory
MIN_GRID_LENGTH = -GRID_LENGTH
SIMS_NUM = 10 # amount of sims
FOOD_NUM = 100 # amount of food
CUBE_SIZE = 0.5
sims = [] # list full of the sims
food = []
MATERIAL_GREEN = bpy.data.materials.new(name = "green")
MATERIAL_GREEN.diffuse_color = (0.0, 1.0, 0.0, 1.0)
FRAME_RATE = 60
PI = math.pi

class Food:
    def __init__(self, location, name):
        self.location = location
        self.name = name

class Sim:
    def __init__(self, name):
        self.name = name
        self.x = 0 # positionary variable
        self.y = 0 # ^
        self.energy = 10 # energy allows the sims to move
        self.energyPerTurn = 1
        self.movement = 1.5/FRAME_RATE # speed allows the sims to 
        self.range = 5
        self.closestFood = ()
        self.distanceToFood = 1000
        self.foodAte = 0
        self.angle = 0
        self.angleChange = {
            "finalAngle" : None,
            "changing" : False,
            "increment" : None
        }  

    def checkValidity(self): # Checks to see if the sims location is on the grid
        if self.x > GRID_LENGTH or self.y > GRID_LENGTH or self.x <  MIN_GRID_LENGTH or self.y < MIN_GRID_LENGTH: 
            return False # returns False if off grid
        return True # returns True if on grid

    def updateLocation(self):
        self.blenderID.location = (self.x, self.y, (CUBE_SIZE/2))        

    def move(self): # Movement function split into nested functions which involves all movement capabilities. Using this function is the only way to access sim movement
        def moveUp():
            self.y += self.movement # what this repeated chunk of code does is checks to see if the move valid and then takes energy if the move is valid
            if self.checkValidity(): # if the move is invalid, the sim is returned to it's original spot and energy is not consumed
                return True # the reason this code is repeated is because i did not want to deal with the operator module which would've had to be implemeneted to make this block of code a function
            else:
                self.y -= self.movement 
                return False         
        def moveDown():
            self.y -= self.movement
            if self.checkValidity():
                return True # returns true if the move is vaid
            else:
                self.y += self.movement
                return False            
        def moveLeft():
            self.x -= self.movement
            if self.checkValidity():
                return True
            else:
                self.x += self.movement     
                return False       
        def moveRight():
            self.x += self.movement
            if self.checkValidity():
                return True
            else:
                self.x -= self.movement      
                return False       

        def moveRandomly(): # moves the sim in a random          
            hasMovementOccurred = False # has a player moved yet?
            randIntLast = [] # all previous invalid moves

            while not hasMovementOccurred: # runs until player movement has been ensured
                randInt = random.randint(1,4) # sets a random integer to allow the sim to move in a random direction
                if randInt in randIntLast: # checks to see if the current random integer has previously been shown to be invalid
                    continue # skips operations to save time
                match randInt:
                    case 1:
                        if moveUp(): hasMovementOccurred = True
                    case 2:
                        if moveDown(): hasMovementOccurred = True
                    case 3:
                        if moveLeft(): hasMovementOccurred = True
                    case 4:
                        if moveRight(): hasMovementOccurred = True
                if hasMovementOccurred == False:
                    randIntLast.append(randInt) # adds the randInt as an invalid move

            self.energy -= self.energyPerTurn
            self.updateLocation()
    
        def moveTowardsFood(): # moves the sim towards the nearest food tile if one is located
            self.locateClosestFood() # calls the food function   
            if self.range >= self.distanceToFood: # in range to spot food
                if self.distanceToFood <= self.movement*2: # if the speed (movement per turn) is greater than the distance to the food, it can eat
                    howMuchFood = 1
                    self.foodAte += howMuchFood
                    for i in range(howMuchFood):
                        print(self.closestFoodBlender.location)
                        bpy.data.objects.remove(self.closestFoodBlender.blenderID)
                        food.remove(self.closestFoodBlender) # removes every instance of the food that was just ate
                    self.locateClosestFood()

                else:
                    distance_x = self.x - self.closestFood[0] #
                    distance_y = self.y - self.closestFood[1]
                    if abs(distance_x) >= self.movement: # if the distance from the object is more than the eating range
                        if distance_x > 0:
                            moveLeft()
                        else:
                            moveRight()

                    elif abs(distance_y) >= self.movement: # if the distance from the object is more than the eating range
                        if distance_y > 0:
                            moveDown()
                        else:
                            moveUp()
                        
                    else:
                        print("there has been a serious error, investigate")
                        print(self.closestFood)
                        print(self.distanceToFood)
                self.updateLocation()
                self.energy -= self.energyPerTurn
            else: 
                moveRandomly()

        moveTowardsFood()           
        return None

    def locateClosestFood(self): # finds the closest piece of food
        distance = sys.maxsize
        closest_food = ()
        #TODO implement check for if there is no food on board
        for i in food:
            new_distance = abs((self.x - i.location[0])) + abs((self.y - i.location[1])) # checks to see the distance between the player and the food tile
            if distance > new_distance:
                distance = new_distance # finds the smallest distance
                closest_food = i
        self.closestFood = closest_food.location
        self.closestFoodBlender = closest_food
        self.distanceToFood = distance
    
    def printCoordinates(self):
        print(f'{self.name} is at {self.x}, {self.y}')

def createGrid():
    bpy.ops.mesh.primitive_grid_add(size=GRID_LENGTH*2)    

def createFood():
    for i in range(FOOD_NUM):
        current_food = Food((random.randint(MIN_GRID_LENGTH, GRID_LENGTH), random.randint(MIN_GRID_LENGTH,GRID_LENGTH)), f'food_{str(i+1)}') # creates food object
        bpy.ops.mesh.primitive_cube_add(size = CUBE_SIZE/2)
        current_food.blenderID = bpy.context.object
        current_food.blenderID.name = current_food.name
        food.append(current_food)
        current_food.blenderID.location = (current_food.location[0], current_food.location[1], (CUBE_SIZE/4))  
        current_food.blenderID.data.materials.append(MATERIAL_GREEN)


def createSims(): 
    for i in range(SIMS_NUM):
        current_sim = Sim("sim_" + str(i+1))
        bpy.ops.mesh.primitive_cube_add(size=CUBE_SIZE)
        current_sim.blenderID = bpy.context.object
        current_sim.blenderID.name = current_sim.name
        sims.append(current_sim)

def delayFunction(delay, function):
    def doFunction():
        function()
    bpy.app.timers.register(doFunction, first_interval=delay)

def move_sims_with_delay(delay=0.5):
    for i in sims:
        delayFunction(1, i.move)

def updateCanvas():
    for i in sims:
        i.move()
    bpy.app.timers.register(updateCanvas, first_interval=1.0 / FRAME_RATE)
        
def placeSims():
    for i in sims:
        i.x = random.randint(MIN_GRID_LENGTH,GRID_LENGTH)
        i.y = random.randint(MIN_GRID_LENGTH,GRID_LENGTH)
        i.updateLocation()

def simulateDay():
    createFood()
    placeSims()

def startSimulation():
    createGrid()
    createSims()
    simulateDay()
    updateCanvas()

startSimulation()