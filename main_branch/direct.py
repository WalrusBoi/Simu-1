import math
import random
import matplotlib.pyplot as plt

PI = math.pi
FRAME_RATE = 60

class Sim:
    def __init__(self, name):
        self.name = name
        self.x = 0 # positionary variable
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
        def moveForward():
            self.x += round(math.cos(self.angle) * self.movement, 5)
            self.allX.append(self.x)
            self.y += round(math.sin(self.angle) * self.movement, 5)
            self.allY.append(self.y)
        moveForward()

    def angleMath(self):
        if self.angleChange["changing"] == True: # if the angle is currently changing
            print(self.angleChange["finalAngle"], self.angle, self.angleChange["increment"])
            if self.angleChange["increment"] > 0 and self.angle > self.angleChange["finalAngle"]: # if the angle is increasing and the current angle is greater than the final angle    
                self.angleChange["changing"] = False # set the changing angle to false
            elif self.angleChange["increment"] < 0 and self.angle < self.angleChange["finalAngle"]:
                self.angleChange["changing"] = False

        elif self.angleChange["changing"] == False: # if the angle is not changing
            self.angleChange["changing"] = True # change the angle to change
            randomIncrement = ((random.random() * PI) - (PI/2)) # the final angle will be the current angle + or - pi/2
            self.angleChange["increment"] = randomIncrement
            self.angleChange["finalAngle"] = self.angle + randomIncrement # set the final angle to the final angle

        def changeAngle(): 
            if self.angleChange["increment"] > 0:
                self.angle += (PI/120)
            else:
                self.angle -= (PI/120)
        changeAngle()

    def printCoordinates(self):
        print(f'My location is {self.x} and {self.y}')      
        


#TODO implement movement using degrees/radians and NOT up down left right==
testSim = Sim("one")
for i in range(10):
    for j in range(60):
        testSim.move()

print(len(testSim.allX))
plt.plot(testSim.allX, testSim.allY, "ro")
plt.show()