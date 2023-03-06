import qrcode
img = qrcode.make('https://www.linkedin.com/in/daniela-decoud-colev/')
img.save("dani-linkedin.png")