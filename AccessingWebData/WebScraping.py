import requests
import lxml
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup)#-->REturns the HTML DOcument

# Select Takes in the CSS Selectors as the arguemnts
for item in soup.select('.toctext'):
    print(item.text)
# image_info = soup.select('.thumbimage')
# first_image = image_info[0]
# print(first_image['src'])
# image_link = requests.get(
#     'http://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
# f = open('my_new_file_name.jpg', 'wb')
# f.write(image_link.content)
# f.close()

# # Many Things

# base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
# start_two_title = []
# for i in range(51):
#     scrapes_url = base_url.format(i)
#     res = requests.get(scrapes_url)
#     soup = bs4.BeautifulSoup(res.text, 'lxml')
#     books = soup.select(".product_pod")
#     for book in books:
#         if(len(book.select('.star-rating.Two')) != 0):
#             start_two_title.append(book.select('a')[1]['title'])

# print(start_two_title)
