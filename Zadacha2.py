Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_list = [x for x in range(1,6)]
>>> print (my_list)
[1, 2, 3, 4, 5]
>>> my_list2=[x for x in range(1,7)]
>>> my_list.extend(my_list2)
>>> print(my_list)
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]
>>> my_set = set(my_list)
>>> print(my_set)
{1, 2, 3, 4, 5, 6}
>>> 
