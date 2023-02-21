#!/usr/bin/env python3

def admin_login(username, password):
    # your code here 
    #   Write a method `admin_login` that takes two arguments, a username and a
    #   password. If the username is "admin" or "ADMIN" and the password is "12345",
    #   return "Access granted". Otherwise, return "Access denied".
    if (username == "admin" or username == "ADMIN") and (password == "12345"):
        return ("Access granted")
    else:
        return ("Access denied")
    

def hows_the_weather(temperature):
    # your code here
    #   Write a method `hows_the_weather` that takes in one argument, a temperature.
    #   If the temperature is below 40, return "It's brisk out there!". If the temperature is
    #   between 40 and 65, return "It's a little chilly out there!". If the temperature is above 85,
    #   return "It's too dang hot out there!". Otherwise, return "It's perfect out there!"
    if temperature < 40:
        return ("It's brisk out there!")
    elif temperature >= 40 and temperature < 65:
        return ("It's a little chilly out there!")
    elif temperature >= 65 and temperature < 85:
        return ("It's perfect out there!")
    else:
        return ("It's too dang hot out there!")
    

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return ("FizzBuzz")
    elif num % 3 == 0:
        return ("Fizz")
    elif num % 5 == 0:
        return ("Buzz")
    else:
        return (num)
    

def calculator(operation, num1, num2):
    # your code here
    #   Write a method `calculator` that takes three arguments: an operation and two
    #   numbers. If the operation is one of the following: `+`, `-`, `*`, or `\`,
    #   return the value of calling the operation on the two numbers. Otherwise,
    #   output a message saying "Invalid operation!" and return `nil`.
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print ("Invalid operation!")
        return None
