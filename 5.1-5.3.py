# def create_car(color, consumption, tank_volume, mileage=0):
#     return {
#         "color": color,
#         "consumption": consumption,
#         "tank_volume": tank_volume,
#         "reserve": tank_volume,
#         "mileage": mileage,
#         "engine_on": False
#     }

# def start_engine(car):
#    if not car["engine_on"] and car["reserve"] > 0:
#        car["engine_on"] = True
#        return "Двигатель запущен."
#    return "Двигатель уже был запущен."

# def stop_engine(car):
#    if car["engine_on"]:
#        car["engine_on"] = False
#        return "Двигатель остановлен."
#    return "Двигатель уже был остановлен."

# def drive(car, distance):
#    if not car["engine_on"]:
#        return "Двигатель не запущен."
#    if car["reserve"] / car["consumption"] * 100 < distance:
#        return "Малый запас топлива."
#    car["mileage"] += distance
#    car["reserve"] -= distance / 100 * car["consumption"]
#    return f"Проехали {distance} км. Остаток топлива: {car['reserve']} л."

# def refuel(car):
#    car["reserve"] = car["tank_volume"]

# def get_mileage(car):
#    return f"Пробег {car['mileage']} км."

# def get_reserve(car):
#    return f"Запас топлива {car['reserve']} л."

# car_1 = create_car(color="black", consumption=10, tank_volume=55)

# print(start_engine(car_1))
# print(drive(car_1, 100))
# print(drive(car_1, 100))
# print(drive(car_1, 100))
# print(drive(car_1, 300))
# print(get_mileage(car_1))
# print(get_reserve(car_1))
# print(stop_engine(car_1))
# print(drive(car_1, 100))

# ===================================================================
# Это процедурный код, функциями, ниже будем переделывать с ООП


# class Car:
#     pass


# Метод объявляется с помощью ключевого слова def, а первым его параметром всегда 
# идёт self. Это ссылка на конкретный объект, для которого вызывается метод:

# def start_engine(self):
    # ...
# С помощью self метод может обращаться к атрибутам и другим методам того же объекта. 
# Без self объект не сможет «узнать» собственные свойства.

# class Car:

#     def __init__(self, color, consumption, tank_volume, mileage=0):
#         self.color = color
#         self.consumption = consumption
#         self.tank_volume = tank_volume
#         self.reserve = tank_volume
#         self.mileage = mileage
#         self.engine_on = False

#     def start_engine(self):
#         if not self.engine_on and self.reserve > 0:
#             self.engine_on = True
#             return "Двигатель запущен."
#         return "Двигатель уже был запущен."
    
#     def stop_engine(self):
#         if self.engine_on:
#             self.engine_on = False
#             return "Двигатель остановлен."
#         return "Двигатель уже был остановлен."
    
#     def drive(self, distance):
#         if not self.engine_on:
#             return "Двигатель не запущен."
#         if self.reserve / self.consumption * 100 < distance:
#             return "Малый запас топлива."
#         self.mileage += distance
#         self.reserve -= distance / 100 * self.consumption
#         return f"Проехали {distance} км. Остаток топлива: {self.reserve}"
    
#     def refuel(self):
#         self.reserve = self.tank_volume

#     def get_mileage(self):
#         return self.mileage
    
#     def get_reserve(self):
#         return self.reserve
    
#     def get_consumption(self):
#         return self.consumption
    
# class ElectricCar:

#     def __init__(self, color, consumption, bat_capacity, mileage=0):
#         self.color = color
#         self.consumption = consumption
#         self.tank_volume = bat_capacity
#         self.reserve = bat_capacity
#         self.mileage = mileage
#         self.engine_on = False

#     def start_engine(self):
#         if not self.engine_on and self.reserve > 0:
#             self.engine_on = True
#             return "Двигатель запущен."
#         return "Двигатель уже был запущен."
    
#     def start_engine(self):
#         if not self.engine_on and self.reserve > 0:
#             self.engine_on = True
#             return "Двигатель запущен."
#         return "Двигатель уже был запущен."

#     def stop_engine(self):
#         if self.engine_on:
#             self.engine_on = False
#             return "Двигатель остановлен."
#         return "Двигатель уже был остановлен."

#     def drive(self, distance):
#         if not self.engine_on:
#             return "Двигатель не запущен."
#         if self.reserve / self.consumption * 100 < distance:
#             return "Малый заряд батареи."
#         self.mileage += distance
#         self.reserve -= distance / 100 * self.consumption
#         return f"Проехали {distance} км. Остаток заряда: {self.reserve} кВт*ч."

