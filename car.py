class Car:
    def __init__(self, speed):
        self.__speed = speed
    
    def get_speed(self):
        return self.__speed

    def set_name(self, speed):
        self.__speed = speed

    def get_age(self):
        return self.__speed

    def set_age(self, speed):
        self.__speed = speed

    def get_all_info(self):
        return [self.__speed]
car1 = Car(240)
print(car1.get_all_info())
