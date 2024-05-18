# from car import carclass # 1 способ
from lesson_1.car.carclass import CarClass  # если в двух папках, то указываем две папки от корня через точку


# class ElectroCar(carclass.CarClass): # 1 способ
class ElectroCar(CarClass):
    def __init__(self, brand, model, year, run):
        super().__init__(brand, model, year, run)
        self.battery = 100

    def description_battery(self):
        print(f"Этот автомобиль имеет мощность {self.battery} %")
