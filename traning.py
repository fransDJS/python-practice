# my_box = []

# my_box.append('яблоко')
# my_box.append('банан')
# my_box.append('апельсин')

# print(my_box)

# my_list = []

# my_list.append('шлюпка')
# my_list.append('палатка')
# my_list.append('мангал')

# a = my_list[2]
# print(a)
# print(my_list)

wardrobe = {
    "пальто": 15,
    "куртка": 8,
    "шапка": 23
}

wardrobe['пальто'] += 5
a = wardrobe["куртка"]

if 'пальто' in wardrobe:
    print("Пальто есть")

for item, count in wardrobe.items():
    print(f"вещь: {item}, количество: {count}")



