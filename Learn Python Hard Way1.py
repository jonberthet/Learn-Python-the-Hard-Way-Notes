
#REFERENCE : http://learnpythonthehardway.org/book/

#Set current Directory
cd /Users/jonathanberthet/Desktop/GDrive/Python/Raw

#Write text in test.py

#print test.py into terminal
python test.py

# Now, I can write code in Sublime Txt, save it, and see it in terminal every time I pass, python test.py


**************************
#Using Modulus & Variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

wadup = True
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % wadup

w = "This is the left side of..."
e = "a string with a right side."

print w + e
**************************
#Print a string 10 times
print "Ha" * 10

*************************
#Other great way to present data. prints out each
formatter = "%s %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("صباح الخير", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
*************************
# Three quotes """ keeps paragraph integrity instead of regular quotes

#\n puts whatever after it on new line

# \\ prints one \

#\" allows you to write " in strings
"I am 6'2\" tall."  # escape double-quote inside string
'I am 6\'2" tall.'  # escape single-quote inside string
\\ 				Backslash ()
\' 				Single-quote (')
\" 				Double-quote (")
\a 				ASCII bell (BEL)
\b 				ASCII backspace (BS)
\f 				ASCII formfeed (FF)
\n 				ASCII linefeed (LF)
\N{name} 		Character named name in the Unicode database (Unicode only)
\r ASCII 		Carriage Return (CR)
\t ASCII 		Horizontal Tab (TAB)
\uxxxx 			Character with 16-bit hex value xxxx (Unicode only)
\Uxxxxxxxx 		Character with 32-bit hex value xxxxxxxx (Unicode only)
\v 				ASCII vertical tab (VT)
\ooo 			Character with octal value ooo
\xhh 			Character with hex value hh

#examples
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

*************************
INPUTING DATA - EXACTLY WHAT I WANNA DO FOR BEER APP!!!!
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#Can also write (Gives same result as directly above):
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#Gives me an integer so I can use the value for math
number_for_math = int(raw_input())

#Run this in terminal...:
python test.py first, 2nd, 3rd

#to this code:
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

*****************
#Also a great a way to get input data from Users
from sys import argv

script, user_name = argv
ppl = '>Answer here '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(ppl)

print "Where do you live %s?" % user_name
lives = raw_input(ppl)

print "What kind of computer do you have?"
computer = raw_input(ppl)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)

*********************
#Get module and import argv filename. Use argv and raw_input to ask the user what file the user wants.
from sys import argv

script, filename = argv
#open file
txt = open(filename)
#print a line
print "Here's your file %r:" % filename
#call a fn on txt. I command the txt to read the whole file
print txt.read()
#Put new line and user enters txt after >
print "Type the filename again:"
file_again = raw_input("> ")
#Write out any file again
txt_again = open(file_again)
#print the new file
print txt_again.read()

***********************
#IMPORTANT COMMANDS for reading/closing files
close -- Closes the file. Like File->Save.. in your editor.
read -- Reads the contents of the file. You can assign the result to a variable.
readline -- Reads just one line of a text file.
truncate -- Empties the file. Watch out if you care about the file.
write(stuff) -- Writes stuff to the file.

#Example:
from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

***********************
Exercise 17: More Files
#Copy file info to another file 

#Copy one file to another
cat file1
#will print the contents of file1 to the standard output.

#The command:
cat file1 file2 > file3
#will sequentially print the contents of file1 and file2 to the file file3,
#truncating file3 if it already exists.

#Example:
#With 2 modules imported, I need to call 2 files like so:
#$ python test.py text.txt text2.txt
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line with: indata = open(from_file).read() . :) Now delete in_file.close() at bottom
in_file = open(from_file)
indata = in_file.read()


print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()


***********************
Exercise 19: Functions and Variables
#Many ways to reference a fn
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

****************************
Exercise 20: Functions and Files
#Use fn to print certain lines from text.txt file
from sys import argv

script, input_file = argv
#Reads whole f file
def print_all(f):
	print f.read()
#Seeks line 0 and starts writing/reading from there
def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First, let's print the whole file: \n"

print_all(current_file)

print "Now, let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print 3 lines."

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
****************************
Exercise 21: Fns can return something
#Diff ways functions can return things
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
**********************
#Ways I can call a fn
def secret_formula(started):
    jelly_beans = started * 10
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

