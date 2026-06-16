
# --------------------------------------------------------------------------
# Lecture 1: Our First Program
# --------------------------------------------------------------------------


# print("Lecture 1: Our First Program")
# print("Hello World")

# x = 76

# print(x + 40)


# --------------------------------------------------------------------------
# Lecture 2: Variables in Python
# --------------------------------------------------------------------------- 


# print("Lecture 2: Variables in python")
# name = "Sourabh Tiware"

# _age = 25

# city_name = "pune"

# print(name)
# print(_age)
# print(city_name)

# print("my name is", name, "and i'm",_age,"year's old." "\ni'm belongs from",city_name,"city")

# --------------------------------------------------------------------------
# Lecture 3: Data Types in Python
# --------------------------------------------------------------------------- 
# print("Lecture 3: Data Types in Python")

# print("Integer Types ")

# age = 34
# bank_balance = 45990

# print("age",age,"and total amount ", bank_balance)

# print("check type")

# print(type(age))
# print(type(bank_balance))

# print("String")

# name = "Hello, I'm Sourabh Tiware"
# qualificatiion = "MCA"

# print(name,qualificatiion)

# print("check type")

# print(type(name))
# print(type(qualificatiion))

# print("float")

# pi = 3.14
# x = 8.4

# print(pi,"and",x)

# print("check type")

# print(type(pi))
# print(type(x))


# print("Boolean")

# isPrime = True
# nonPrime = None

# print(isPrime)
# print(nonPrime)

# print("check type")

# print(type(isPrime))
# print(type(nonPrime))

# print("None type")

# car_value = None
# print(car_value)

# print("check type")

# print(type(car_value))


# --------------------------------------------------------------------------
# Lecture 4: Keywords & comments in Python
# --------------------------------------------------------------------------- 
# print("Lecture 4: Keywords & comments in Python")

#  Keywords - those words are not used for declaring variable name / function name. 

#  Single Line comments = #

''' this is a multiple comments. '''


# --------------------------------------------------------------------------
# Lecture 5: style Guide in Python
# --------------------------------------------------------------------------- 
# print("Lecture 5: style Guide in Python")


# print("Snake case = total_price")
# print("camcel case = totalPrice")
# print("Pascal Casse = TotalPrice")

# print("Python prefer SNAKE CASE ")

# # Task - calculate sum of two number 

# print("\n \nTask - calculate sum of two number ")

# a = 5
# b = 10

# sum = a + b
# print("sum of two numbers ",sum)


# --------------------------------------------------------------------------
# Lecture 6: Arithmetic operator in Python
# --------------------------------------------------------------------------- 
# print("Lecture 6: Arithmetic operator in Python\n\n")

# a = 5
# b = 10

# print("a = 5 & b = 10 \n")

# print("addition oprator a + b:", a + b,"\n")
# print("substraction oprator a - b:", a - b,"\n")
# print("multiplication oprator a * b:", a * b,"\n")
# print("division oprator a / b:", a / b,"\n")
# print("module oprator a '%' b:", a % b,"\n") # calculate reminder
# print("power oprator a ** b:", a ** b,"\n")


# --------------------------------------------------------------------------
# Lecture 7: Relational / comparison operator in Python
# --------------------------------------------------------------------------- 
# print("Lecture 7: Relational / comparison operator in Python\n\n")


# a = 10
# b = 5

# print("a = 10 & b = 5 \n")

# print("greate than: ", a > b,"\n")
# print("greate than equal to : ", a >= b,"\n")
# print("less than: ", a < b,"\n")
# print("less than equal to : ", a <= b,"\n")
# print("equal to : ", a == b,"\n")
# print("not equl to : ", a != b,"\n")


# --------------------------------------------------------------------------
# Lecture 8: Assignment operator in Python
# --------------------------------------------------------------------------- 
# print("Lecture 8: Assignment operator in Python\n\n")


# a = 10
# b = a



# print("equal to ", b)

# a += 5
# print("plus equal to a += 5  : ",a)

# d = 10

# d -= 3
# print("minus equal to d = 10, d -= 3 : ",d)


# x = 15 

# x *=3
# print("multiple equal to x = 15, x*=3 : ", x)


# z = 10

# z /=2

# print("divide equal to z = 10, z /= 2 : ", z)

# b = 4

