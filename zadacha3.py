Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mylist = [x for x in range(0,11)]
>>> mylist.extend(mylist)
>>> print(mylist)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> newlist=[]
>>> for obj in mylist:
	if (obj in newlist)==False:
		newlist.append(obj)

		
>>> print(newlist)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
