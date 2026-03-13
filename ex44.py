
class Vehicle:
    def __init__(self, brand:str , model:str):
        self.brand = brand
        self.model = model
    
    def Description(self)->str:
        return self.brand + " " + self.model
    
class Car(Vehicle):
    def __init__(self, brand,model,numDoors:int):

        self.numDoors = numDoors
        super().__init__(brand, model)

    def Description(self)->str:
        return self.brand + " " + self.model + " " + str(self.numDoors)

car = Car("bmw","serie3",3)
print(car.Description())