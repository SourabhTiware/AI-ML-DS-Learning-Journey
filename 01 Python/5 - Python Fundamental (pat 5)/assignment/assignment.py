# Q1 - Create a program that:
#      1. Opens a file "names.txt" in write mode
#      2. Writes 5 names (one per line) entered by the user
#      3. Then opens the same file in read mode and prints all names

# with open("name.txt","r") as f:
#     # data = f.write("Sourabh")
#     print(f.read())

# with open("name.txt","a") as f:
#     data = f.write("\nakahsy\nram\nBob")

# with open("name.txt","r") as f:
#     # data = f.write("Sourabh")
#     print(f.read())


# Q2 - Create a program that:
#   1. Opens a file "log.txt" in append mode
#   2. Adds a new log entry (like "program run successfully")
#   3. Opens the file read mode and prints all logs

# with open("log.txt","a+") as f:
#     f = f.write("Program run successfully")
#     print(f.readline())

# Python Restart Journey 

# -----------------------------------------------------------------------------
"""
    1. Create a program that:
        1. Opens a file "names.txt" in write mode
        2. Writes 5 names (one per line) entered by the user
        3. Then opens the same file in read mode and prints all names
"""
# -----------------------------------------------------------------------------

# with open("name2.txt", "w+") as f:
#     data = f.write("Sourabh\nRaj\nShivani\nNeha\nNethaji")
#     data = f.readline()


# with open("name2.txt", "r") as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
    

# -----------------------------------------------------------------------------
"""
    2. Create a program that:
        1. Opens a file "log.txt" in append mode
        2. adds a new log entry (like "program run successfully")
        3. Opens the file in read mode in prints all logs. 
"""
# -----------------------------------------------------------------------------

# with open("logs2.txt", "a+") as f:
#     f.write("Program run successfully 2 times")

# with open("logs2.txt", "r") as file:
#     print("---- Log Entries ----")
#     print(file.read())


# -----------------------------------------------------------------------------
"""
    3.Create a program that:
        1. Has a list of numbers: [5, 10, 15, 20, 25]
        2. users a list comprehension to create a new list with only numbers greater that 15
        3. prints the new list
"""
# -----------------------------------------------------------------------------

# numbers = [5,10,15,20,25]

# new_list = [num for num in numbers if num > 15]

# print(new_list)


# -----------------------------------------------------------------------------
"""
    4. Create a python dictionary of 3 cities and their populations. save it to "cities.json"
        1. Then load the JSON and print each city and it's population
        2. Ask the user for a new city & it's population - update this info in the json file
"""
# -----------------------------------------------------------------------------

# import json

# cities = {
#     "Mumbai": 12442373,
#     "Pune": 7449834,
#     "Nagpur": 2405665
# }

# with open("cities.json", "w") as file:
#     json.dump(cities, file, indent=4)


# with open("cities.json", "r") as file:
#     data = json.load(file)


# print("Cities and their Populations:")
# for city, population in data.items():
#     print(f"{city} : {population}")

# new_city = input("\nEnter a new city: ")
# new_population = int(input("Enter its population: "))


# data[new_city] = new_population


# with open("cities.json", "w") as file:
#     json.dump(data, file, indent=4)

# print("\nCity added successfully!")

# print("\nUpdated Cities and Populations:")
# for city, population in data.items():
#     print(f"{city} : {population}")



"""
    5. Write a program that tires to open "data.txt" in read mode. if the file does not exist, catch the exception and print "File not found"
"""
# -----------------------------------------------------------------------------


try:
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")