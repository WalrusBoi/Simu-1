import random
import sys

GRID_LENGTH = 10 # self explanatory
MIN_GRID_LENGTH = GRID_LENGTH*-1
SIMS_NUM = 100 # amount of sims
FOOD_NUM = 2 # amount of food
CUBE_SIZE = 0.5
sims = [] # list full of the sims
food = []

class Sim:
    def __init__(self, name):
        self.name = name
        self.x = 0 # positionary variable
        self.y = 0 # ^
        self.energy = 10 # energy allows the sims to move
        self.movement = 1 # speed allows the sims to 
        self.range = 5
        self.closestFood = ()
        self.distanceToFood = 0

    def checkValidity(self): # Checks to see if the sims location is on the grid
        if self.x > GRID_LENGTH or self.y > GRID_LENGTH or self.x <  MIN_GRID_LENGTH or self.y < MIN_GRID_LENGTH:
            return False
        return True

    def move(self): # Movement function split into nested functions which involves all movement capabilities. Using this function is the only way to access sim movement
        def moveUp():
            self.y += self.movement
        def moveDown():
            self.y -= self.movement
        def moveLeft():
            self.x -= self.movement
        def moveRight():
            self.x += self.movement

        def moveRandomly(): # moves the sim in a random
            randInt = random.randint(1,4) # sets a random integer to allow the sim to move in a random direction
            match randInt:
                case 1:
                    moveUp()
                case 2:
                    moveDown()
                case 3:
                    moveLeft()
                case 4:
                    moveRight()

        self.locateClosestFood() # calls the food function      
        if self.range >= self.distanceToFood: # in range to spot food
            if self.distanceToFood <= 1.5:
                # TO DO: IMPLEMENT eatFood()
                # eatFood()
                pass
            else:
                distance_x = self.x - self.closestFood[0]
                distance_y = self.y - self.closestFood[1]
        else: 
            moveRandomly()

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
        print(i.x, i.name)
        i.move()
        print(i.x, i.name)
            
def startSimulation():
    createGrid()
    createSims()
    simulateDay()

# Somehow, name does not equal main in this project when
# if __name__ == "__main__": 
#     startSimulation()

startSimulation()