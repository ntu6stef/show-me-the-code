#import the necessary lib
from PIL import Image, ImageDraw, ImageFont
import random
#open the photo to change
image = Image.open('Photos.jpg')
#create the draw object
draw = ImageDraw.Draw(image)
#create the num font object
font = ImageFont.truetype(font = 'ARLRDBD.TTF',size = 50)

#get image size
w,h = image.size
#create random number
def rndNum():
	return str(random.randint(0,11))
	
#the main
#draw the num on the draw object
draw.text((w-40,5),rndNum(),fill = 255,font = font)
image.save('photo.jpg')