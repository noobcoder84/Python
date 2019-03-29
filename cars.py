class Cars:
    
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def car_details(self):
        return '{}\n{}\n{}'.format(self.name, self.model, self.year)
        #print(self.name, self.model, self.year)

new_car = Cars('bmw', 'x5', 2019)
print(new_car.car_details())
#new_car.car_details()


