class A:
    def __init__(self, name, junk, pjunk):
        self.name = name
        self.junk = junk
        self.pjunk = pjunk

class B(A):
    def __init__(self, junk):
        super().__init__("B")
        print("B's __init__ my name is ", self.name)