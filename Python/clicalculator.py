operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if operation == "+":
   print(number_1 + number_2)

elif operation == "-":
   print(number_1 - number_2)

elif operation == "*":
    print(number_1 * number_2)

elif operation == "/":
   print(number_1 / number_2)

elif operation == "%":
   print(number_1 % number_2)

else:
    print("No operation entered")
 