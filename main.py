#DAY 1
# print("hello world!")

# print("4 + 5 =", 4 + 5)
# print("12 / 5 =", 12 / 5)

# List

# my_cars = ["BMW", "Ferrari", "Honda"]
# selected_cars = my_cars[2]
# print("The selected car is:", selected_cars)
# my_cars.append("Toyota")
# print(my_cars)

#DAY 2
#List functions
# age_list = [23, 43, 25, 32]
# length_of_age_list = len(age_list)
# print(length_of_age_list)

# #Find maximum and minimum ages
# maximum_age = max(age_list)
# print("The oldest person is:", maximum_age)

# minimum_age = min(age_list)
# print("The youngest person is:", minimum_age)

#Changing Lists
# my_fruits = ["apple", "orange", "banana", "guava"]
# print(my_fruits)

# #ad item in list
# my_fruits.append("strawberry")
# print(my_fruits)


# find_banana = my_fruits[2]
# print(find_banana)

# #delete item from list
# my_fruits.pop(2)
# print(my_fruits)

# #slicing in list
# print(my_fruits[0:2])

#dictionaries
# person = {"name":"Madiha", "age": "28", "gender":"female"}
# print(person)

# #Accessing values in dictionary
# print(person["age"])

#IF STATEMENTS
# food = ["burger", "pizza", "kebab"]
# entered_food = input("Enter the food you wanted:")
# if entered_food in food:
#     print("i'll bring food for you")
# else:
#     print("Sorry, We don't have right now")    

#FOR LOOP
# for x in range(3,10):
#     print(x)

# names_person = ["madiha", "rehana", "khadija", "aisha"]
# for x,name in enumerate(names_person):
#     names_person[x] = name + "'s room"
# print(names_person)    

#Loop through the Dictionaries
fruit_stock ={"apple": 24, "mango": 55, "strawberry":60}
for name,value in fruit_stock.items():
    print(name,value)

#f string
string_f = f"We have {value} {name}'s in stock"
print(string_f)    

#DAY 3