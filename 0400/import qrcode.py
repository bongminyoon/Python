import qrcode

data = "Hello, World!"

img = qrcode.make(data)

img.save("qrcode.png")
