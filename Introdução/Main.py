# #This is my first python program
# #print("I like Mac and cheese")
# #print("It's really good")

# # Strings ---------------------------------------------------------------------------------
# #first_name = "Lucas"
# #food = "Mac and cheese"
# #email = "lucas@gmail.com"

# #print(f"Hello {first_name}")
# #Print(f"You like {Food}")

# #Integers ---------------------------------------------------------------------------------
# #age = 25
# #quantity = 3
# #num_of_students = 30

# #print(f"You are {age} years old")
# #print(f"You are buying {quantity} itens")
# #print(f"Your class has {num_of_students} students")

# # Float ---------------------------------------------------------------------------------
# # price = 10.99
# # gpa = 3.2
# # distance = 5.5

# # print(f"The price is ${price}")
# # print(f"Your gpa is: {gpa}")
# # print(f"you ran {distance} kilometers")

# # Boolean ---------------------------------------------------------------------------------
# is_student = False
# for_sale = True
# is_online = True
# #     #Exercise
# # user_name = "Lucas Cotrim"
# # year = 2025
# # pi = 3.14
# # is_admin = True

# # print(f"Your name is {user_name}")
# # print(f"We are in the year {year}")
# # print(f"Usually, in exams, {pi} is a short for pi")
# # if is_admin:
# #     print("You are a admin")
# # else:
# #     print("You are not a admin")
# # print (f"Are you a student?: {is_student}")

# # if is_student:
# #     print("You are a student")
# # else:
# #     print("You are NOT  a student")

# # if for_sale:
# #     print("That item is for sale")
# # else:
# #     print("That item is not available")

# # if is_online:
# #     print("You are online")
# # else:
# #     print("You are offline")

# #Typecasting ---------------------------------------------------------------------------------

# name = "Bro code"
# age = 25
# gpa = 3.2
# is_student = True

# gpa = int(gpa)
# print (gpa)

# age = float(age)
# print(age)

# age = str(age)
# print(age)
# print(type(age))

# name = bool(name)
# print(name)
# #falso apenas se não houver dado na variável

#Input ---------------------------------------------------------------------------------

# name = input("What is your name?:")
# age = int(input("How old are you?:"))

# age = age + 1

# print(f"Hello {name}!")
# print("HAPPY BIRTHDAY!!!")
# print(f"You are {age} years old")

    #Exercise 1 Rectangle area calc
# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))

# print(f"The are of the rectangle is {length*width}cm²")
#     #or
# area = length * width

# print(f"the area of the rectangle is {area}cm²")

    #Exercise 2 Shopping cart program

# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity

# print(f"You have bought {quantity} X {item}/s")
# print(f" your tortal is {total}")

# Madlibs game: ---------------------------------------------------------------------------------
# word game where you create a random story by filling in blacns with random words

# adjective1 = input("Enter an adjective (description): ")
# noun1 = input("Enter a noun (person, place, thing): ")
# adjective2 = input("Enter an adjective (description): ")
# verb1 = input("Enter a verb ending with 'ing'")
# adjective3 = input ("Enter an adjective (description): ")


# print(f"Today I went to a {adjective1} zoo.")
# print(f"In an exhibit, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")

# mathematics functions ---------------------------------------------------------------------------------

# friends = 0

# # #friends = friends + 1   
# # friends += 1
# friends = friends - 2
# friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends/2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# remainder = friends % 3

# print(friends)


# x = 3.14
# y = 4
# z = 5

# # result = round (x)
# # result = abs(y)
# # result = pow(4, 3)
# # result = max(x, y, z)
# result = min(x, y, z)
# print (result)

# import math

# x = 9

# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)

# print(result)

# import math

# radius = input ("Enter the radius of a circle: ")

# circumference = 2 * math.pi * radius

# print(f"The circumference is: {round(circumference, 2)}cm")

# import math

# radius = float(input("Enter the radius of a circle: "))

# area = math.pi * pow(radius, 2)

# print (f"The area of the circle is: {round(area, 2)}cm²")

#Hipotenusa

# import math

# a = int(input("Enter the length of side A: "))
# b = int(input("Enter the length of side B: "))

