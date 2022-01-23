#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    # By convention all the methods in the class take the reference to the object as the first parameter
    # (usually named 'self')
    def __init__(self, bodystyle):  # <== This is just like a constructor for a class
        self.bodystyle = bodystyle
        self.body = True

    def drive(self, speed):  # <== A method
        self.mode = "driving"
        self.speed = speed


class Car(Vehicle):
    def __init__(self, enginetype, type):
        # super keyword is used to inherit all the properties of the parent's class
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype
        self.type = type

    def drive(self, speed):  # <== Method Overriding
        super().drive(speed)
        print(self.mode, "my", self.type, self.enginetype,
              self.bodystyle, "at", self.speed)


class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print(self.mode, "my", self.enginetype,
              self.bodystyle, "at", self.speed)


class Wood():
    def __init__(self):
        self.body = "It has one"


class Chair(Wood):
    def __init__(self, worker):
        Wood.__init__(self)   # To access the attribute of the parent class
        self.worker = worker


car1 = Car("gas", "Limosine")
car2 = Car("electric", "hatchback")
mc1 = Motorcycle("gas", True)

# print(mc1.wheels)
# print(mc1.bodystyle)
# print(car1.enginetype)
# print(car2.doors)

# car1.drive(30)
# car2.drive(40)
# mc1.drive(50)

# print(car1.type)

wood1 = Chair("Mazdoor")

print(wood1.worker, wood1.body)
