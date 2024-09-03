import math
import random
import matplotlib.pyplot as plt

PI = math.pi
FRAME_RATE = 60
GRID_LENGTH = 10
MIN_GRID_LENGTH = -GRID_LENGTH

current_food = (3, 4)
class Sim:
    def __init__(self, name):
        self.name = name
        self.x = 9.8 # positionary variable
        self.y = 0 # ^
        self.angle = 0
        self.angleChange = {
            "finalAngle" : None,
            "changing" : False,
            "increment" : None
        } 
        self.movement = 1.5/FRAME_RATE
        self.allX = []
        self.allY = []
    def move(self):
        self.angleMath()

        def moveTowardsFood(): # moves the sim towards the nearest food tile if one is located
            # self.locateClosestFood() # calls the food function   
            if self.range >= self.distanceToFood: # in range to spot food
                distance_x = (self.x - current_food[0]) 
                distance_y = (self.y - current_food[1])
                new_angle = math.atan2(distance_y, distance_x) # finds the nearest angle (in degrees)
                print(new_angle, "THIS IS THE NEW ANGLE")
                if self.distanceToFood <= self.movement*2: # if the speed (movement per turn) is greater than the distance to the food, it can eat
                    pass
            #         howMuchFood = 1
            #         self.foodAte += howMuchFood
            #         for i in range(howMuchFood):
            #             print(self.closestFoodBlender.location)
            #             bpy.data.objects.remove(self.closestFoodBlender.blenderID)
            #             food.remove(self.closestFoodBlender) # removes every instance of the food that was just ate
            #         self.locateClosestFood()
            

                else:
                    distance = math.sqrt(((self.x - self.closestFood[0])**2) + ((self.y - self.closestFood[1])**2))                                 
                    if distance >= self.movement: # if the distance from the object is more than the eating range
                        pass
                        # self.angle = 
                        # if distance_x > 0:
                        #     moveLeft()
                        # else:
                        #     moveRight()

                    # elif abs(distance_y) >= self.movement: # if the distance from the object is more than the eating range
                    #     if distance_y > 0:
                    #         moveDown()
                    #     else:
                    #         moveUp()
                        
                    else:
                        print("there has been a serious error, investigate")
                        print(self.closestFood)
                        print(self.distanceToFood)
                self.updateLocation()
                self.energy -= self.energyPerTurn
            else: 
                moveForward()
        
        def moveForward():
            self.printAngleInfo()
            if not self.checkValidity():
                self.angle += PI
                self.angleChange["finalAngle"] += PI
                print("changed")
            self.x += round(math.cos(self.angle) * self.movement, 5)
            self.allX.append(self.x)
            self.y += round(math.sin(self.angle) * self.movement, 5)
            self.allY.append(self.y)
        moveForward()

    def angleMath(self):
        if self.angleChange["changing"] == True: # if the angle is currently changing           
            if self.angleChange["increment"] > 0 and self.angle > self.angleChange["finalAngle"]: # if the angle is increasing and the current angle is greater than the final angle    
                self.angleChange["changing"] = False # set the changing angle to false
            elif self.angleChange["increment"] < 0 and self.angle < self.angleChange["finalAngle"]:
                self.angleChange["changing"] = False

        elif self.angleChange["changing"] == False: # if the angle is not changing
            print("actively changing angle")
            self.angleChange["changing"] = True # change the angle to change
            randomIncrement = ((random.random() * PI) - (PI/2)) # the final angle will be the current angle + or - pi/2
            self.angleChange["increment"] = randomIncrement
            self.angleChange["finalAngle"] = self.angle + randomIncrement # set the final angle to the final angle

        def changeAngle(): 
            if self.angleChange["increment"] > 0:
                self.angle += (PI/(FRAME_RATE*2))
            else:
                self.angle -= (PI/(FRAME_RATE*2))
        changeAngle()
    
    def checkValidity(self): # Checks to see if the sims location is on the grid
        if self.x > GRID_LENGTH or self.y > GRID_LENGTH or self.x <  MIN_GRID_LENGTH or self.y < MIN_GRID_LENGTH: 
            return False # returns False if off grid
        return True # returns True if on grid


    def printCoordinates(self): # debug tool
        print(f'My location is {self.x} and {self.y}')    

    def printAngleInfo(self): # debug tool
        print(f'Current angle: {self.angle}, Final angle: {self.angleChange["finalAngle"]}, increment: {self.angleChange["increment"]}')  


testSim = Sim("one")
for i in range(10):
    for j in range(100):
        testSim.move()

print(len(testSim.allX))
plt.plot(testSim.allX, testSim.allY, "ro")
plt.show()