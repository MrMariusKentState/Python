# 1. TASK: print "Hello World"

print("Hello World");

# 2. print "Hello Noelle!" with the name in a variable

name = "Noelle";

print("Hello",name); # with a comma
print("Hello" + name);	# with a +

# 3. print "Hello 42!" with the number in a variable

name = 42;
print("Hello", name);	# with a comma
#print(Hello + name);	# with a +	-- this one should give us an error! (It does. "Hello" should be in quotation marks).


# 4. print "I love to eat sushi and pizza." with the foods in variables

fave_food1 = "sushi";
fave_food2 = "pizza";
print("I love to eat {} and {}.".format(fave_food1,fave_food2)); # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}."); # with an f string


#5.  List functions

list = [3, 7, 8.5, 9, -2, -12, -8]

print(max(list));
sort = sorted(list);
print(sort);
print((list[:2]));
print((list[4:]));
print((list[3:5]));




