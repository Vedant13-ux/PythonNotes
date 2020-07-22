import urllib.request
import urllib.parse
import urllib.error
import ssl
import bs4
import requests
#*******Basic Requests******#
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())


#******COunting Words********#
for line in fhand:
    counts = dict()
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0)+1
    print(counts)

#******Interacting With HTML********#

# Ignore SSL Certificate Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter-')
html = urllib.request.urlopen(
    'https://yelp-camp-vedant.herokuapp.com/campgrounds', context=ctx).read()

soup = bs4.BeautifulSoup(html, 'lxml')
campgrounds = soup.select('.card')
for campground in campgrounds:
    img_src = requests.get(campground.select('img')[0]['src'])
    file_name = f"camp-{campground.select('h5')[0].text}"
    f = open(file_name, 'ab')
    f.write(img_src.content)
    f.close()

for campground in campgrounds:
    title = campground.select('h5')[0].text
    print(title.strip())
