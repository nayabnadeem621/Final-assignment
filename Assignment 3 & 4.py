#  ASSIGNMENT NO. 3 

#  Q1 Write a Python program to print the following string in a specific format (see the
# output).

#                  Twinkle, twinkle, little star,
#                          How I wonder what you are!
#                                   Up above the world so high,
#                                   Like a diamond in the sky.

#                  Twinkle, twinkle, little star,
#                          How I wonder what you are
                
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# Q2 Write a Python program to get the Python version you are using

# import sys
# print("Python version:", sys.version)
# print("Python Version info. :", sys.version_info)

# Q3 Write a Python program to display the current date and time.

# import datetime
# now= datetime.datetime.now()
# print ("Current date and Time:") 
# print (now.strftime("%d-%m-%Y %H:%M:%S"))

# Q4 Write a Python program which accepts the radius of a circle from the user and compute the area.

# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# Q5 Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

# first_name =(input("your first name: "))
# last_name =(input("your last name: "))
# print(last_name, first_name)

# Q 6 Write a python program which takes two inputs from user and print them addition

# first_num = int(input("first number:" ))
# sec_num = int(input("second number:" ))
# total = first_num + sec_num

# print (total)

# or

# fname =(input("your first name: ", ))
# lname =(input("your last name: "))
# full_name= fname+" "+lname
# print(full_name)

# Q7 Write a program which takes 5 inputs from user for different subject’s marks, total it and generate mark sheet using grades ?


# print("input marks obtained in 5 different subjects")
# maths= int(input("Input Maths marks: "))
# Isl= int(input("Input Islamiat marks: "))
# english= int(input("Input English marks: "))
# computer= int(input("Input computer marks: "))
# urdu= int(input("Input urdu marks: "))

# obtained_marks= maths+ Isl+ english
# total_marks= 300

# perc = int((obtained_marks/total_marks*100))

# if perc <=100 and perc >=80:
#     print("Your Grade is A+ and your percentage is", perc)
# elif perc <80 and perc >=70:
#     print("Your Grade is A and your percentage is", perc)
# elif perc <70 and perc >=60:
#     print("Your Grade is B and your percentage is", perc)
# elif perc <60 and perc >=50:
#     print("Your Grade is C and your percentage is", perc)
# elif perc <50 and perc >=40:
#     print("Your Grade is D and your percentage is", perc)
# elif perc <40 and perc >=33:
#     print("Your Grade is E and your percentage is", perc)
# elif perc > 100 or perc < 0:
#     print("This is an inappropriate percentage please input correct marks")
# else:
#     print("fail")



# Q 8 Write a program which take input from user and identify that the given number is even or odd?

# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")

# Q 9 Write a program which print the length of the list?

# num=["ali",1,2.3,True]
# print(len(num))

# Q 10 Write a Python program to sum all the numeric items in a list?

# num = [2,4,2,5,7,9,23,4,5]
# numsum=0
# for i in num:
#     numsum+=i
# print('Sum of List: ',numsum)

# Q 11 Write a Python program to get the largest number from a numeric list.

# listnum = [19, 10, 45, 26, 6,45,25,89,32,6,105]
# print("Largest number of the list is:", max(listnum))

# Q 12 Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Write a program that prints out all the elements of the list that are less than 5.

# element= [2 ,42 ,18, 9, 6, 19,1 , 21,4 , 59]

# for a in element:
#     if a < 5:
#      print(a)
        
        
        
# ASSIGNMENT NO. 4


# Q1 Make a calculator using Python with addition , subtraction ,multiplication ,division and power.
 
# num1= float(input("enter first numbers :"))
# num2= float(input("enter second numbers :"))
# operator = str(input("enter operator "))


# if operator== "+":
#      print(num1 + num2)
#  elif operator== "-":
#      print(num1 - num2)
#  elif operator== "*":
#      print(num1 * num2)
#  elif operator== "/":
#      print(num1 / num2)
#  else:
#      print("error")

#  Q 2 Write a program to check if there is any numeric value in list using for loop.

#  def has_numeric_value(input_list):
#      for item in input_list:
#          if isinstance(item, (int, float)):
#              return True
#      return False

#  my_list = [1, 'apple', 3.14, 'banana', True]
#  result = has_numeric_value(my_list)

#  if result:
#      print("The list contains numeric values.")
#  else:
#      print("The list does not contain numeric values.")

# Q 3 Write a Python script to add a key to a dictionary.

#  d = {0:10, 1:20}
#  print(d)
#  d.update({2:30})
#  print(d)

#  Q 4 Write a Python program to sum all the numeric items in a dictionary.

#  def sumlist(items):
#         sumnum= 0
#         for x in items:
#             sumnum += x
#         return sumnum
#  print(sumlist([22,12,2]))

#  Q 5 Write a program to identify duplicate values from list.

#  l=[1,2,3,4,5,2,3,4,7,9,5]
#  l1=[]
#  for i in l:
#      if i not in l1:
#          l1.append(i)
#      else:
#          print(i)
        
#  Q 6 Write a Python script to check if a given key already exists in a dictionary

#  Fruits = {'a': "Apple", 'b':"Banana", 'c':"Carrot"}
#  key_to_lookup = 'a'
#  if key_to_lookup in Fruits:
#    print ("Key exist")
#  else:
#    print ("Key does not exist")