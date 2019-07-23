Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1.101):
	if (i%3==0)&(i%5==0):
		print("FizzBuzz")
	elif (i%3==0):
		print("Fizz")
	elif (i%5==0):
		print("Buzz")
	else:
		print(i)
