'''
Exercise:
- Create different functions to represent all the possibilities in terms of returns and arguments.
- Check if it's possible to create a function inside another function.
- Use an example of a built-in function
- Test the LOCAL and GLOBAL variable's concept

Extra:
Create a function that gets 2 strings as arguments and return a number:
- The function must print all the numbers from 1 to 100
-- If the number is divisible by 3, print the first string
-- If the number is divisible by 5, print the second string
-- If the number is divisible by 3 and 5, print both strings concatenated
-- The function must return the number of times that none of the strings was printed
'''

var1: int = 10
var2: int = 20

var3: float = 30.0
var4: float = 40.0

def hello_world():
    print('hello world')

def sum_int(a: int, b: int) -> int:
    '''Sum two integers'''
    return (a+b)

def sum_float(a: float, b: float) -> float:
    '''Sum two floating point numbers'''
    return (a+b)

def show_name(name: str) -> None:
    '''Show a name'''
    print(name)

def sum_global_vars() -> float:
    global var1
    global var2
    global var3
    global var4
    return sum([var1, var2, var3, var4])

def sum_local_vars() -> float:
    var1 = 100
    var2 = 200
    var3 = 300
    var4 = 400
    return sum([var1, var2, var3, var4])

def print_numbers(str1: str, str2: str) -> int:
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(str1 + str2)
            continue
        if i % 3 == 0:
            print(str1)
            continue
        if i % 5 == 0:
            print(str2)
            continue
        print(i)
        count += 1
    return count

hello_world()
print(sum_int(var1, var2))
print(sum_float(var3, var4))
show_name('MoureDev')
print(sum_global_vars())
print(sum_local_vars())
print(type(var1))
print(type(var3))
print(print_numbers('MoureDev', 'AriasAntony'))
