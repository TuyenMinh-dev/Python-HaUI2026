class Car:
    def __init__(self, name, brand, color):
        self.name = name
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"You are driving a {self.name} car, it is {self.color} and a {self.brand}'s car")  

kiaMorning = Car("KIA Morning","KIA","blue")
kiaMorning.drive()
ferrariTributo = Car("Ferarri F8 Tributo","Ferrari","red")
ferrariTributo.drive()