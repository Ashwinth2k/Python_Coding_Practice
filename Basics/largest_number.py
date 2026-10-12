#!usr/bin/python3

#Method : 1
#Write a Python program to find the largest number in a list without using max().
numbers = [-10,-25,-7,-40,-34]
largest = numbers [0]
for i in numbers:
   if i > largest:
      largest = i
print("Largest number:", largest)

#Method : 2
#Use in-built function max() to find largest number.
numbers = [35, 12, 89, 4, 56, 23]
largest = max(numbers)
print("Largest number:", largest)