#     def recharge(self):
#         self.reserve = self.bat_capacity

#     def get_mileage(self):
#         return self.mileage

#     def get_reserve(self):
#         return self.reserve

#     def get_consumption(self):
#         return self.consumption


# def range_reserve(car):
#     return car.get_reserve() / car.get_consumption() * 100
    


# car_1 = Car(color="black", consumption=10, tank_volume=55)
# car_2 = ElectricCar(color="white", consumption=15, bat_capacity=90)
# print(f"Запас хода: {range_reserve(car_1)} км.")
# print(f"Запас хода: {range_reserve(car_2)} км.")

# import math

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy

#     def length(self, other):
#         distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
#         return round(distance, 2)
    

# first_point = Point(2, -7)
# second_point = Point(7, 9)
# print(first_point.length(second_point))
# print(second_point.length(first_point))


# class RedButton:
    
#     def __init__(self):
#         self.counter = 0

#     def click(self):
#         self.counter += 1
#         print("Тревога!")
    
#     def count(self):
#         return self.counter
    

# first_button = RedButton()
# second_button = RedButton()
# print(first_button.click())
# print(first_button.count(), second_button.count())
        

# class Lamp:

#     def __init__(self):
#         self.state = False
#         self.click = 0

#     def toggle(self):
#         self.click += 1
#         if self.state:
#             self.state = False
#             return "Лампа погасла"
#         else:
#              self.state = True
#              return "Лампа зажглась"
        
    
#     def is_on(self):
#         return self.state
    
#     def click_count(self):
#         return self.click
    

# lamp1 = Lamp()
# lamp2 = Lamp()

# print(lamp1.toggle())   # Лампа зажглась
# print(lamp1.toggle())   # Лампа погасла
# print(lamp2.toggle())   # Лампа зажглась

# print(lamp1.is_on())    # False
# print(lamp2.is_on())    # True
# print(lamp1.click_count())  # 2
# print(lamp2.click_count())  # 1


# class Safe:

#     def __init__(self, code = 1234):
#         self.secret_code = code
#         self.attempts = 0

#     def open(self, code):
#         if code == self.secret_code:
#             self.attempts = 0
#             return "Сейф открыт"
#         else:
#             self.attempts += 1
#             return (f"Неверный код. Попыток: {self.attempts}")
    
#     def reset_attempts(self):
#         self.attempts = 0
    
#     def get_attempts(self):
#         return self.attempts

# safe = Safe(1234)

# print(safe.open(1111) )  # Неверный код. Попыток: 1
# print(safe.open(2222))   # Неверный код. Попыток: 2
# print(safe.open(1234))   # Сейф открыт

# safe.open(5678)   # Неверный код. Попыток: 1 (счётчик сбросился после успешного открытия)

# print(safe.get_attempts())  # 1
# safe.reset_attempts()
# print(safe.get_attempts())  # 0


# class TrafficLight:

#     def __init__(self):
#         self.states = ["Красный", "Жёлтый", "Зелёный", "Жёлтый"]
#         self.index = 0
#         self.counter = 0

#     def next(self):
#         self.counter += 1
#         self.index = (self.index + 1) % len(self.states)
#         return self.states[self.index]
    
#     def current(self):
#         return self.states[self.index]

#     def switch_count(self):
#         return self.counter
    
#     def reset(self):
#         self.index = 0
#         self.counter = 0
#         return "Светофор сброшен"




# light = TrafficLight()

# print(light.current())        # Красный

# print(light.next())           # Жёлтый
# print(light.next())           # Зелёный
# print(light.next())           # Жёлтый
# print(light.next())           # Красный

# print(light.switch_count())   # 4
# print(light.current())        # Красный
# print(light.reset())
# print(light.switch_count())
        
# class Programmer:
#     _base_salaries = {
#         'Junior': 10,
#         'Middle': 15,
#         'Senior': 20
#     }

#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#         self.hours = 0
#         self.total_pay = 0
#         self._rise_count = 0

#     @property
#     def current_rate(self):
#         if self.position == 'Senior':
#             return self._base_salaries['Senior'] + self._rise_count
#         return self._base_salaries[self.position]

#     def work(self, time):
#         self.hours += time
#         self.total_pay += time * self.current_rate

