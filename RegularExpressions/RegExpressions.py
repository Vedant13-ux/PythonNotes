import re
text = "The person's phone number is 408-555-1234. Call soon!"
pattern = 'phone'
print(re.search(pattern,text))#--> <re.Match object; span=(13, 18), match='phone'>
print(re.search(pattern,text).span())
match=re.findall('[a-z]',text)
print(match)
#['h', 'e', 'p', 'e', 'r', 's', 'o', 'n', 's', 'p', 'h', 'o', 'n', 'e', 'n', 'u', 'm', 'b', 'e', 'r', 'i', 's', 'a', 'l', 'l', 's', 'o', 'o', 'n']