Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def total():
	print(sum(range(1,10)))

	
>>> total()
45
>>> def funName(list,i):
	e=[]
	f=[]
	for v in list:
		if v%i==0:
			e.append(v)
		else:
			f.append(v)
	print(e)
	print(f)

	
>>> s=[1,2,3,4,5,6,7,8,9]
>>> funName(s,2)
[2, 4, 6, 8]
[1, 3, 5, 7, 9]
>>> def totList(n):
	z=[]
	for x in range(1,n+1):
		z.append(x)
		l=sum(z)
	return l

>>> sumList(2)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    sumList(2)
NameError: name 'sumList' is not defined
>>> totList(2)
3
>>> totList(9)
45
>>> totList(8)
36
>>> totList(7)
28
>>> 
