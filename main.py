from PIL import Image

#Opens the image, converts it to greyscale and saves it.
img = Image.open('batman.jpg')
img = img.convert('LA')
#Thanks Lee!
img = img.rotate(90, expand=True)
img.save('greybatman.png')

'''The lower the value, the darker the average.
We use 'weightier' characters like @ for the dark colours, 
and more soft characters like "*" for the lighter colours.'''
characters = {
	0: '@',
	10: '#',
	20: 'N',
	30: '$',
	40: '8',
	50: '&',
	70: '£',
	80: '^',
	90: '*',
	100: '.',
	110: ' '
}


IMAGE_WIDTH, IMAGE_HEIGHT = img.size

STEP_WIDTH = 40
STEP_HEIGHT = 35

'''Gets the average of all pixel values within the step.
E.g, STEP_WIDTH = 10 and STEP_HEIGHT = 10. Adds up the values of all
100 pixels, divides it by 100 and returns the result. The average is used in
determining what character to use. The lower the value, the more bold the character.'''
def getAverage(x, y):
	count = 0
	for i in range(x - STEP_WIDTH, x):
		for n in range(y - STEP_HEIGHT, y):
			#Get the value of the pixel at every place within the step.
			pixl = img.getpixel((i, n))
			#getpixel returns a tuple, but we're only interested in the first element.
			count += pixl[0]
	#to find the average, add up all elements and divide by the number of elements.
	#Count contains all of the values added up, now we divide them by the number of pixels in each step.
	return count / (STEP_WIDTH * STEP_HEIGHT)

#Iterate over the whole image, taking steps defined earlier.
for x in range(STEP_WIDTH, IMAGE_WIDTH, STEP_WIDTH):
	for y in range(STEP_HEIGHT, IMAGE_HEIGHT, STEP_HEIGHT):
		#Get the average of all pixels within the last step.
		average = getAverage(x, y)
		'''This line is dense. Essentially, it searches the characters dictionary
		for the value that's closest to the average we got previous, and prints the
		corresponding character. We use end="" to avoids newlines.'''
		print(characters[min(characters, key=lambda x:abs(x - average))], end="")
	print("\n", end="")



