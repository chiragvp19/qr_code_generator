import qrcode as qr
img = qr.make("https://www.google.com/") 
img.save("Google.png") 