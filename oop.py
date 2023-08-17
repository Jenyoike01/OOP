class Students:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

     def sayhello(self):
        print("My name is", self.name, "Im", self.age, "years", self.gender)

myobje = Students("Jeremy", "Male", 20)
myobje.sayhello()
