# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Привет, меня зовут {self.name}, мне {self.age} лет")

#     def is_adult(self):
#         if self.age >= 18:
#             return True
#         else:
#             return False
    
#     def birthday(self):
#         self.age += 1
#         print(f"С днём рождения! Теперь мне {self.age} лет")

        

# user1 = User("Алексей", 25)
# user2 = User("Мария", 16)

# user1.greet()
# print(user1.is_adult())

# user1.birthday()
# user2.birthday()


# class Worker(User):   # Worker наследует всё от User
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)  # вызываем конструктор родителя
#         self.salary = salary
    
#     def work(self):
#         print(f"{self.name} работает за {self.salary} рублей")

# # Используем
# worker = Worker("Иван", 30, 50000)
# worker.greet()     # Привет, меня зовут Иван, мне 30 лет (метод из User)
# worker.work()      # Иван работает за 50000 рублей (новый метод)


class Vehicle:
    vehicles_created = 0 
    def __init__(self, brand, max_speed):
        self.brand = brand
        self._max_speed = max_speed
        self._mileage = 0
        Vehicle.vehicles_created += 1

    def get_max_speed(self):
        return self._max_speed
    
    def get_mileage(self):
        return self._mileage
    
    def drive(self, distance):
        self._mileage += distance
    
    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Макс. скорость: {self._max_speed} км/ч")
        print(f"Пробег: {self._mileage} км")

class Car(Vehicle):
    def __init__(self, brand, max_speed, engine_type) -> None:
        super().__init__(brand, max_speed)
        self.engine_type = engine_type

    def display_info(self):
        super().display_info()
        print(f"Тип двигателя: {self.engine_type}")

class Bicycle(Vehicle):
    def __init__(self, brand, max_speed, frame_matetial) -> None:
        super().__init__(brand, max_speed)
        self.frame_material = frame_matetial

    def display_info(self):
        super().display_info()
        print(f"Материал рамы: {self.frame_material}")
class Vehicle:
    vehicles_created = 0 
    def __init__(self, brand, max_speed) -> None:
        self.brand = brand
        self._max_speed = max_speed
        self._mileage = 0
        Vehicle.vehicles_created += 1

    def get_max_speed(self):
        return self._max_speed
    
    def get_mileage(self):
        return self._mileage
    
    def drive(self, distance):
        self._mileage += distance
    
    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Макс. скорость: {self._max_speed} км/ч")
        print(f"Пробег: {self._mileage} км")

class Car(Vehicle):
    def __init__(self, brand, max_speed, engine_type) -> None:
        super().__init__(brand, max_speed)
        self.engine_type = engine_type

    def display_info(self):
        super().display_info()
        print(f"Тип двигателя: {self.engine_type}")

class Bicycle(Vehicle):
    def __init__(self, brand, max_speed, frame_matetial) -> None:
        super().__init__(brand, max_speed)
        self.frame_material = frame_matetial

    def display_info(self):
        super().display_info()
        print(f"Материал рамы: {self.frame_material}")

# Создаем объекты разных классов
tesla = Car("Tesla", 250, "Электро")
bmw = Car("BMW", 280, "Бензин")
trek = Bicycle("Trek", 40, "Карбон")

# Демонстрируем полиморфизм: работаем с разными объектами через общий интерфейс
vehicles = [tesla, bmw, trek]
for vehicle in vehicles:
    print("---")
    vehicle.display_info() # Один и тот же вызов - разное поведение
    vehicle.drive(100)
    print(f"Пробег после поездки: {vehicle.get_mileage()} км")

print("\n" + "="*30)
# Демонстрируем работу атрибута класса
print(f"Всего создано транспортных средств: {Vehicle.vehicles_created}")



