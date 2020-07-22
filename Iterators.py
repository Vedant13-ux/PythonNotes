#map(function,list)-map() returns a special object that yields one result at a time as needed.
def fahrenheit(celsius):
    return (9/5)*celsius+32
temps=[0,22.5,40,100]
print(list(map(fahrenheit,temps)))
#Returns-->[32.0, 72.5, 104.0, 212.0]

print(list(map(lambda celsius:(9/5)*celsius+32,temps)))
#Returns-->[32.0, 72.5, 104.0, 212.0]

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

list(map(lambda x,y,z:x+y+z,a,b,c))
#Returns-->[15, 18, 21, 24]



#Generators-Generator functions allow us to write a function that can send back a value 
# and then later resume to pick up where it left off. 
# This type of function is a generator in Python,allowing us to generate a sequence of values over time. 
# The main difference in syntax willbe the use of a yield statement.The main difference is when a generator
# function is compiled they become an object that 
# supports an iteration protocol. That means when they are called in your code they don't 
# actually return a value and then exit
def gencubes(n):
    for x in range(n):
        yield n**3

for x in gencubes(10):
    print(x)

def genfibon(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b #simultaneous Update in Python

for x in genfibon(10):
    print(x)   


#reduce(function, sequence)-The function reduce(function, sequence) continually applies the function to the sequence. 
# It then returns a single value.
from functools import reduce

lst =[47,11,42,13]
reduce(lambda x,y: x+y,lst)#113

#Find the maximum of a sequence (This already exists as max())
max_find = lambda a,b: a if (a > b) else b
print(reduce(max_find,lst))
#47

#fiilter(function,sequence)-The function filter(function, list) offers a convenient way to filter out all 
# the elements of an iterable, for which the function returns True.The function needs to return a 
# Boolean value (either True or False). This function will be applied to every element of the iterable.
#  Only if the function returns True will the element of the iterable be included in the result.
lst=range(20)
list(filter(lambda x: x%2==0 ,lst))


#zip(sequence1,sequence2.....sequence(n))-Zips the sequneces and returns a tuple
x = [1,2,3]
y = [4,5,6,7,8]

# Zip the lists together
list(zip(x,y))
#Returns-->[(1, 4), (2, 5), (3, 6)]

d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

list(zip(d1,d2))
#Returns-->[('a', 'c'), ('b', 'd')]

list(zip(d2,d1.values()))
#Returns-->[('c', 1), ('d', 2)]

#zip() is equivalent to:

def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)

#enumerate(sequence,start_index)-->Enumerate allows you to keep a count as you iterate through an object.
#  It does this by returning a tuple in the form (count,element). The function itself is equivalent to:
def enumerate(sequence,start=0):
    n=start
    for elem in sequence:
        yield n,elem
        n+=1

        
lst = ['a','b','c']

for number,item in enumerate(lst):
    print(number)
    print(item)
#Return--> 
#a
#1
#b
#2
#c

months = ['March','April','May','June']
list(enumerate(months,start=3))
#[(3, 'March'), (4, 'April'), (5, 'May'), (6, 'June')]

#
#all() and any() are built-in functions in Python that allow us to conveniently check for boolean matching 
# in an iterable. all() will return True if all elements in an iterable are True. 
# It is the same as this function code:

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

#any() will return True if any of the elements in the iterable are True. It is equivalent to the following 
# function code:

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False


lst = [True,True,False,True]
all(lst)#-->False
any(lst)#-->True




#next()-->The next() function allows us to access the next element in a sequence. Lets check it out:

def simple_gen():
    for x in range(3):
        yield x

print(simple_gen())#0
print(simple_gen())#1
print(simple_gen())#2

#How to make a object iterator is by using the function iter()
s='hello'
s_iter=iter(s)
print(next(s_iter))#h
print(next(s_iter))#e
print(next(s_iter))#l
print(next(s_iter))#l
print(next(s_iter))#o










