class Car:
    def __init__(self, speed):
        self.__speed = speed
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, speed):
        self.__speed = speed

car1=Car(2000)
print(car1.get_speed())