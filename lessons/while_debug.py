"""Practice while loops and debug them"""

my_number = 8675309
my_number_str = str(my_number)
total = 0
index = 0
while index < len(my_number_str):
    value: int = int(my_number_str[index])
    total += value
    index += 1