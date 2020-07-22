
import lxml
import requests
import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
import urllib.parse

data = '''<stuff>
    <users>
        <user x="2">
            <id>1000</id>
            <name>Vedant</name>
        </user>
        <user x="7">
            <id>1001</id>
            <name>Ujjwal</name>
        </user>
    </users>
</stuff>'''

tree = ET.fromstring(data)
lst_user = tree.findall('users/user')
print('User Count:', len(lst_user))
print('*****************')
for item in lst_user:

    print('Name:', item.find('name').text)
    print('ID:', item.find('id').text)
    print('Attribute:', item.get('x'))
    print('*****************')

# User Count: 2
# *****************
# Name: Vedant
# ID: 1000
# Attribute: 2
# *****************
# Name: Ujjwal
# ID: 1001
# Attribute: 7
# *****************


# Using Requests Module

data = requests.get(
    'http://py4e-data.dr-chuck.net/comments_759071.xml')
tree = ET.fromstring(data.text)
counts = tree.findall('.//count')
sum = 0
print(counts)
for count in counts:
    sum = sum+float(count.text)
print(sum)