#     def rise(self):
#         if self.position == 'Junior':
#             self.position = 'Middle'
#         elif self.position == 'Middle':
#             self.position = 'Senior'
#         elif self.position == 'Senior':
#             self._rise_count += 1

#     def info(self):
#         return f"{self.name} {self.hours}ч. {self.total_pay}тгр."


# programmer = Programmer('Васильев Иван', 'Junior')
# programmer.work(750)
# print(programmer.info())
# programmer.rise()
# programmer.work(500)
# print(programmer.info())
# programmer.rise()
# programmer.work(250)
# print(programmer.info())
# programmer.rise()
# programmer.work(250)
# print(programmer.info())


# >================================================================================>
# 5.2

# class Pencil:

#     def __init__(self, color="серый"):
#         self.color = color

#     def draw_picture(self):
#         return f"Нарисован рисунок цветом '{self.color}'."

# class Pen(Pencil):

#     def sign_document(self):
#         if self.color not in ("синий", "чёрный", "фиолетовый"):
#             return f"Ручкой цвета '{self.color}' нельзя подписать документ."
#         return f"Подписан документ."

# blue_pen = Pen(color="синий") 
# print(blue_pen.draw_picture()) Нарисован рисунок цветом 'синий'.
# print(blue_pen.sign_document()) Подписан документ.
# red_pen = Pen(color="красный")
# print(red_pen.draw_picture()) Нарисован рисунок цветом 'красный'.
# print(red_pen.sign_document()) Ручкой цвета 'красный' нельзя подписать документ.

# class GreetingFormal:

#     def __init__(self):
#         self.formal_greeting = "Добрый день,"

#     def greet_formal(self, name):
#         return f"{self.formal_greeting} {name}!"

# class GreetingInformal:

#     def __init__(self):
#         self.informal_greeting = "Привет,"

#     def greet_informal(self, name):
#         return f"{self.informal_greeting} {name}!"

# class GreetingMix(GreetingFormal, GreetingInformal):

#     def __init__(self):
#         GreetingFormal.__init__(self)
#         GreetingInformal.__init__(self)

# mixed_greeting = GreetingMix()
# print(mixed_greeting.greet_formal("Пользователь"))
# print(mixed_greeting.greet_informal("Пользователь"))


# class Car:

#     def __init__(self, color, consumption, tank_volume, mileage=0):
#         self.color = color
#         self.consumption = consumption
#         self.tank_volume = tank_volume
#         self.reserve = tank_volume
#         self.mileage = mileage
#         self.engine_on = False

#     def start_engine(self):
#         if not self.engine_on and self.reserve > 0:
#             self.engine_on = True
#             return "Двигатель запущен."
#         return "Двигатель уже был запущен."

#     def stop_engine(self):
#         if self.engine_on:
#             self.engine_on = False
#             return "Двигатель остановлен."
#         return "Двигатель уже был остановлен."

#     def drive(self, distance):
#         if not self.engine_on:
#             return "Двигатель не запущен."
#         if self.reserve / self.consumption * 100 < distance:
#             return "Малый запас топлива."
#         self.mileage += distance
#         self.reserve -= distance / 100 * self.consumption
#         return f"Проехали {distance} км. Остаток топлива: {self.reserve} л."

#     def refuel(self):
#         self.reserve = self.tank_volume

#     def get_mileage(self):
#         return self.mileage

#     def get_reserve(self):
#         return self.reserve

#     def get_consumption(self):
#         return self.consumption

# class ElectricCar(Car):

#     def __init__(self, color, consumption, bat_capacity, mileage=0):
#         super().__init__(color, consumption, bat_capacity, mileage)
#         self.bat_capacity = bat_capacity

#     def drive(self, distance):
#         if not self.engine_on:
#             return "Двигатель не запущен."
#         if self.reserve / self.consumption * 100 < distance:
#             return "Малый запас заряда."
#         self.mileage += distance
#         self.reserve -= distance / 100 * self.consumption
#         return f"Проехали {distance} км. Остаток заряда: {self.reserve} кВт*ч."

#     def recharge(self):
#         self.reserve = self.bat_capacity

#     def __str__(self):
#         return f"Электромобиль. " \
#                f"Цвет: {self.color}. " \
#                f"Пробег: {self.mileage} км. " \
#                f"Остаток заряда: {self.reserve} кВт*ч."



