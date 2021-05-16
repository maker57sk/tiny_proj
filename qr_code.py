import pyqrcode
from pyqrcode import QRCode

user_input = input('Enter a Url: ')
file_name = user_input.strip('https://www./')
url = pyqrcode.create(user_input)
url.svg(file_name+'.svg', scale=8)

print('{} is generated'.format(file_name))