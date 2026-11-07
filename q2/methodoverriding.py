#The parent class
class Animal:
  def __init__(self,name):
    self.name = name

  def eat(self): #This defines the eat method
    print(self.name, "is currently eating")

  def make_sound(self): #This defines the make_sound method
    print(self.name, "produces a sound")
    
class Lion (Animal):

  def eat(self): #This defines the eat method for the lion class #Overrides eat method
    print(self.name, "eats fresh meat")

  def make_sound(self): #This defines the make_sound method for the lion class #Overrides make_sound method
    print(self.name, "roars loudly")

class Elephant(Animal):

  def eat(self): #This defines the eat method for the elephant class #Overrides eat method
    print(self.name, "eats grass and fruits")

  def make_sound(self): #This defines the make_sound method for the elephant class #Overrides make_sound method
    print(self.name, "trumpets") 

class Monkey(Animal):

  def eat(self): #This defines the eat method for the monkey class #Overrides eat method
    print(self.name, "eats bananas")

  def make_sound(self): #This defines the make_sound method for the monkey class #Overrides make_sound method
  print(self.name, "chatters")

#Objects of each animal
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

#Calling eat and make_sound methods for lion
print(lion.make_sound())
print(lion.eat())
print("------")

#Calling eat and make_sound methods for elephant
print(elephant.make_sound())
print(elephant.eat())
print("------")

#Calling eat and make_sound methods for monkey
print(monkey.make_sound())
print(monkey.eat())
print("------")
