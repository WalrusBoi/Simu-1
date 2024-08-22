import random
import sys
import time

GRID_LENGTH = 10 # self explanatory
MIN_GRID_LENGTH = GRID_LENGTH*-1
SIMS_NUM = 10 # amount of sims
FOOD_NUM = 20 # amount of food
CUBE_SIZE = 0.5
sims = [] # list full of the sims
food = [] # list of food coordinates

class Sim:
    def __init__(self, name):
        self.name = name
        self.x = 0 # positionary variable
        self.y = 0 # ^
        self.energy = 10 # energy allows the sims to move
        self.energyPerTurn = 1
        self.movement = 1 # speed allows the sims to 
        self.range = 5
        self.closestFood = ()
        self.distanceToFood = 1000
        self.foodAte = 0

    def checkValidity(self): # Checks to see if the sims location is on the grid
        if self.x > GRID_LENGTH or self.y > GRID_LENGTH or self.x <  MIN_GRID_LENGTH or self.y < MIN_GRID_LENGTH: 
            return False # returns False if off grid
        return True # returns True if on grid

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
        
        def moveTowardsFood(): # moves the sim towards the nearest food tile if one is located
            self.locateClosestFood() # calls the food function   
            if self.range >= self.distanceToFood: # in range to spot food
                if self.distanceToFood <= self.movement: # if the speed (movement per turn) is greater than the distance to the food, it can eat
                    howMuchFood = food.count(self.closestFood) # counts how many instances of food are in the tile (in case of food stacking onto the same tile)
                    self.foodAte += howMuchFood
                    for i in range(howMuchFood):                        
                        food.remove(self.closestFood) # removes every instance of the food that was just ate
                    self.locateClosestFood()

                else:
                    distance_x = self.x - self.closestFood[0] # (1,2 2,2)
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

            else: 
                moveRandomly()
        
        moveTowardsFood()

    def locateClosestFood(self): # finds the closest piece of food
        distance = sys.maxsize
        closest_food = ()
        for i in food:
            new_distance = abs(abs((self.x - i[0])) + abs((self.y - i[1]))) # checks to see the distance between the player and the food tile
            if distance > new_distance:
                distance = new_distance # finds the smallest distance
                closest_food = i 
            
        self.closestFood = closest_food
        self.distanceToFood = distance
    
    def printCoordinates(self):
        print(f'{self.name} is at {self.x}, {self.y}')

def createGrid():
    pass

def placeFood():
    for i in range(FOOD_NUM):
        food.append((random.randint(MIN_GRID_LENGTH, GRID_LENGTH), random.randint(MIN_GRID_LENGTH,GRID_LENGTH))) # creates food tiles with x and y coordinates

def createSims(): 
    for i in range(SIMS_NUM):
        current_sim = Sim("sim_" + str(i+1))
        sims.append(current_sim)

def placeSims():
    for i in sims:
        i.x = random.randint(MIN_GRID_LENGTH,GRID_LENGTH)
        i.y = random.randint(MIN_GRID_LENGTH,GRID_LENGTH)

def simulateDay():
    placeFood()
    placeSims()
    for i in sims:
        i.printCoordinates()
        i.move()
        i.printCoordinates()
        print("\n")
            
def startSimulation():
    createGrid()
    createSims()
    simulateDay()

# Somehow, name does not equal main in this project when
# if __name__ == "__main__": 
#     startSimulation()

startSimulation()