# electric_car = ElectricCar(color="white", consumption=15, bat_capacity=90)
# print(electric_car.start_engine())
# print(electric_car.drive(100))
# print(electric_car)


# class A:

#     def __init__(self):
#         self.value = 10

#     def __add__(self, other):
#         return "Выполняется метод __add__."

#     def __radd__(self, other):
#         return "Выполняется метод __radd__."

#     def __iadd__(self, other):
#         self.value += other
#         return self

#     def __str__(self):
#         return f"value: {self.value}."
        
# a = A()
# print(a + 1)
# print(1 + a)
# a += 1
# print(a)


# def create_book_class():
#     class Book:
#         def __init__(self, title, author, pages): self.title, self.author, self.pages = title, author, pages
#         def get_info(self): return f"'{self.title}' by {self.author}, {self.pages} pages"
    # return Book

# class Logger():
#     def log(self, message):
#          return f"[LOG]: {message}"

# class TimestampLogger(Logger):
#      def log(self, message):
#         return f"{super().log(message)} (timestamp)"
    
# # Создаём объект обычного логгера
# simple_logger = Logger()
# print(simple_logger.log("Запуск программы"))
# # Вывод: [LOG]: Запуск программы

# # Создаём объект логгера с временной меткой
# timestamp_logger = TimestampLogger()
# print(timestamp_logger.log("Пользователь вошёл в систему"))
# # Вывод: [LOG]: Пользователь вошёл в систему (timestamp)

# # Можно сохранять результаты в переменные
# msg1 = simple_logger.log("Ошибка подключения")
# msg2 = timestamp_logger.log("Данные сохранены")

# print("Обычный логгер:", msg1)
# print("Логгер с timestamp:", msg2)

# # Несколько вызовов подряд
# print(timestamp_logger.log("Шаг 1"))
# print(timestamp_logger.log("Шаг 2"))
# print(timestamp_logger.log("Шаг 3"))


# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def start_engine(self):
#         return 'Двигатель запущен'
    
#     def honk(self):
#         return 'Общий сигнал!'
    
# class Car(Vehicle):
#     def start_engine(self):
#         super().start_engine()
#         return "Двигатель запущен... Проверка систем автомобиля."

#     def honk(self):
#         return "Би-бип!"

# # === Проверка ===
# my_car = Car("Tesla")

# print("Марка:", my_car.brand)              # Tesla
# print("Сигнал:", my_car.honk())            # Би-бип!
# print("Запуск:", my_car.start_engine())    # Двигатель запущен... Проверка систем автомобиля.

# # Проверка родительского honk (через super(), если нужно)
# print("Родительский сигнал:", super(Car, my_car).honk())  # Общий сигнал!


# class Product():
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class DiscountedProduct(Product):
#     def __init__(self, name, price, discount):  # ← принимаем все параметры
#         super().__init__(name, price)            # ← передаём name и price родителю
#         self.discount = discount                 # ← добавляем новый атрибут

#     def get_price_with_discount(self):
#         return self.price - (self.price * self.discount / 100)

# item = DiscountedProduct("Мышь", 1500, 15)
# print(f"Товар: {item.name}, Цена: {item.price}, Скидка: {item.discount}%")


# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Cat(Animal):
#     def meow(self):
#         print("Мяу!")

# class Dog(Animal):
#     def bark(self):
#         print("Гав!")

# # Создаем объекты
# generic_animal = Animal("Нечто")
# cat = Cat("Барсик")
# dog = Dog("Рекс")

# # --- Проверяем собаку ---
# print("--- Проверяем Рекса (объект Dog) ---")
# print(f"Рекс является экземпляром Dog?     {isinstance(dog, Dog)}")     # True
# print(f"Рекс является экземпляром Animal?   {isinstance(dog, Animal)}")   # True (!!!)
# print(f"Рекс является экземпляром Cat?      {isinstance(dog, Cat)}")      # False

# # --- Проверяем кошку ---
# print("\n--- Проверяем Барсика (объект Cat) ---")
# print(f"Барсик является экземпляром Cat?    {isinstance(cat, Cat)}")     # True
# print(f"Барсик является экземпляром Animal? {isinstance(cat, Animal)}") # True

# # --- Проверяем простое животное ---
# print("\n--- Проверяем Нечто (объект Animal) ---")
# print(f"Нечто является экземпляром Animal? {isinstance(generic_animal, Animal)}") # True
# print(f"Нечто является экземпляром Dog?    {isinstance(generic_animal, Dog)}")    # False

# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
    
#     # --- Вот и наша "магия" ---
#     def __str__(self):
#         # Мы сами решаем, как будет выглядеть наш объект в виде строки.
#         # Этот метод должен ВЕРНУТЬ строку, а не напечатать ее!
#         return f"Пользователь {self.username} (email: {self.email})"

# # Создаем экземпляр класса
# user_alex = User("Alex", "alex@example.com")
# user_maria = User("Maria", "maria@stepik.org")

# # Теперь `print()` будет работать так, как мы хотим!
# print(user_alex)
# print(user_maria)

# # Функция str() тоже будет использовать наш метод
# user_string = str(user_alex)
# print(f"\nРезультат вызова str(): {user_string}")


# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
    
#     # 1. Сначала пишем __repr__ для разработчиков.
#     def __repr__(self):
#         return f"Car(model={self.model!r}, color={self.color!r})"
        
#     # 2. Затем добавляем __str__ для красивого вывода.
#     def __str__(self):
#         # return f"Красный автомобиль модели Tesla" # В нашем случае это будет негибко, лучше так:
#         return f"{self.color.capitalize()} автомобиль модели {self.model}"

# my_car = Car("Tesla", "red")

# # Теперь у нас есть оба варианта:
# print(my_car)                     # Вызовет __str__:  Красный автомобиль модели Tesla
# print(repr(my_car))               # Вызовет __repr__: Car(model='Tesla', color='red')
# print([my_car])                   # Вызовет __repr__: [Car(model='Tesla', color='red')]

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         # Добавим repr для красивого вывода
#         return f"Vector({self.x}, {self.y})"

#     # --- Вот наша перегрузка оператора `+` ---
#     def __add__(self, other):
#         """Этот метод вызывается, когда Vector стоит СЛЕВА от знака `+`."""
#         # 'self' - это первый вектор (v1)
#         # 'other' - это второй вектор (v2)
        
#         # Создаем НОВЫЙ вектор, являющийся суммой двух других
#         new_x = self.x + other.x
#         new_y = self.y + other.y
#         return Vector(new_x, new_y)

# # Теперь магия работает!
# v1 = Vector(2, 3)
# v2 = Vector(4, 5)

# # За кулисами Python выполняет: v1.__add__(v2)
# result = v1 + v2

# print(v1)
# print(v2)
# print(result) # Выведет: Vector(6, 8)


# class Point:
#     def __init__(self, x):
#         self.x = x

#     def __repr__(self):
#         return f"Point({self.x})"

#     # --- Перегрузка оператора РАВЕНСТВА (==) ---
#     def __eq__(self, other):
#         """Две точки равны, если их координаты x равны."""
#         print(f"Вызван __eq__ для {self} и {other}")
        
#         # 1. Проверяем, что сравниваем с объектом того же типа
#         if not isinstance(other, Point):
#             return NotImplemented
            
#         # 2. Возвращаем результат сравнения атрибутов
#         return self.name == other.name
    
# p1 = Point(10)
# p2 = Point(10)
# p3 = Point(20)

# print(p1 == p2) # Выведет: True
# print(p1 == p3) # Выведет: False
# print(p1 == 10) # Выведет: False (благодаря проверке isinstance)


# class Point:
#     def __init__(self, x):
#         self.x = x

#     def __repr__(self):
#         return f"Point({self.x})"

#     def __eq__(self, other):
#         if not isinstance(other, Point):
#             return NotImplemented
#         return self.x == other.x

#     # --- Перегрузка оператора "МЕНЬШЕ ЧЕМ" (<) ---
#     def __lt__(self, other):
#         """Одна точка "меньше" другой, если ее координата x меньше."""
#         if not isinstance(other, Point):
#             return NotImplemented
#         return self.x < other.x
    
# # Создаем список из объектов Point в произвольном порядке
# points_list = [Point(100), Point(20), Point(50), Point(-10)]
# print(f"Исходный список: {points_list}")

# # А теперь магия! Python будет многократно вызывать __lt__ и __eq__
# # для сравнения элементов и их расстановки.
# sorted_points = sorted(points_list)

# print(f"Отсортированный список: {sorted_points}")


# class Portfolio:
#     def __init__(self):
#         self._stocks = {}

#     # Магия длины
#     def __len__(self):
#         return len(self._stocks)

#     # Магия чтения []
#     def __getitem__(self, ticker):
#         return self._stocks.get(ticker, 0)

