#                                           Lec-01 - String

# word = "python "

# print("total character in string = ",len(word))

# Acces the string character by manually 

# print(word[0])
# print(word[1])
# print(word[2])
# print(word[3])
# print(word[4])

# Accessing the string character using loop

# print("\n \n ")
# for i in word:
#     print(i)


# Concatenate String using " + " operator

# w1 = "I love"
# w2 = "python"

# sentence = w1 + " " + w2
# print(sentence)


#                                           Lec-02 - Slicing in String

# word = "Hello, I'm Sourabh"

# # 0 to end of the sting
# print(word[:])

# # 0 to end of the string in another way
# print(word[0:]) # by default it's going to the end of the stirng 

# # 0 to end of the string in another way
# print(word[:len(word)])

# # 2nd position to the 6 th position ( Last index is not including in final output. )
# print(word[2:7])

# # 11 th position to the end of the string
# print(word[11:])

# # 7th position to the 10 th position ( last index is not included in final output)
# print(word[7:11])


#                                           Lec-03 - String formatting f-string & format()

# 1. format function - python version 3. 

# a = 5
# b = 10

# sum = a+b

# print("sum is {}".format(sum)) # normal formatting
# print("language is {}".format("python"))  # In format string also include string format. 
# print("sum of {} & {} is {} ".format(a,b,sum))


# 1.2 Index formatting. Not mostly use

# print("sum of {0} & {1} is {2}".format(a,b,sum))
# print("sum of {1} & {0} is {2}".format(a,b,sum))

# 1.3 Value based formatting

# print("value of variable {a} & {b}".format(a=4,b=3))

# 2. f-string formatting (Literal string interpolation). mostly used in python code 

# print(f"sum of {a} & {b} is = {a+b}")



#                                           Lec-04 - List in python

# marks = [98, 87, 78, 87,"sourabh", 96.43, "python"]
# print(marks)
# print(marks[0])
# print(marks[-2])

# Slicing on list 

# print(marks[:])
# print(marks[2:6])
# print(marks[4:])
# print(marks[-5:-1])


#                                           Lec-05 - List methods (function)

# nums=[1,2,3]

# # append(value) - it's add and element to the end of the list
# nums.append(4)
# print(nums)

# inset(idx, value) - it's add an element in list, according to the index.
# nums.insert(2,10)
# print(nums)

# The insert(10, 39) uses index 10, exceeding the list's length of 4, so Python appends 39 to the end instead of 
# raising an error. The final list becomes [1, 2, 10, 3, 39]

# nums.insert(10,39)
# print(nums)

# # sort() - it is sort the list in ascending order
# nums.sort()
# print(nums)

# # sort(reverse=True - it is sort in desending order
# nums.sort(reverse=True)
# print(nums)

# # reverse() - it is an reverse the list
# nums.reverse()
# print(nums)


#                                           Lec-06 - using loops with lists

# list_num = [19,23,48,23,3,42,4]
# num=3
# idx = 0

# for val in list_num:
#     if(val == num):
#         print(f"{num} is found at index {idx}")
#         break
#     idx += 1


#                                           Lec-07 Tuple in python

# tup = (1,2,3,4,5)

# Accessing the tuple element.
# print(tup[3])

# Can't assign new value of tuple index. it can casue error
# tup[3] = 3
# print(tup)

# but over write the tuple value. assign new value to the tuple. 

# tup = (88,78,97, 34,5,4)
# print(tup)

# for val in tup:
#     print(val)


#                                           Lec-08 - Tuple Method

# t.index(val) - index method, print the index of value

# t = (2,3,4,2,4,5,2,4,5,6,2)

# print(t.index(2))

# t.count(val) - count the total value appeared in tuple

# print(t.count(2))


#                                           Lec-09 - Dictionary in python

# info = {
#     "name" : "sourabh",
#     "cgpa" : 9.2,
#     "subject" : ["math", "science"],
#     3.14: "PI"
# }

# # print the dict 

# print(info)

# # Accessing the value using key

# print(info["name"])

# # Dict is mutable

# info["cgpa"] = 9.6
# print(info)


#                                           Lec-10 - Dictionary methods

# print the all keys of dictionary 

# dict_key = info.keys()
# print(dict_key)

# # print the all values of dictionary 

# dict_val = info.values()
# print(dict_val)

# # pirnt all items of the dictionary (key:value) 

# dict_item = info.items()
# print(dict_item)

# # print the value through the key

# print(info.get("name"))
# print("end of get method")

# # update the dictionary. 

# info.update({
#     "city" : "kolhapur"
# })

# print(info)


#                                           Lec-11 - sets in python


# s = {1,2,3,4,5}
# print(s)

# # empty set is always consider as dictionary
# t = {}
# print(type(t))

# # do declare empty set consider following syntax

# x = set()
# print(type(x))


#                                           Lec-12 - Set Method

# p = {1,2,3,4,5}

# # p.add(val)        Add a value

# p.add(6)
# print(p)

# # p.remove(val)     Remove a value

# p.remove(2)
# print(p)

# # p.pop()           Remove a randome value from set

# p.pop()
# print(p)

# # a.union(b)     Return union of 2 sets 

