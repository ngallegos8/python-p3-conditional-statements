#!/usr/bin/env python3

# def admin_login(username, password):
#     if (username == "admin" or username == "ADMIN") and (password == "12345"):
#         return "Access granted"
#     else:
#         "Access denied"

# def hows_the_weather(temperature):
#     if temperature < 40:
#         return "It's brisk out there!"
#     elif temperature >= 40 and temperature < 65:
#         return "It's a little chilly out there!"
#     elif 85 >= temperature:
#         return "It's too dang hot out there!"
    
#     print("It's perfect out there!")
        
    

# def fizzbuzz(num):
#     if not num % 15:
#         return "FizzBuzz"
#     elif not num % 3:
#         return "Fizz"
#     elif not num % 5:
#         return "Buzz"
    
    
#     return num

# def calculator(operation, num1, num2):
#     if operation == "+":
#         return num1 + num2
#     elif operation == "-":
#         return num1 - num2
#     elif operation == "*":
#         return num1 * num2
#     elif operation == "/":
#         return num1 / num2
    
#     print("Invalid operation!")
#     return None

# # # OR...
# def calculator(operation, num1, num2):
#     if operation is "+":
#         return num1 + num2
#     elif operation is "-":
#         return num1 - num2
#     elif operation is "*":
#         return num1 * num2
#     elif operation is "/":
#         return num1 / num2
    
#     print("Invalid operation!")
#     return None


def admin_login(username, password):
    if username.upper() == "ADMIN" and password == "12345":
        return "Access granted"
    
    return "Access denied"

def hows_the_weather(temperature):
    if temperature > 85:
        return "It's too dang hot out there!"
    elif 65 >= temperature >= 40:
        return "It's a little chilly out there!"
    elif temperature < 40:
        return "It's brisk out there!"

    return "It's perfect out there!"

def fizzbuzz(num):
    if not num % 15:
        return "FizzBuzz"
    elif not num % 5:
        return "Buzz"
    elif not num % 3:
        return "Fizz"
    
    return num

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

    print("Invalid operation!")
    return None