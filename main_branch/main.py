import random
import sys
import bpy


# Deselect all objects
bpy.ops.object.select_all(action='DESELECT')

# Select all objects
bpy.ops.object.select_all(action='SELECT')

# Delete selected objects
bpy.ops.object.delete()

GRID_LENGTH = 10 # self explanatory
MIN_GRID_LENGTH = GRID_LENGTH*-1
SIMS_NUM = 100 # amount of sims
FOOD_NUM = 25 # amount of food
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
        self.blenderID = 0

    def move(self):
        def moveUp(self):
            self.y += self.movement
        def moveDown(self):
            self.y -= self.movement
        def moveLeft(self):
            self.x -= self.movement
        def moveRight(self):
            self.x += self.movement
        
        def checkValidity():
            if self.x > GRID_LENGTH or self.y > GRID_LENGTH or self.x <  MIN_GRID_LENGTH or self.y < MIN_GRID_LENGTH:
                return False
            return True

        if self.range >= self.distanceToFood:
            if self.distanceToFood <= 1.5:
                # TO DO: IMPLEMENT eatFood()
                # eatFood()
                pass
            else:
                distance_x = self.x - self.closestFood[0]
                distance_y = self.y - self.closestFood[1]
                #if 

    def locateClosestFood(self):
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
    bpy.ops.mesh.primitive_grid_add(size=GRID_LENGTH*2)

def placeFood():
    for i in range(FOOD_NUM):
        food.append((random.randint(MIN_GRID_LENGTH, GRID_LENGTH), random.randint(MIN_GRID_LENGTH,GRID_LENGTH))) # creates food tiles with x and y coordinates

def createSims(): 
    for i in range(SIMS_NUM):
        current_sim = Sim("sim_" + str(i+1))
        bpy.ops.mesh.primitive_cube_add(size=CUBE_SIZE)
        current_sim.blenderID = bpy.context.object
        current_sim.blenderID.name = current_sim.name
        sims.append(current_sim)


def placeSims():
    for i in sims:
        i.x = random.randint(MIN_GRID_LENGTH,GRID_LENGTH)
        i.y = random.randint(MIN_GRID_LENGTH,GRID_LENGTH)
        i.blenderID.location = (i.x, i.y, (CUBE_SIZE/2))

def simulateDay():
    placeFood()
    placeSims()
            
def startSimulation():
    createGrid()
    createSims()
    simulateDay()

# Somehow, name does not equal main in this project when
# if __name__ == "__main__": 
#     startSimulation()

startSimulation()