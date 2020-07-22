import json
data = '''
[
    {
        "id":"1000",
        "name":"Vedant",
        "x":"7"
    },
    {
        "id":"1001",
        "name":"Ujjwal",
        "x":"2"
    }
]'''

info = json.loads(data)
print('No. of People:', len(info))
for item in info:
    print('ID:', item['id'])
    print('Name:', item['name'])
    print('Attribute', item['x'])

# No. of People: 2
# ID: 1000
# Name: Vedant
# Attribute 7
# ID: 1001
# Name: Ujjwal
# Attribute 2