# hip = math.sqrt(a**2 + b**2)

# print(f"Side c's length equals {hip}")

#if ---------------------------------------------------------------------------------

# age = int(input("Enter your age: "))

# if age >=100:
#     print("You're too old to sign up")
# elif age >= 18:
#     print("You are now signed up")
# elif age < 0:
#     print("You haven't been born yet")
# else:   
#     print("You must be 18+ to sign up")

# response = input("Would you like food? (Y/N): ")

# if response == "Y":
#     print("Have some food")
# else:
#     print("No food for you")


# name = input("Enter your name: ")

# if name == "":
#     print("You dud not type your name")
# else:
#     print(f"Hello, {name}")

# user_online = True

# if user_online:
#     print("The user is online")
# else:
#     print("The user is offline")

# operator = input("Escolha o que deseja fazer. (Somar[S], multiplicar[M], dividir[D] e subtrair[Su]): ")
# n1 = int(input("Escolha um número: "))
# n2 = int(input("Escolha o segundo numero: "))

# if operator == "S":
#     print(f"A soma é {n1 + n2}")
# elif operator == "M":
#     print(f"A multiplicação é {n1 * n2}")
# elif operator == "Su":
#     print (f"A substração é {n1 - n2}")
# else:
#     print(f"A divisão é {n1 / n2}")

    #weight converter

# weight = float(input("Whats your weight?: "))
# converter = input("Kilograms or pounds?: (K/P)")

# if converter == "K":
#     print(f"You weight {round(weight)} in Kilograms and {round(weight / 2.205)} in pounds.")
# elif converter == "P":
#     print(f"You weight {round(weight)} in pounds and {round(weight * 2.205)} in kilograms.")
# else:
#     print("You inserted an invalid option.")

    #temperature converter

# unidade = input("Type in the unit of temperature (K, C or F): ")
# temp = float(input("type in th teperature: "))

# if unidade == "K":
#     print(f"The temperature in Fahrenheit is {(temp - 273.15) * 9/5 + 32} and in Celsius is {temp - 273.15}")
# elif unidade == "C":
#     print(f"The temperature in Kelvin is {temp + 273.15} and in fahrenheit is {temp * 9/5 + 32}")
# elif unidade == "F":
#     print(f"The temperature in celsius is {(temp -32) * (5/9)} and in Kelvin is {(temp - 32) * 5/9 + 273.15}")
# else:
#     print(f"{unidade} is invalid")

#Logical operators ----------------------------------------------------------------------------------------------------

# temp = 25
# is_raining = False

# if temp > 35 or temp <0 or is_raining:
#     print("The outdoor event is cancelled")
# else:   
#     print("The outdoor event is still scheduled")

# temp = 23
# is_sunny = True

# if temp >= 23 and is_sunny:
#     print("It is hot outside")
#     print("It is sunny")
# elif temp <= 0 and is_sunny:
#     print("It is cold outside")
#     print("It is sunny")
# elif 28 > temp > 0 and is_sunny:
#     print("It is warm outisde")
#     print("It is sunny")
# elif 28 > temp > 0 and not is_sunny:
#     print("It is warm outside")
#     print("It is cloudy")
# elif temp <= 0 and not is_sunny:
#     print("It is cold outside")
#     print("It is cloudy")

#COnditional expresions -----------------------------------------------------------------------------------------------------

# num = 5
# a = 6
# b = 7
# age = 18
# temperature = 203
# user_role = "admin"

# # print("Positive" if num > 0 else "Negative")

# # result = "Even" if num % 2 == 0 else "Odd"

# # max_num = a if a > b else b
# # min_num = a if a < b else b

# # status = "Adult" if age >= 18 else "Child"

# # weather = "HOT" if temperature > 20 else "COLD"

# access_level = "Full access" if user_role == "admin" else "Limited access"

# print(access_level)

# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")

# result = len(name)
# result = name.find(" ")
# result = name.rfind(" ")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# phone_number = phone_number.replace("-", " ")

# print(help(str))

# #Exercise "creating a username"

# user_name = input("Enter an username: ")

