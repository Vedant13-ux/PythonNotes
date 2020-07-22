# ******Number Method********

# Conver Into Heaxdecimal Numbder
hex(238)

# Conver Into Binary Number
bin(284)

# Power And Mod
pow(2, 4, 3)  # -->means (2*4)%3=1

round(3.142890, 2)  # -->Rounds to 2 Decimal Places

# *****String Methods*******

str = "hello"

#Uppercase and Lowercase
str.upper()
str.lower()

# For couting
str.count('o')

# For finding the Index of a letter
str.find('o')

# IF YOU WANT A STRING IN THE CENTER
str.center(20, 'z')
# 20-->Total Length of string
# z--> want the string -str in between z's
# Result-'zzzzzzzhellozzzzzzzz'

# For Checking AlphaNumeric Characters
str.isalnum()
str.isalpha()
# Uppercase and Lowercase 2
str.islower()
str.isnumeric()
str.isspace()  # -->Rreturns True is there is any space in the string
str.istitle()  # Returns True if first letter is Capital
str.endswith('o')

# split-Splits at every instance
str.split('e')  # -->Returns ['h','llo']
str.split('l')  # Returns--> ['he','','o']

# partition-Splits at only first instance
str.partition('e')  # -->Returns ('h','e','llo')
str.partition('l')  # -->Returns ('He', 'l', 'lo')


# *******Sets*******

s1 = {1, 2, 3, 4}

# add()-Adds items to set

s1.add(5)

# copy
s2 = s1.copy()

# differnece
s2 = {1, 2, 3, 4, 5}
s1.difference(s1)  # -->Returns the difference that is {5}

# difference_update-Removes the same elements betweeen s1 and s2 from s1
s1.difference_update(s2)

# discard()
s1.discard(2)  # -->Discards 2 from the set

# intersection()-Returns a new set with items which are common between two sets
s1.intersection(s2)

# intersection_update()-Returns the intersection and sets the set1 as the returned intersection set
s1.intersection_update(s2)

# isdisjoint()-Opposite of Intersection and returns a boolean
s1.isdisjoint(s2)

# issubset()-Returns whether s1 is a subset of s2 or not
s1.issubset(s2)  # Returns True

# issuperset()-oppsite of issubset()
s2.issubset(s1)  # Returns True

# symmetric_difference()-Oppsoite of interection(),returns a set with items which are unique in each set
s1.symmetric_difference(s2)

# sets the value of the returned set to s1
s1.symmetric_difference_update(s2)

# union()-Returns a set which is union of s1 and s2
s1.union(s2)

# update()-Returns a set which is union and sets the set to s1
s1.update(s2)


#********Dictionary********#

# Dictionary Comprehension
{x: x**2 for x in range(10)}

#Keys,Values,Items in Dictionary
d = {'k1': 1, 'k2': 2}
for k in d.keys():
    print(k)
# Returns--> k1 k2

for v in d.values():
    print(v)
# Returns--> 1 2

for item in d.items():
    print(item)
# Returns-->('k1', 1) ('k2', 2)


#*********Lists**********#

# List Comprehension
lst = [x for x in range(10)]
print(lst)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst = [x for x in range(20) if x % 2 == 0]
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

lst = ["Even" if(x % 2 == 0) else "odd" for x in range(20)]
#['Even', 'odd', 'Even', 'odd', 'Even', 'odd', 'Even', 'odd', 'Even', 'odd', 'Even', 'odd', 'Even', 'odd', 'Even', 'odd', 'Even', 'odd', 'Even', 'odd']

celsius = [0, 10, 20.1, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit)
#[32.0, 50.0, 68.18, 94.1]


