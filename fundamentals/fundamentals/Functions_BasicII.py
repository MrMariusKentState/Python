#1 Countdown

def Countdown(x):
    while x >= 0:
        print(x)
        x = x - 1

Countdown(17)


#2 Print and Return

variable = [5, -13];

def print_and_return(x):
    print(x[0]);
    return(x[1]);

returned = print_and_return(variable)
print(returned)


#3 First plus length

Da_Bulls = [23, 33, 91, 7, 54, 25];

def First_plus_length(x):
    return(x[0]+len(x))

Bulls = First_plus_length(Da_Bulls)
print(Bulls)


#4 Values Greater than Second

Jersey_numbers = [23, 12, 4, 54, 38, -3]

def values_greater_than_second(x):
    newlist = [];
    count = 0;
    i = 0;
    while i < len(x):
        if x[i] > x[1]:
            newlist.append(x[i])
            count = count + 1
        i = i + 1
    print(count)
    return newlist

returned = values_greater_than_second(Jersey_numbers)
print(returned)


#5 This Length, that value

def this_length_that_value(size,value):
    newlist = []
    i = 0
    while i < size:
        newlist.append(value)
        i = i + 1
    return newlist

returned = this_length_that_value(5,7)
print(returned)