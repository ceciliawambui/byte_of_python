types_of_people = 10 #A variable types_of_people assigned 10 to it
x = f"There are {types_of_people} types of people."#A variable assigned to it a string


binary= "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
#A variable assigned to it a string
print(x)
#prints out what is in x
print(y)
#Prints out what is in y
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)
