
#Counter-Counts the Number of Unique values
from collections import Counter
mylist=[1,1,1,1,2,2,2,3,3]
Counter(mylist)
Counter('ashjdgahjsdjhasjd')#-->Even Counts the unique letteres n the strings
print(Counter(('Hey There I am Vedant,I am Called Vedant').split()))
#Retruns-->Counter({'am': 2, 'Hey': 1, 'There': 1, 'I': 1, 'Vedant,I': 1, 'Called': 1, 'Vedant': 1})

letters='aaaaaaaaasssssshhhhhhiiii'
c=Counter(letters)

#Common patterns when using the Counter() object

sum(c.values())                 #total of all counts
c.clear()                       #reset all counts
list(c)                         #list unique elements
set(c)                          #convert to a set
dict(c)                         #convert to a regular dictionary
c.items()                       #convert to a list of (elem, cnt) pairs
c.most_common()       #n least common elements
c+= Counter()                  #emove zero and negative counts


#******************************************************************************#
from collections import defaultdict
d={'a':20,'b':40}
#Suppose we call d['c'] then the Python returns a KeyError that the following key doesn't exist
#To solve this problem,we use "defaultdict",which returns a default value when we return a default value
d=defaultdict(lambda:0)
d['correct']=100
d['Wrong Key!']
print(d)
#Returns-->defaultdict(<function <lambda> at 0x00D4E1D8>, {'correct': 100, 'Wrong Key!': 0})

#******************************************************************************#
from collections import namedtuple
t=(10,20,30)#This is a simple tuple whose indexing start from 0
Dog=namedtuple('Dog',['age','breed','name'])
#Here is a namedtupled whose each index has a name call on it,and this has a type - "Dog"
robin=Dog(age=5,breed='mutt',name='robin')
print(type(robin))
#The result is mix of a tuple and a object
print(robin.age)





