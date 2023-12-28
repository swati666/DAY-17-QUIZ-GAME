# NOTES- ATTRIBUTES ARE THE THINGS THAT THE OBJECT HAS and An ATTRIBUTE ia a variable associated with objects.
# TODO- Create a class name car and its object named User_1
class Car:
    pass

# Notes- It is the object of the class Car()
user_1 = Car()


# TODO- Create another class and demonstrate its constructor
class CarOfConstructor:
    def __init__(self, name, mileage):
    # NOTES-  self is the actual object that will being created or being INTIALIZED for the class
    #  named CarOfConstructor(example) here in this case.
    #  1. self will be apllied to the every constructor create by the class
    #  2. and will be called acutomatically on the creation of the objects.
    #  3. __init__ function is used to initialise attributes of objects or variables of class.

        self.user_name = name

    # notes In addition you can add as many Parameters as you want and pass name and
    #  that parameter is going to be passed in when an object gets constructed from repected class.
    #  And once you receive that data, then you can use it to set the object's attributes.

        self.mileage = mileage
    #  notes- for example here mileage will be attach with every constructor

        self.speed = 0
        # notes- for such variables we dont need to mention them in the parameters of the class
        #  because they are dynamic in nature and will change everytime with the excecution of the class.


car_constructor = CarOfConstructor("Ferrari", '8.77KM/L')
print(car_constructor.user_name)
print(car_constructor.mileage)
print(car_constructor.speed)

# notes-- PARAMETERS are mandatory for the every constructors that will be created under the class.

# TODO- CREATE A RaceCar class and demonstrate methods under it.

# NOTES-- METHODS IS WORK THAT AN OBJECT CAN DO.
#  When a function attached with an object is called an METHOD

class Racecar:
    def __init__(self):
        self.seats = 4
    def race_mode(self):
        self.seats = 2



my_race_car = Racecar()
print("Number of seats before racing mode: ", my_race_car.seats)
# notes-- console output: Numbers of seats after car came into race mode: 4

my_race_car.race_mode()
print(f"Numbers of seats after car came into race mode: {my_race_car.seats}")
# notes-- console output: Numbers of seats after car came into race mode: 2
#  clearly you can see the difference that method race mode did to the object
