#Operations on strings - membership, strip, replace

#membership  in , not in

fruits = ["apple", "banana", "cherry"]
print( "mango" in fruits)
print( "mango" not in fruits)

# let's try with dictionary

data = {1: "A", 2: "B"}

print(1 in data)
print("A" in data)  #false In Python, when you use the in operator with a dictionary, it checks only the keys, not the values.

print("A" in data.values()) #true

# strip   // The strip() method is used to remove leading and trailing whitespace (spaces, tabs, newlines) from a string

text= "   'vjiay'    'sunar'   "
print(text.strip())



raw_input="  south zone    "
cleaned= raw_input.strip()
print(f"region : {cleaned}")

texts = "-----Report------"
print(texts.strip("-"))   #You can also pass characters to remove:

# replace  // replace() is a string method used to change one part of a string to another.
# It finds a word or character and replaces it with something else

s1 = "hello im vijay"
print(s1.replace("vijay","sadaf"))

print(s1)