dictionary = {}

for number in range(1,51):
    if number % 2  == 0 and number % 7 == 0:
        dictionary[number] = number * 2
    elif number % 2 == 0:
        dictionary[number] = number + 1
    elif number % 7 == 0:
        dictionary[number] = number - 1
    else:
        dictionary[number] = number

print(dictionary)