# Functions with input

"""def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")"""

#Functions with more than 1 input

"""def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("asad", "dublin")"""

#positional ke pair arguments

"""def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with(name="ASAD", location="Dublin")"""


word1 = "true"
word2 = "love"

name1 = "usama"
name2 = "asad"


for number in range(len(name1)): #0,1,2,3
    if name1[number] == word1[number]:
        print(f"Matched letters: {name1[number]} and {word1[number]}")
    else:
        print(f"Unmatched letters: {name1[number]} and {word1[number]}")