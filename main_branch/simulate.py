class Parent:

    def __init__(self, item, model):
          self.item = item
          self.model = model
    def sayHello(self):
       print("hello world!")

class child(Parent):
   
   def __init__(self, item, model):
       Parent.__init__(self, item, model)

       print(item)  # I am able to get this value

   def example(self): 

       value = self.item * 10 # This item is not able to access and throughs an error.

       print(value)

foo = child(10, "jet engine")
foo.sayHello()