#     # Магия записи []
#     def __setitem__(self, ticker, amount):
#         if amount < 0:
#             raise ValueError("Нельзя иметь отрицательное число акций")
#         self._stocks[ticker] = amount
        
#     # Вспомогательный метод для добавления (накапливания)
#     def add_stock(self, ticker, amount):
#         self._stocks[ticker] = self._stocks.get(ticker, 0) + amount

#     def __str__(self):
#         return str(self._stocks)

# # --- Тестируем ---
# my_port = Portfolio()

# # 1. Используем вспомогательный метод (накапливаем)
# my_port.add_stock("AAPL", 10)
# my_port.add_stock("AAPL", 5)  # Теперь их 15!

# # 2. Используем __setitem__ (устанавливаем напрямую)
# my_port["GOOGL"] = 3
# my_port["TSLA"] = 35

# # 3. Используем __len__
# print(f"Всего позиций в портфеле: {len(my_port)}") # Вывод: 3

# # 4. Используем __getitem__
# print(f"У нас Apple: {my_port['AAPL']} шт.")       # Вывод: 15
# print(f"У нас Google: {my_port['GOOGL']} шт.")     # Вывод: 3
# print(f"У нас Google: {my_port['TSLA']} шт.")     # Вывод: 35

# ============================================================================================
# "До": Классический геттер
# class User:
#     def __init__(self, age):
#         self._age = age # Защищенный атрибут

#     def get_age(self):
#         """Обычный метод-геттер."""
#         return self._age

# user = User(30)
# # Чтобы получить возраст, мы ВЫЗЫВАЕМ МЕТОД
# print(user.get_age()) # 30

# # "После": Использование @property
# class User:
#     def __init__(self, age):
#         self._age = age

#     # 1. Применяем декоратор @property к нашему геттеру
#     @property
#     # 2. Переименовываем метод в то имя, которое мы хотим видеть снаружи
#     def age(self):
#         """Это метод-геттер, замаскированный под атрибут."""
#         print("(Вызывается геттер)") # Добавим для наглядности
#         return self._age

# user = User(30)

# # Теперь, чтобы получить возраст, мы ОБРАЩАЕМСЯ К АТРИБУТУ
# # Скобки () больше не нужны!
# print(user.age)

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = 0      # Инициализируем нулем
#         self.age = age     # Тут сработает наш сеттер!

#     # 1. ГЕТТЕР (Чтение)
#     @property
#     def age(self):
#         return self._age

#     # 2. СЕТТЕР (Запись)
#     @age.setter
#     def age(self, value):
#         print(f">> Проверяем число {value}...")
#         if 0 <= value <= 120:
#             self._age = value  # Всё ок, кладем в сейф
#             print(">> Успешно сохранено!")
#         else:
#             print(">> Ошибка! Недопустимый возраст.")

# # Проверяем
# u = User("Маша", 25)
# # Вывод: >> Проверяем число 25... >> Успешно сохранено!

# u.age = -5
# # Вывод: >> Проверяем число -5... >> Ошибка! Недопустимый возраст.

# print(u.age) # 25 (осталось старое значение)


# Класс 1: Обычный, с __dict__
class PointWithDict:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Класс 2: Оптимизированный, со __slots__
class PointWithSlots:
    # Объявляем фиксированный набор атрибутов
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

# --- Тестируем обычный класс ---
print("--- PointWithDict ---")
p_dict = PointWithDict(10, 20)
print(f"Атрибуты: x={p_dict.x}, y={p_dict.y}")

# У него есть __dict__
print(f"__dict__: {p_dict.__dict__}")

# Мы можем добавлять новые атрибуты на лету
p_dict.z = 30
print(f"Новый атрибут z: {p_dict.z}")
print(f"__dict__ после добавления: {p_dict.__dict__}")


# --- Тестируем класс со слотами ---
print("\n--- PointWithSlots ---")
p_slots = PointWithSlots(10, 20)
print(f"Атрибуты: x={p_slots.x}, y={p_slots.y}")

# Попытка получить доступ к __dict__
try:
    print(p_slots.__dict__)
except AttributeError as e:
    print(f"Попытка доступа к __dict__: Ошибка! {e}")

# Попытка добавить новый атрибут
try:
    p_slots.z = 30
except AttributeError as e:
    print(f"Попытка добавить новый атрибут: Ошибка! {e}")