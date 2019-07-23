Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def my_decorator(functionisone):
	def my_decorator_func(arg1,arg2):
		print('Вызов декоратора для функции. Сумма равна')
		functionisone(arg1,arg2)
	return my_decorator_func

>>> @my_decorator
def firstfun(arg1=10,arg2=15):
	print(arg1+arg2)
	return (arg1+arg2)

>>> res = firstfun(15, 25)
Вызов декоратора для функции. Сумма равна
40
>>> 
