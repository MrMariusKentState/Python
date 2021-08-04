num1 = 42    #variable declaration, number (data type)
num2 = 2.3   #variable declaration, number (data type)
boolean = True   #variable declaration, Boolean (data type)
string = 'Hello World'   #variable declaration, string (data type)
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #data type, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #data type, list, Boolean
fruit = ('blueberry', 'strawberry', 'banana') #data type, list
print(type(fruit))  #log statement
print(pizza_toppings[1])  #log statement
pizza_toppings.append('Mushrooms')  #data type, list: add value
print(person['name']) #log statement
person['name'] = 'George'  #data type, list: change value
person['eye_color'] = 'blue'  #data type, list: change value
print(fruit[2]) #log statement

if num1 > 45:               #conditional, if
    print("It's greater")   #log statement
else:                    #conditional, else
    print("It's lower")  #log statement

if len(string) < 5:  #conditional, length check
    print("It's a short word!")  #log statement
elif len(string) > 15:   #conditional, length check
    print("It's a long word!")  #log statement
else:                   #conditional
    print("Just right!") #log statement

for x in range(5):   #for loop
    print(x)    #log statement
for x in range(2,5):  #for loop
    print(x)    #log statement
for x in range(2,10,3):  #for loop
    print(x)    #log statement
x = 0    #variable define
while(x < 5):
    print(x)    #log statement
    x += 1    #increment

pizza_toppings.pop()    #data type, list: delete value
pizza_toppings.pop(1)   #data type, list: delete value

print(person)           #log
person.pop('eye_color')  #list,delete value
print(person)       #log

for topping in pizza_toppings:    #for loop, start
    if topping == 'Pepperoni':   #conditional, if
        continue               #continue
    print('After 1st if statement')    #log
    if topping == 'Olives':       #conditional, if
        break          #break

def print_hello_ten_times():  #function
    for num in range(10):  #loop
        print('Hello') #log

print_hello_ten_times()  #function call

def print_hello_x_times(x):  #function, parameter
    for num in range(x):  #loop
        print('Hello') #log

print_hello_x_times(4)  #function call, parameter

def print_hello_x_or_ten_times(x = 10):  #function, parameter
    for num in range(x):        #loop      
        print('Hello')          #log

print_hello_x_or_ten_times()    #log
print_hello_x_or_ten_times(4)   #log, parameter


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
