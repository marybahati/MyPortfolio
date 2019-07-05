Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[]
>>> b=[]
>>> for z in range(0,100):
	if z%9==0:
		a.append(z)
	elif z%11==0:
		b.append(z)

		
>>> a
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
>>> b
[11, 22, 33, 44, 55, 66, 77, 88]
>>> 
