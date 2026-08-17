# The use of IF and ELSE

# Use of Else If; elif
# Example
# If A is correct, choose A
# elif B is correct, choose B
# elif C is correct, choose C
# else choose D

# For Instance
# answer = input("Enter the correct option from A to D: ")
# if answer == "A":
#     print("you chose A")
# elif answer == "B":
#     print("you chose B")
# elif answer == "C":
#     print("you chose C")
# else:
#     print("you chose D")

# For the above instance, if I input say ABD together, the output will be you chose D.
# To correct that, we do this instead

# answer = input("Enter the correct option from A to D: ")
# if answer == "A":
#     print("you chose A")
# elif answer == "B":
#     print("you chose B")
# elif answer == "C":
#     print("you chose C")
# elif answer == "D":
#     print("you chose D")
# else:
#     print("please follow the instructions")


#Another example

# score = input("Enter your score from 0 to 100: ")
# score = int(score)
# if 70 <= score <= 100:
#     print("Your score is A")
# elif 60 <= score <= 69:
#     print("Your score is B")
# elif 50 <= score <= 59:
#     print("Your score is C")
# elif 45 <= score <= 49:
#     print("Your score is D")
# elif 40 <= score <= 44:
#     print("Your score is E")
# elif 0 <= score <= 39:
#     print("Your score is F")
# else:
#     print("The input is not valid")
#
#
# # Types of If Else Statements
# There are 2 types
# Exclusive If Elif statements
# And Inclusive If Elif statement

# Exclusive IF ELIF
# In exclusive if else statement, there is no overlap b/n the two conditions

# EG, If (Value > 7)
#     elif (Value < -5)
# # The 2 values do not overlap
# The significance is  that, the order of writing the code does not matter for this type

# INCLUSIVE IF ELSE STATEMENTS
# For this type, there are points of intersection between the 2 conditional statements
# ,and you have to follow the order of writing the code.
# You must start from the point of intersection and then write for the 2 other conditions

# If you start with the code for one condition and not the intersection, it will return the value of the one since
# the intersection is also part of it the condition.

# EG
number = input("Please input your number: ")
number = int(number)
if number % 6 == 0:
    print ("The number is a multiple of 2 and 3")
elif number % 2 == 0:
    print ("The number is a multiple of 2")
elif number % 3 == 0:
    print ("The number is a multiple of 3")
else:
    print ("The number is neither a multiple of 2 nor 3")

# But if the order were to change, say number % 2 ==0 comes first before 6, the results will be different
