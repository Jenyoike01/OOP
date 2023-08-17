class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof"
class cat(Animal):
    def speak(self):
        return "Meeeoww"
doggy=Dog("Rottweiler")
cat=cat("Brown")
print(doggy.speak())
print(cat.speak())