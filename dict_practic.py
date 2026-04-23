# countries = {
#     "Sweden": ["Stockholm", "Göteborg", "Malmö"],
#     "Norway": ["Oslo", "Bergen", "Trondheim"],
#     "England": ["London", "Birmingham", "Manchester"],
#     "Germany": ["Berlin", "Hamburg", "Munich"],
#     "France": ["Paris", "Marseille", "Toulouse"]
# }

# city = input()

# for key, value in countries.items():
#     if city in value:
#         print(f"INFO: {city} is a city in {key}")
#         break
# else:
#     print(f"ERROR: Country for {city} not found")
        
# days = {
#     1: 31,
#     2: 28,
#     3: 31,
#     4: 30,
#     5: 31,
#     6: 30,
#     7: 31,
#     8: 31,
#     9: 30,
#     10: 31,
#     11: 30,
#     12: 31
# }

# month = int(input())

# if month in days:
#     print(days[month])

# sweet = {
#     "id": "0001",
#     "type": "donut",
#     "name": "Cake",
#     "ppu": 0.55,
#     "calories": 125,
# }

# sweet["weight"] = 230
# sweet["have_topping"] = True
# sweet["name"] = "SuperCake"
# sweet["calories"] = 350
# print(sweet)

alphabet = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
    'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
    'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
    'w': 23, 'x': 24, 'y': 25, 'z': 26
}

text = input().split()

for letter in text:
    alphabet.pop(letter, None)

print(alphabet)