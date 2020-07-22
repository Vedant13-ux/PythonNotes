import urllib.request
import urllib.parse
import urllib.parse
import ssl
from twurl import augment

print('Calling TWitter.....')
url = augment('http://api.twitter.com/1.1/statuses/user_timeline.json',
              {"screen_name": "Vedant", "count": "2"})

print(url)
