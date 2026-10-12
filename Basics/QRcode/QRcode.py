# #!usr/bin/python3
# Install Packages Using Terminal Before Running This Code
# pip install pyqrcode
# pip install pypng

#Import QRcode from pyqrcode
import pyqrcode as qr
import png
from pyqrcode import QRCode

#String which represents the QR code
S = "https://www.linkedin.com/in/ashwinth2000/"

#Generate QR code
url = qr.create(S)

#Create and save the svg file nameing "myqr.svg"
url.svg("myqr.svg", scale =8)

#Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)
