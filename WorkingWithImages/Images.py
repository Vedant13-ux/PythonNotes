
from PIL import Image


mac = Image.open("example.jpg")
print(mac.size)  # (1993, 1257)
mac_crop = mac.crop((0, 0, 100, 100))
mac_crop.save("example2.jpg")
