Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = {'Фамилия':'Иванов','Имя':'Иван','Отчество':'Иванович'}
>>> dnew = {}
>>> for key in d.keys():
	dnew[d[key]] = key

	
>>> print(dnew)
{'Иванов': 'Фамилия', 'Иван': 'Имя', 'Иванович': 'Отчество'}
>>> 