# b **=2

# print("power equal to b = 4, b **=2 : ", b)

# r = 10

# r %=2

# print("module equal to r = 10, r %=2 : ", r)


# --------------------------------------------------------------------------
# Lecture 9: Logical operator in Python
# ---------------------------------------------------------------------------
# print("\nLecture 9: Logical operator in Python\n\n") 

# print("not operator - it's a convert into reverse => means if value is true convert into false vice varsa \n")

# print("not True : ",not True)
# print("not False : ", not False)

# print("not 5 > 7 : ",not (5>7))
# print("not 5 < 7 : ", not (5 < 7), "\n")


# print("and operator \n")

# print("T and T = T")
# print("T and F = F")
# print("F and T = F")
# print("F and F = F")


# print("\n(5 < 6) and (8 < 9): ", (5 < 6) and (8 < 9))
# print("\n(5 < 6) and (8 > 9): ", (5 < 6) and (8 > 9))
# print("\n(5 > 6) and (8 < 9): ", (5 > 6) and (8 < 9))
# print("\n(5 > 6) and (8 > 9): ", (5 > 6) and (8 > 9))

# print("\nor operator\n")


# print("T or T = T")
# print("T or F = T")
# print("F or T = T")
# print("F or F = F")

# print("\n(5 < 6) or (8 < 9): ", (5 < 6) or (8 < 9))
# print("\n(5 < 6) or (8 > 9): ", (5 < 6) or (8 > 9))
# print("\n(5 > 6) or (8 < 9): ", (5 > 6) or (8 < 9))
# print("\n(5 > 6) or (8 > 9): ", (5 > 6) or (8 > 9))


# print("\nbitwise operator")


# --------------------------------------------------------------------------
# Lecture 10: Operator precedence in Python
# ---------------------------------------------------------------------------
# print("\nLecture 10: Operator precedence in Python\n\n")


# print("10 * 2 + 5 :", 10 * 2 + 5)
# print("\nSame precendence: 10 / 2 * 4 : ", 10 / 2 * 4)


# --------------------------------------------------------------------------
# Lecture 11: Operator precedence in Python
# ---------------------------------------------------------------------------
# print("\nLecture 10: Operator precedence in Python\n\n")


# print("\nImplicit (automatic perform by python) and explicit (perform by developer with compitable conversion)")

# val1 = 10 + 38.0 
# print("\n 10 + 38.0 : ", val1, "= Implicit type conversion by python. Type = ", type(val1) )

# val2 = int(40.0 + 8)
# print("\n int(40.0 + 8) : ", val2, "= using int function convert float answer into the int. Type = ", type(val2))

# str = int("123")
# print("\n int('123') : ", str, "= Implicit type conversion. String value convert it into INT Type = ", type(str))

# val3 = bool(10)
# print("\n bool(10): ", val3, "= convert integer into boolean value. 0 measn False and True means any number != 0 Type = ", type(val3))

# val4 = bool(0)
# print("\n bool(0) : ", val4, "= convert integer into boolean value. 0 means False and True means any number != 0. Type = ", type(val4))


# --------------------------------------------------------------------------
# Lecture 12: Taking user input in Python
# ---------------------------------------------------------------------------
# print("\nLecture 12: Taking user input in Python\n\n")

# a = input("enter value:")
# print(a)

# print("\nget input 2 number from user and perform addition of those number: ")

# num1 = input("enter value one: ") 
# num2 = input("enter value two: ")

# print("value 1 : ",num1, " and value 2 ", num2)

# sum = num1 + num2
# print("\naddition of num1 and num2 ", sum)
# print("\nhere print wrong answer becuase of input function take a input in string format and whenever we perform operation on those string python concat both string.")

# num1 = int(num1) # num1 = int(input("enter value one: "))
# num2 = int(num2) # num2 = int(input("enter value two: "))

# sum2 = num1 + num2
# print("\naddition of two number after conversion into int",sum2)


# --------------------------------------------------------------------------
# Lecture 13: Average of 2 nums in Python
# ---------------------------------------------------------------------------
print("\nLecture 12: Taking user input in Python\n\n")

print("WAP to get input from user and calculate average of two numbers")

x = float(input("enter value 1: "))
y = float(input("enter value 2: "))

avg = (x + y)/2

print(avg)