food = []

class Food:
    def __init__(self, location, name, blenderID):
        self.location = location
        self.name = name
        self.blenderID = blenderID

b = 0
for i in range(10):
    a = Food((3,7), i, "j")
    food.append(a)
    b = a

print(b.name)

print(food.remove(b))
print(food[-1].name)
