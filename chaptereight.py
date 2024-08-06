class Student:
    name= "Krish Jain"
    age= 18

s1 = Student() 
print(s1.name)
print(s1.age)

s2= Student()
print(s2.name)


class Student:
    college_name = "AVADA KADAVRA"

    def __init__(self, name):
        self.name = name
        print("Adding new student in the database.")


s1 = Student("Krish")
print(s1.name)

s2= Student("Rakazaka")
print(s2.name)


print(s2.college_name)

class Student: 
    @staticmethod
    def college():
        print("ABC College")

# Call the static method
Student.college()

class Car: 
    def __init__(self):
        self.acc = False
        self.brk = False
        self. clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started")

car1= Car()
car1.start()


class Account: 
    def __init__ (self, acc_no, acc_pass):
        self.__acc__no = acc_no
        self.acc__pass = acc_pass


acc1 = Account("12345" , "adgwgw")

print(acc1.acc__no)
print(acc1.__acc_pass)

class Car: 
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
        def __init__(self,name):
            self.name = name 

car1= ToyotaCar("honda")
car2= ToyotaCar("fortuner")

print(car1.color)

class Car: 
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
        def __init__(self,name):
            self.name = name 

car1= ToyotaCar("honda")
car2= ToyotaCar("fortuner")

print(car1.start())


class Car: 
    def __init__(self,type):
         self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
        def __init__(self,name,type):
            self.name = name 
            super().__init__(type)

car1= ToyotaCar("honda", "electric")

print(car1.type)


class Student: 
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


stu1 = Student(98, 97, 96)
print(stu1.percentage)  

stu1.phy = 82
print(stu1.percentage)  


print (1+2)
print("krish" + "jain")
print([1,2,3] + [4,5,6])

class Complex:
    def __init__ (self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__ (self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
    
num1= Complex (1,3)
num1.showNumber()

num2= Complex (4,8)
num2.showNumber()

num3= num1 + num2
num3.showNumber()






      





        









