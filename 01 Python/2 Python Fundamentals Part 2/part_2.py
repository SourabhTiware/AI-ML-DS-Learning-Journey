#-----------------------------------------------------------------------------
# Lec 1: Conditional Statement
#-----------------------------------------------------------------------------
# print("\nLec 1: Conditional Statement\n")


# print("Python conditional statement keyword\nif\nelif\nelse")

# print("\nVoting Program")

# age = int(input("\nEnter you age: "))

# if age >= 18:
#     print("You can vote")
#     print("you can drive")
# else:
#     print("You can't vote")
#     print("You can't drive")

# print("\nTraffic light Program")

# color =input("Enter traffic light color: ")

# if color == "yellow":
#     print("look")
# elif color == "red":
#     print("wait")
# elif color == "green":
#     print("go")
# else:
#     print("Wrong color input")


#-----------------------------------------------------------------------------
# Lec 2: Practice Example on Conditional Statement
#-----------------------------------------------------------------------------
# print("\nLec 2: Practice Example on Conditional Statement\n")

# print("Ques 1: age less than 13 print child \nage is between 13-18 print teenager \nand age is greater than 18 print adult")

# age = int(input("Enter you age: "))

# if(age >= 0 and age < 13):
#     print("child")
# elif (age >= 13 and age <18):
#     print("teenager")
# elif(age >= 18 and age <=60):
#     print("adult")
# elif(age >60):
#     print("oldage")
# else:
#     print("Your input age is wrong")

# print("\nQues 2: Design login system using python ")

# username = "sourabhtiware"
# password = 1234

# user_name = input("\nEnter your username : ")
# pass_word = int(input("\nEnter you password : "))

# if(username == user_name and password == pass_word):
#     print("\nLogin successfully")
# else:
#     print("\nWrong username or password")


# print("\nQues3: check number is multiple of 5 or not")

# num = int(input("enter number "))

# if(num % 5 == 0):
#     print("number is multiple of 5")
# else:
#     print("number is not multiple of 5")


#-----------------------------------------------------------------------------
# Lec 3: Odd or Even
#-----------------------------------------------------------------------------
# print("\n Lec 3: Odd or Even\n")


# print("\nPrint any give number is odd or even")

# num = int(input("\nEnter number to check odd or even : "))

# if( num <= 0):
#     print("Wrong input")
# elif ( num % 2 == 0):
#     print("Even number ")
# else:
#     print("Odd number")


#-----------------------------------------------------------------------------
# Lec 4: Nesting
#-----------------------------------------------------------------------------
# print("\n Lec 4: Nesting\n")

# print("Ques: check user name and password, it's correct print sucess else check again username wrong and password wrong")

# user_name = input("\nenter uesrname : ")
# pass_word = input("\nenter password : ")

# if(user_name == "admin" and pass_word == "pass"):
#     print("\nSuccess")
# else:
#     if( (user_name != "admin") and (pass_word != "pass")):
#         print("\nusername and password both are wrong")
#     elif (user_name != "admin"):
#         print("\nWrong username")
#     else:
#         print("\nWrong password")


# -----------------------------------------------------------------------------
# Lec 5: Match Case in python
# -----------------------------------------------------------------------------
# print("\nLec 5: Match Case in python\n")

# color = input("enter color: ")

# match color:
#     case "Green":
#         print("\nGo")
#     case "Yellow":
#         print("\nLook")
#     case "Red":
#         print("\nStop")
#     case _:
#         print("Wrong input")


# -----------------------------------------------------------------------------
# Lec 6: Loops using while
# -----------------------------------------------------------------------------
# print("\nLec 6: Loops using while\n")

# print("\nQues: print 'Hello World' 10 times using while loops\n")

# i = 1; #iterator

# while(i <=10):
#     print("Hello World", i)
#     i += 1

# print("\nafter end of the loop, i value = ", i)


# -----------------------------------------------------------------------------
# Lec 7: Practice Example (Loops)
# -----------------------------------------------------------------------------
# print("\nLec 7: Practice Example (Loops)\n")

# print("Ques 1: WAP to print 1 to 10\n")

# i = 1

# while( i <= 10 ):
#     print(i)
#     i += 1

# print("Ques 2: WAP to print 10 to 1\n")

# j = 10

# while( j >=1):
#     print(j)
#     j -=1


# -----------------------------------------------------------------------------
# Lec 8: Multiplication Table of n 
# -----------------------------------------------------------------------------
# print("\nLec 8: Multiplication Table of n\n")


# n = int(input("Enter number "))

# i = 1

# while(i <=10):
#     print( n * i)
#     i +=1


# -----------------------------------------------------------------------------
# Lec 9: Break and Continue 
# -----------------------------------------------------------------------------
# print("\nLec 9: Break and Continue\n")

# print("Break keyword work like if condition is true then terminate the loop and \ncontinue keyword work like if condition is true then it's skip the following work and go towards to the loops\n")

# i = 1

# print("Break statement / keyword use")
# while( i <= 10):
#     if(i % 6 == 0):
#         break
#     print(i)
#     i += 1

# print("Continue Statemetn / keyword use")

# while (i <= 10):
#     if( i % 3 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1






