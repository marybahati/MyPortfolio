Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> flat=[[1,2,3],
	  [4,5,6],
	  [7,8,9]]
>>> print([flat[0],[1],[2]])
[[1, 2, 3], [1], [2]]
>>> print([flat=[]
	   
SyntaxError: invalid syntax
>>> print([flat[])
	  
SyntaxError: invalid syntax
>>> print([flat[]]
	  
SyntaxError: invalid syntax
>>> print([flat[0]])
	  
[[1, 2, 3]]
>>> print([flat[0],flat[1],flat[2]])
	  
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> print([flat0,flat1,flat2])
	  
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print([flat0,flat1,flat2])
NameError: name 'flat0' is not defined
>>> flat
	  
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> a=1,2,3
	  
>>> b=4,5,6
	  
>>> c=7,8,9
	  
>>> flat=a+b+c
	  
>>> flat
	  
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> flat=[a+b+c]
	  
>>> flat
	  
[(1, 2, 3, 4, 5, 6, 7, 8, 9)]
>>> flat=[x for x in a+b+c]
	  
>>> flat
	  
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> squares=[x* for x in flat]
	  
SyntaxError: invalid syntax
>>> squares=[x* for x in a,b,c]
	  
SyntaxError: invalid syntax
>>> squares=[x* for x a+b+c]
	  
SyntaxError: invalid syntax
>>> squares=[flat* for x in flat]
	  
SyntaxError: invalid syntax
>>> squares=[a*+b*+c*]
	  
SyntaxError: invalid syntax
>>> squares=[x* for x in flat]
	  
SyntaxError: invalid syntax
>>> d=[x* for x in a]
	  
SyntaxError: invalid syntax
>>> d
	  
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> squares=[x*x for x in flat]
	  
>>> squares
	  
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>>   
