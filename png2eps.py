

from PIL import Image

image_png = 'pic.png'
im = Image.open(image_png)

#im.show()

fig = im.convert(im.mode) 

fig.save('pic.eps', lossless = True)
