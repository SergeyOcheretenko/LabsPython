#Lab 2

import math
#1
def func1(a):
	if a >= 1:
		return math.cos(a) * (math.sin(a) ** 2)
	elif a > 0 and a < 1:
		return math.log(a) ** 2
	else:
		return 'no value'

a = float(input('Enter a: '))
print('Result: ' + str(round(func1(a), 10)))
print()

#2
def func2(b):
	if b < 0:
		return round(b ** (1/3), 10) % 1
	else:
		return math.sin(b) - 12 * math.cos(b) // 1

b = float(input('Enter b: '))
print('Result: ' + str(func2(b)))
print()

#3
c = input('Enter c: ')
if c < 'first':
	print('Result: ' + c + ', first') 
else:
	print('Result: ' + 'first, ' + c)
print()

#4-5
color = 41
while True:
	button = input("Press the button or enter 'exit': ")
	if button == 'exit':
		print("\033[31m\033[47m{}\033[0m".format('Good bye!'))
		break
	else:
		text = 'ASCII cod: ' + str(ord(button))
		print("\033[37m\033[" + str(color) + 
			"m{}\033[0m" .format(text))
		color += 1
		color = 41 if color == 47 else color
	print()
	print("Enter 'exit' for close the programm")
	print()