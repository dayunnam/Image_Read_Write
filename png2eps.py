from PIL import Image
#import sys

#print("Tyype (1)input-file and (2)output-file\n e.g., pic.png pic.eps\n"  )
#in_file=sys.argv[1]
#out_file=sys.argv[2]
#print("Input File Path : " + in_file)
#print("Output File Path : " + out_file)


image_png = 'pic.png'
im = Image.open(image_png)

#im.show()

fig = im.convert(im.mode) 

fig.save('pic.eps', lossless = True)
fig.save('pic.pdf', lossless = True)