#Once I returned the the variables above, I can call new variable names for the same fn
start_point = 10000
jon, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (jon, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
***********************
Exercise 25: Even More Practice
#I pass all these functions within python
#type:
python
#Then:
begin writing in variables and commands, do not write the functions

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

 **************************
 Exercise 30: Else if:
#This is a game decided by if/then statements w/in if/then statements. Can go forever :)
people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
 **************************
#Create list
hairs = ['brown', 'blond', 'red']

#FOR Loops
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists / create lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

#FYI: explanation of .append here: http://learnpythonthehardway.org/book/ex38.html

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

****************************
#WHILE Loops
#while-loop will keep executing the code block under it as long as a boolean expression is True.
#A for-loop can only iterate (loop) "over" collections of things. 
#A while-loop can do any kind of iteration (looping) you want. 
#However, while-loops are harder to get right and you normally can get many things done with for-loops.
#Cardinal numbers start at 0. Ordinal numbers start at 1
#ordinal == ordered, 1st; cardinal == cards at random, 0


************************
Exercise 35: Branches and Functions
#A fun game of if-then statements
from sys import exit

def gold_room():
    print "This room is full of gold.  How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()


************
Exercise 38: Doing Things to lists
#.append a while list. Create a list and add things to it.
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!
******************
Exercise 39: Dictionaries
#Navigate Dictionary
#Map of states and their abbreviations
states = { 
    'Oregon' : 'OR',
    'California' : 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    'Florida' : 'FL'
    }

#Map of state and city
cities = {
    'CA' : 'San Fran',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

#Add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print some cities
print '_' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities["OR"]

#print some states
print '_' * 10
print "Michigan abbrev. is: ", states['Michigan']
print "Oregon's abbrev. is: ", states['Oregon']

#print states using state, then city dicts
print '_' * 5
print 'Michigan has: ', cities[states['Michigan']]
print 'Florida has: ', cities[states['Florida']]

#print every state abbreviation
print '_' * 5
for state, abbrev in states.items():
    print "%s is abbreviated %s." % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now print both city and state
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

******************
Exercise 40: Modules, Classes, Objects
#Example of a class
#Python looks at MyStuff() and see's that it's a class
#Python makes an empty object w/ all the fns I've specified using the 'def'
class MyStuff(object):
#Python then sees I made an __init__ (ie - instantiate or create) fn and uses it to create newly created empty object
#In init fn, I get extra variable, 'self', which is empty object and I set variables on it
    def __init__(self):
#Here, i set object to tangerine to make a new object
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"

#Then, I can take new object (self.tangerine) and assign thing to it.
thing = MyStuff()
#both lines below print out apple and tangerine items
thing.apple()
print thing.tangerine

##**##
###VERY IMPORTANT
###Now, 3 ways to get things from things:

# dict style
mystuff['apples']

# module style
mystuff.apples()
print mystuff.tangerine

# class style
thing = MyStuff()
thing.apples()
print thing.tangerine

*************
Exercise 41: Speaking OOL


class :         Tell Python to make a new kind of thing.
object :        Two meanings: the most basic kind of thing, and any instance of some thing.
instance :      What you get when you tell Python to create a class.
def :           How you define a function inside a class.
self :          Inside the functions in a class, self is a variable for the instance/object being accessed.
inheritance :   The concept that one class can inherit traits from another class, much like you and your parents.
composition :   The concept that a class can be composed of other classes as parts, much like how a car has wheels.
attribute :     A property classes have that are from composition and are usually variables.
is-a :          A phrase to say that something inherits from another, as in a "salmon" is-a "fish."
has-a :         A phrase to say that something is composed of other things or has a trait, as in "a salmon has-a mouth."


class X(Y)
    "Make a class named X that is-a Y."
class X(object): def __init__(self, J)
    "class X has-a __init__ that takes self and J parameters."
class X(object): def M(self, J)
    "class X has-a function named M that takes self and J parameters."
foo = X()
    "Set foo to an instance of class X."
foo.M(J)
    "From foo get the M function, and call it with parameters self, J."
foo.K = Q
    "From foo get the K attribute and set it to Q." 

#Practice these equations with code here: 
# http://learnpythonthehardway.org/book/ex41.html

***********
Exercise 42: Is-A, Has-A, Objects, and Classes
# Mary is a kind of Salmon that is a kind of Fish. object is a class is a class.

#learn two catch phrases "is-a" and "has-a." 
Use the phrase is-a when you talk about objects and classes being related to each other by a class relationship. 
Use has-a when you talk about objects and classes that are related only because they reference each other.

is-a: Salmon is-a Fish               /inheritance of both methods and attributes
has-a: Salmon has-a gill (object)    /composition 

#classes made up of 2 things: variables (attributes) and methods (functions)
#Jon's answers: maybe right or wrong:
is-a / has-a

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

##Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## self.name is-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## self has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ##Employee has-a name
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## sata is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## Mary has-a pet 
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet called rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
bar()




***********
Exercise 43: Creating in Python + Design
#Follow this process

1   Write or draw about the problem.
2   Extract key concepts from #1 and research them.
3   Create a class hierarchy and object map for the concepts.
4   Code the classes and a test to run them.
5   Repeat and refine.

####FIX!!!!!###
from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "Scene not yet configured."
        print "Subclass it and implement enter()."
        enter(1)

class SceneFinal(Scene):
    def enter(self):
        return "This is the subclass of Scene"

class Engine(object):
    #When creating an Engine object, you give the map containing scenes to its constructor
    def __init__(self, scene_map):
        self.scene_map = "Engine __init__ has scene_map"
        self.scene_map = scene_map

    #The method which starts playing the scenes
    def play(self):
        #opening scene from map is selected as current scene
        current_scene = self.scene_map.opening_scene()
        print "Play's first scene", current_scene
        #now I loop all the scenes probably
        
        while True:
            print "\n___"
            #seems like next scene name is known in current scene
            next_scene_name = current_scene.enter()
            print "next scene", next_scene_name
            #replaces current scene with next scene from map
            current_scene = self.scene_map.next_scene(next_scene_name)
            print "map returns new scene", current_scene

class Death(Scene):

    quips = [
        "You died.  You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew.  You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an "
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body.  He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim.  Your laser hits his costume but misses him entirely.  This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into an insane rage and blast you repeatedly in the face until"
            print "you are dead.  Then he eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding.  It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container.  There's a keypad lock on the box"
        print "and you need the code to get the bomb out.  If you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb.  The code is 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print "You burst onto the Bridge with the netron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship.  Each of them has an even uglier"
        print "clown costume than the last.  They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door.  Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes.  It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference.  You get to the chamber with the escape pods, and"
        print "now need to pick one to take.  Some of them could be damaged"
        print "but you don't have time to look.  There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")


        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below.  As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time.  You won!"
            return 'finished'



class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
        }

    def __init__(self, start_scene):
        #Creates a variable in 'Map' called 'start_scene' containing opening scene
        self.start_scene = start_scene
        print "start_scene in __init__", self.start_scene
    #Returns a scene based on its name or key in the scenes array
    def next_scene(self, scene_name):
        print "start_scene in next_scene"
        val = Map.scenes.get(scene_name)
        print "next_scene returns", val
        return val
    #returns opening scene which is set up when I create the map
    def opening_scene(self):
        return self.next_scene(self.start_scene)




a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()


**************************
Exercise 44: Inheritance vs composition
#Implicit Inheritance of Parent traits
class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

#Override Parent Explicitly
class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()

#Alter Before or After
class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()

#Used together. Here, child 'is-a' relationship with a parent
class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

#Using super()
class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()


#Here, child and parent relationship is 'has-a'
#USEFUL STYLE TO CODE
#http://legacy.python.org/dev/peps/pep-0008/

#The question of "inheritance vs. composition" comes down to an attempt to solve the problem of reusable code.
# You don't want to have duplicated code all over your software, since that's not clean and efficient. 
#Inheritance solves this problem by creating a mechanism for you to have implied features in base classes.
# Composition solves this by giving you modules and the ability to simply call functions in other classes.




from sys import exit
from random import randint
     
     
     
    def main_hall():
        print "You are on the war ship. You need to get into the elevator to get to the bridge; where the General is."
        print "The whole destroyer is on alert and nearly every door is locked. There is a keypad on the elevator."
        print "There is a warning saying you only have 10 attemps, then the system deactivates and you cannot complete your mission. Be careful!"
     
        combination = "%d%d%d"  % (randint(1,9), randint(1,9), randint(1,9))
     
        guess = raw_input ("[Keypad:] ")
     
        guesses = 0
     
        while guess != combination and guesses < 10 and guess != "admin":
            print "*BZZT!* ERROR 2355: Incorrect combination!"
            guesses += 1
            guess = raw_input ("[Keypad:] ")
     
        if guess == combination:
            print "You open the elevator and start going up, fast. "
            return 'junction'
     
        elif guess == "admin":
            return 'junction'
     
        else:
            print "You have had more than 10 attempts! \n A small self destruct system in the lock blows you up!\n"
            return 'death'
     
     
     
     
    main_hall()
     
     
     
    def junction():
        print "When you get to the top, you are at a T-junction. Do you go left or right?"
        action = raw_input ("> ")
     
        if action == "left":
            print "You start running left, gun in hand, until you come across a turn, with some dark mist. You attempt to run through the mist, but you start to choke and you cannot get out. You die!"
            return 'death'
     
        elif action == "right":
            print "You start running down the right corridor, gun in hand. You finally make it to the brige where you must take control of the ship. You then reallize there is a crew of around 4-5 people. What do you do?"
            return 'bridge'
     
    def bridge():
        action = raw_input ("Kill;\nPretend you're one of them?\nRun?\n> ")
     
        if action == "kill":
            print "You click the safety off you rifle, and start opening fire. You manage to kill all but one of them. You try to shoot at the last man, but he is too fast! You see him initiate the self destruct! You die!"
            return 'death'
     
        elif action == "pretend":
            print "You walk into the bridge, casually. They dont make any signs of noticing at first, but then they see your uniform and start shouting questions at you. Then, they start shooting you. You start shooting back but it was too late. You die!"
     
        elif action == "run":
            print "You start running back the way you came, until  you find somebody else from you ship. You tell him about what happens, you go back and complete the mission. Congratulations!"
            return 'win'
     
     
    def win():
        print "Horray! You take control of the ship, and become a hero!"
        exit (1)
     
    def death():
        print "Well you really have failed this mission. GO HOME LOSER!"
        exit (1)
     
   

    result = junction()
    if result != "death":
        bridge()
        win()
        death() 


********************
Exercise 46: A Project Skeleton - Installing packages  ?? Cannot run tests
#Discover runtime of a test
#nosetests

*********************
Exercise 48 & 49 : Advanced User Input / Making Sentences   ???Don't know how to run these tests.

#First,
#Make it so users can write in a variety of answers, that work
#Breaking up a sentence. Here, I define a sentence as 'words separated by spaces'
#Use fn: .split()
stuff = raw_input('> ')
words = stuff.split()

#Second,
#create 'tuples', or a list that can't be modified. Created by two () w/ a comma, like a list
#Here, I create a pair (TYPE, WORD) that lets you look at the word and do things with it.
first_word = ('direction', 'north')
second_word = ('verb', 'go')
sentence = [first_word, second_word]



*********************
#Your First Website
#1st, create these directories and files:
$ cd projects
$ mkdir gothonweb
$ cd gothonweb
$ mkdir bin gothonweb tests docs templates
$ touch gothonweb/__init__.py
$ touch tests/__init__.py

#2nd, Put following code into bin/app.py
import web

urls = (
  '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        greeting = "Hello World"
        return greeting

if __name__ == "__main__":
    app.run() 

#3rd, in terminal run:
#Note, must run in higher directory, not w/in bin directory
$python bin/app.py

#4th, go to browser and put this code into URL:
http://localhost:8080/

#What's going on:
1    Your browser makes a network connection to your own computer, which is called localhost and is a standard way of saying "whatever my own computer is called on the network." It also uses port 8080.
2    Once it connects, it makes an HTTP request to the bin/app.py application and asks for the / URL, which is commonly the first URL on any website.
3    Inside bin/app.py you've got a list of URLs and what classes they match. The only one we have is the '/', 'index' mapping. This means that whenever someone goes to / with a browser, lpthw.web will find the class index and load it to handle the request.
4    Now that lpthw.web has found class index it calls the index.GET method on an instance of that class to actually handle the request. This function runs and simply returns a string for what lpthw.web should send to the browser.
5    Finally, lpthw.web has handled the request and sends this response to the browser, which is what you are seeing.

########
1st
#Put in bin/app.py
import web

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())
#New render variable, which is web.template.render object
#render object knows how to load .html files out of the templates/ directory because I told it to (passed it as that parameter)
render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting = "BONJOUR MONDE!"
#Now, isntead of just saying 'greeting = "Hello World" ', 
#I call render.index and pass the greeting to it as a variable
#The render.index is knows where the render fn is, knows I'm looking for 'index' in templates/, then "renders" or converts it.
#index (or foo) must be an html file       
        return render.foo(greeting = greeting)  

if __name__ == "__main__":
    app.run()

#OR########################
import web

urls = (
  '/hello', 'Index'
)


app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
#Instead of string for greeting, I use web.input to get data from browser
#web.input uses key=value and parses ?name=Frank that way.
    form = web.input(name="Nobody", greet=None)

    if form.greet:
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting = greeting)
    else:
        return "ERROR: greet is required."       #Gives me an error if greeting parameters not given

if __name__ == "__main__":
    app.run()



#############################




2nd
#Put in index.html (w/in template folder)
#this def says that this file takes a 'greeting' parameter
#you have the HTML in templates/index.html that looks at the greeting 
#variable and, if it's there, prints one message using #the $greeting, or #a default message.
$def with (greeting)

<html>
    <head>
        <title>Gothons Of Planet Percal #25</title>
    </head>
<body>

$if greeting:
    I just wanted to say <em style="color: green; font-size: 2em;">$greeting</em>.
$else:
    <em>Hello</em>, world!

</body>
</html>






