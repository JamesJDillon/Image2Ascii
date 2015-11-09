from PIL import Image

img = Image.open('batman.jpg')
img = img.convert('LA')
img.save('greybatman.png')

ascii = {
	0: '@',
	10: '#',
	20: '$',
	40: '8',
	50: '&',
	70: '£',
	80: '^',
	90: '*',
	110: '.',
	120: ' '
}

WIDTH_STEP = 25
HEIGHT_STEP = 15

def getAverage(x, y):
	values = 0
	for i in range(x - WIDTH_STEP, x):
		for n in range(y - HEIGHT_STEP, y):
			test = img.getpixel((i, n))
			values += test[0]
	return values / (WIDTH_STEP * HEIGHT_STEP)

for x in range(WIDTH_STEP, 2072, WIDTH_STEP):
	for y in range(HEIGHT_STEP, 1225, HEIGHT_STEP):
		value = getAverage(x, y)
		print(ascii[min(ascii, key=lambda x:abs(x - value))], end="")
		# if img.getpixel((x, y)) == 0:
		# 	print("@", end="")
		# else:
		# 	print(".", end="")
	print("\n")
		#print(img.getpixel((x, y)))


# for x in range(WIDTH_STEP, 500, WIDTH_STEP):
# 	for y in range(HEIGHT_STEP, 500, HEIGHT_STEP):
# 		average = getAverage(x, y)
# 		print(ascii[min(ascii, key=lambda x:abs(x - average))], end="")
# 		# if img.getpixel((x, y)) == 0:
# 		# 	print("@", end="")
# 		# else:
# 		# 	print(".", end="")
# 	print("\n")
# 		#print(img.getpixel((x, y)))
