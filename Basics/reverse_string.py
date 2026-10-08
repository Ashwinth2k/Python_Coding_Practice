#!usr/bin/python2

#Method : 1
#Write a Python program to reverse a string without using a built-in reverse function.
text = input("Enter a string: ")
reverse = ""
for char in text:
    reverse = char + reverse
print("Reversed string:", reverse)

#Method : 2
#Can you reverse a string using Python slicing?
text = "hello"
reverse = text[::-1]
print(reverse)

#Method : 3
#Reverse a string using reversed() function.
text = "hello"
reversed_text = "".join(reversed(text))
print(reversed_text)
