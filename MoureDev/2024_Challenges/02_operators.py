"""
Exercise:
- Create examples of using each operator. Arithmetic, assignment, comparison, logical, identity and membership operators.
- Using operators, create examples of every control flow statement the language allows.
- Print the result of the examples on the console.

Extra:
- Create a program that prints the even numbers except the 16 and the 3 multiples between 10 and 55, included.
"""

# Variables
num1 = 10
num2 = 20

# Arithmetic operators
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 ** num2)
print(num1 // num2)

# Assignment operators
num1 += num2
print(num1)
num1 -= num2 
print(num1)
num1 *= num2
print(num1)
num1 /= num2
print(num1)
num1 %= num2
print(num1)
num1 **= num2
print(num1)
num1 //= num2
print(num1)

#Reseting variables
num1 = 10
num2 = 20

# Comparison operators
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

# Logical operators
print(num1 and num2)
print(num1 or num2)
print(not num1)

# Identity operators
print(num1 is num2)
print(num1 is not num2)

# Membership operators
print(str(num1) in str(num2))
print(str(num1) not in str(num2))

# Control flow statements
if num1 > num2:
    print("num1 is greater than num2")
elif num1 < num2:
    print("num1 is less than num2")
else:
    print("num1 is equal to num2")

loop_controler = num1
while loop_controler > 0:
    print(loop_controler)
    loop_controler -= 1

match num1:
    case 10:
        print("num1 is 10")
    case 20:
        print("num1 is 20")

try:
    num4 = num3
except NameError:
    print("num3 is not defined")
    num4 = -1
finally:
    print(num4)

# Extra: Print the even numbers except the 16 and the 3 multiples between 10 and 55, included.
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