# if len(user_name) > 12:
#     print("Invalid Username, your username can't be more than 12 characters long")
# elif not user_name.find(" ") == -1:
#     print("Invalid username, your username can't contain spaces")
# elif not user_name.isalpha():
#     print("Invalid username, your username can't contain digits")
# else:
#     print(f"Valid username, welcome {user_name}")


# indexing ----------------------------------------------------------------------------------------------------------------

# credit_number = "1234-5678-9101-0976"

# # print(credit_number[10])
# # print(credit_number[:4])
# # print(credit_number[5:9])
# # print(credit_number[5:])
# # print(credit_number[-4])
# # print(credit_number[::3])

# last_digits = credit_number[-4:]
# credit_number = credit_number[::-1]
# print(f"XXXX-XXXX-XXXX{last_digits}")
# print(credit_number)

# Format especifier ----------------------------------------------------------------------------------

# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34
# price4 = 80.44
# price5 = 7.41
# price6 = 1904890.21

# print(f"Price 1 is ${price1:.<10}")
# print(f"Price 2 is ${price2:.>10}")
# print(f"Price 3 is ${price3:.2f}")
# print(f"Price 4 is ${price4:.^10}")
# print(f"Price 5 is ${price5:-}")
# print(f"Price 6 is ${price6:+,.2f}")

#While loop ------------------------------------------------------------------------------------------------

# name = input ("Enter your name: ")

# while name == "":
#     print("You did not enter you name")
#     name = input("Enter your name: ")

#     print(f"Hello, {name}")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# num = int(input("Enter a # between 1 - 10: "))

# while num < 1 or  num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # bewtween 1 - 10: "))

#Python compound interest calculator -----------------------------------------------------------------------------------------------------------

# 

# for loop ----------------------------------------------------------------
# for counter in range(1, 11):
#     print(counter)

# for counter in reversed(range(1, 11)):
#     print(counter)
# print("Happy new year!")

# for x in range (1, 11, 3):
#     print(x)

# credit_card = "1234-5678-9012"

# for x in credit_card:
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         continue
#     else: 
#         print(x)

#Execise timer module
# import time

# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("TIME'S UP")

#nested loop ---------------------------------------------------------------------------------------------------------------------------------

# rows =  int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbol = input("Enter a symbol: ")

# for x in range(rows):
#     for y in range (columns):
#         print(symbol, end = " ")
#     print()

# Collection  list [] set {}tuple ()-----------------------------------------------------------------------------------------------------------

# fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)
          
# fruits[1] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# print(fruits[0])
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("banana"))

# for fruit in fruits:
#     print(fruit)

# fruits = {"apple", "orange", "banana", "coconut"}

#fruits[1] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# print(fruits[0])
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("banana"))

# exercise Shopping cart program

# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Enter a food to buy (q to qut): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("------- Your cart -------")

# for food in foods:
#     print(food, end=" ")

# for price in prices:
#     total += price

# print(f"Your total is: ${total}")

# 2d Lists -----------------------------------------------------------------------------------------------------------------

# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]
# print(groceries[2][1])
#--------

# groceries = [["apple", "orange", "banana", "coconut"], 
#              ["celery", "carrots", "potatoes"], 
#              ["chicken", "fish", "turkey"]]

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()

#exercise
# num_pad = ((1, 2, 3),
#            (4, 5, 6),
#            (7, 8, 9),
#            ("*", 0, "*"))

# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()

#exercise quiz game 

questions = ("What's the biggest ocean in the world?", 
             "What's the tallest land animal in the world?", 
             "In what states is found the statue of liberty?", 
             "What's the name of the planet closest to the sun?")

options = (("A. Atlantic Ocean", "B. Indian Ocean", "C. Artic Ocean", "D. Pacific Ocean"), 
           ("A. Hippopothamus", "B. Giraffe", "C. Elephant", "D. Rhinoceros"), 
           ("A. USA", "B. France", "C. Brazil", "D. Russia"), 
           ("A. Jupiter", "B. Mars", "C. Mercury", "D. Venus"))

answers = ("D", "B", "A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

    print("-----------------")
    print("     Results     ")
    print("-----------------")

    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