# a = {33,22,55,44}
# b = {88,33,22,77}

# print(a.union(b))


# # p.intersion(set2) Return the inserseciton of two sets

# print("intersection")
# print(a.intersection(b))


# Restart jounney

# -----------------------------------------------------------------------------
# Lec 1: String in python
# -----------------------------------------------------------------------------
# print("\n Lec 1: String in python")

# word = "python "

# print("total character in string = ",len(word))

# Acces the string character by manually 

# print(word[0])
# print(word[1])
# print(word[2])
# print(word[3])
# print(word[4])

# Accessing the string character using loop

# print("\n \n ")
# for i in word:
#     print(i)


# Concatenate String using " + " operator

# w1 = "I love"
# w2 = "python"

# sentence = w1 + " " + w2
# print(sentence)

# word = "python"
# print("word = ",word)

# print("\n total character in word string : ",len(word))

# # Access the string character by manually using index.

# print("\n fourth index : ",word[4])
# print("\n zeroth index : ",word[0])
# print("\n fifth index : ",word[5])

# #Accessing the string character using loop

# print("\n Accessing the string character using loop")
# for ch in word:
#     print(ch)

# # Concatenate String using " + " operator

# word2 = "I Love"

# print("string 1 : ",word2)
# print("string 2 : ",word)

# sentence = word2 + " " + word
# print("\n",sentence)


# -----------------------------------------------------------------------------
# Lec 2: Slicing in String
# -----------------------------------------------------------------------------
# print("\n Lec 2: Slicing in String. It's creating another copy of the string ")

# word = "I want to see my to as a Global leader and guide to global for peace and environment fridenly Growth"

# print(word[24:31]) # print 24 index to 30. Last index is not included in python slicing. 

# print(word[:]) # Print string from start to end. blank means start from 0 to len-1. 

# print(word[6:]) # starting index 6 and ending index is blank means print upto the len-1

# print(word[-16:-7]) # here use -ve indexing but always starting index is less that ending index. 


# -----------------------------------------------------------------------------
# Lec :3 String Formatting - f-string and format string 
# -----------------------------------------------------------------------------
# print("\n Lec :3 String Formatting - f-string and format string ")

# Format string. 

# a = 5
# b = 10
# sum = a + b

# # Normal Formatting 

# print("Language is {} and it a best language for AI-ML-DS for now".format("python"))
# print("sum of {} and {} = {}".format(a,b,sum))

# # Index Based formatting

# print("avg of {1} and {0} is {2}".format(a,b,(sum/2)))

# # Value based formatting 

# print("values of {c} and {d}".format(c=29,d=38))

# # f-string formatting. 

# a = 48
# b = 70

# print(f"sum of {a} and {b} is {a + b}")
# print(f"avg of {a} and {b} is {(a + b)/2}")


# -----------------------------------------------------------------------------
# Lec 4: Lists in Python 
# -----------------------------------------------------------------------------
# print("\n Lec 4: Lists in Python ")

# list = [23,4,34,34,"sourabh",848.88]
# print(list)

# print(type(list))

# print(list[4])

# # sling in List - it's a another copy of the original list. last index is not included.  

# print(list[:])
# print(list[0:])
# print(list[:4])

# print(list[-4:-2])


# -----------------------------------------------------------------------------
# Lec 5: Lists method 
# -----------------------------------------------------------------------------
# print("\n Lec 5: Lists method ")


# dummy_list = [1,2,3]

# dummy_list.append(4); # append end of the list. 
# print(dummy_list)

# dummy_list.insert(2,10) # Inset value at specific index. must be pass index and value. also you can pass index len(list) + 10. 
# print(dummy_list)

# dummy_list.sort() # ascending order # show list in sorted format with ascending. 
# print(dummy_list)

# dummy_list.sort(reverse= True) # Reverse Order  # show list in un-sorted format with descending format. 
# print(dummy_list)

# dummy_list.reverse() # Exact reverse of the orignal list.
# print(dummy_list)



# -----------------------------------------------------------------------------
# Lec 6: Using loops with Lists
# -----------------------------------------------------------------------------
# print("\n Lec 6: Using loops with Lists ")

# list = [2, 3, 72, 36, 10, 48, 37, 48, 37]

# value = 10
# idx = 0

# # Linerar Search 

# for val in list:
#     if(val == value):
#         print(f"{val} found at index {idx}")
#     idx += 1


# -----------------------------------------------------------------------------
# Lec 7: Tuples in python
# -----------------------------------------------------------------------------
print("\n Lec 7: Tuples in python, Immutable sequence of values")

# Declare only value in tuple without comma after value means python consider as a single value with store as a variable. 
tup = (1)
amu = ("sourabh")

print(type(tup))
print(type(amu))

acutal_tuple = (84,)
autal_tuple_2 = ("kdf;ljdfl",)

print(type(acutal_tuple))
print(type(autal_tuple_2))

# can re-assign value for particular tuple index it's not apply on tuple becuase of tuple is immutable sequence of values. 

tuple = (38,38, 9,4, "sourabh", 38, "Indian")


# tuple([3]) = 30 # error - cannot assign to function call here

print(tuple[2:5
            ])
print(tuple[:])
print(tuple[-4:-1])

