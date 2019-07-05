Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits=['banana','apple','mango','orange','melon']
>>> for fruit in fruits:
	print(fruits)

	
['banana', 'apple', 'mango', 'orange', 'melon']
['banana', 'apple', 'mango', 'orange', 'melon']
['banana', 'apple', 'mango', 'orange', 'melon']
['banana', 'apple', 'mango', 'orange', 'melon']
['banana', 'apple', 'mango', 'orange', 'melon']
>>> numbers=[1,2,3,4,5,6,7,8,9,]
>>> for number in numbers
SyntaxError: invalid syntax
>>> for number in numbers
SyntaxError: invalid syntax
>>> for number in numbers:
	print(number)

	
1
2
3
4
5
6
7
8
9
>>> fruits[0]
'banana'
>>> fruits[4]
'melon'
>>> fruits[0:4]
['banana', 'apple', 'mango', 'orange']
>>> fruits[3:5]
['orange', 'melon']
>>> fr
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    fr
NameError: name 'fr' is not defined

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> c=a+b
>>> c
[1, 2, 3, 4, 5, 6]
>>> d=a*3
>>> d
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> fruits
['banana', 'apple', 'mango', 'orange', 'melon']
>>> fruits.append('grapes')
>>> fruits
['banana', 'apple', 'mango', 'orange', 'melon', 'grapes']
>>> fruits.extend(['peach','kiwi'])
>>> fruits
['banana', 'apple', 'mango', 'orange', 'melon', 'grapes', 'peach', 'kiwi']
>>> fruits.remove('melon')
>>> fruits
['banana', 'apple', 'mango', 'orange', 'grapes', 'peach', 'kiwi']
>>> fruits.sort()
>>> fruits
['apple', 'banana', 'grapes', 'kiwi', 'mango', 'orange', 'peach']
>>> fruits.reverse()
>>> fruits
['peach', 'orange', 'mango', 'kiwi', 'grapes', 'banana', 'apple']
>>> fruits.pop()
'apple'
>>> fruits
['peach', 'orange', 'mango', 'kiwi', 'grapes', 'banana']
>>> del fruits[0]
>>> fruits
['orange', 'mango', 'kiwi', 'grapes', 'banana']
>>> fruits.replace('banana','dates')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    fruits.replace('banana','dates')
AttributeError: 'list' object has no attribute 'replace'
>>> fruits.replace('banana','apple')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    fruits.replace('banana','apple')
AttributeError: 'list' object has no attribute 'replace'
>>> numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> sum(numbers)
45
>>> sum(fruits)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    sum(fruits)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> min(numbers)
1
>>> max(numbers)
9
>>> fruits.append('banana')
>>> fruits
['orange', 'mango', 'kiwi', 'grapes', 'banana', 'banana']
>>> fruits.count('banana')
2
>>> n=range(10)
>>> for x in n
SyntaxError: invalid syntax
>>> for x in n:
	print(x)

	
0
1
2
3
4
5
6
7
8
9
>>> m=range(10,20)
>>> for x in m:
	print(x)

	
10
11
12
13
14
15
16
17
18
19
>>> for f in fruits:
	print(f)

	
orange
mango
kiwi
grapes
banana
banana
>>> e=[x*10 for x in a]
>>> e
[10, 20, 30]
>>> f=[x*2 for x in e]
>>> f
[20, 40, 60]
>>> g=range(25,50)
>>> h=[x*x for x in g]
>>> h
[625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]
>>> for x in g:
	h.append(x)

	
>>> h
[625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> h=[]
>>> for x in g:
	y=x*x
	h.append(y)

	
>>> h
[625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]
>>> v=[100,200,300,400,500]
>>> y[v/7 %]
SyntaxError: invalid syntax
>>> y[v%7]
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    y[v%7]
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> y[v/7]
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    y[v/7]
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> y[% x/7]
SyntaxError: invalid syntax
>>> y=[% of v/7]
SyntaxError: invalid syntax
>>> for x in v:
	y=v/7
	h.append

	
Traceback (most recent call last):
  File "<pyshell#98>", line 2, in <module>
    y=v/7
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> y=[v%7 for y in v]
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    y=[v%7 for y in v]
  File "<pyshell#99>", line 1, in <listcomp>
    y=[v%7 for y in v]
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> y=[z%7 for z in x]
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    y=[z%7 for z in x]
TypeError: 'int' object is not iterable
>>> x=[100,200,300,400,500]
>>> y=[z%7 for z in x]
>>> y
[2, 4, 6, 1, 3]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>>  for z in x:
	
SyntaxError: unexpected indent
>>> for z in x:
	q=z%7
	y.append(q)

	
>>> y
[2, 4, 6, 1, 3, 2, 4, 6, 1, 3]
>>> y=[z%7 for z in x]
>>> y
[2, 4, 6, 1, 3]
>>> a=range(99-109)
>>> b=[z*z for z in a]
>>> b
[]
>>> for x in a:
	s=x*
	
SyntaxError: invalid syntax
>>> for x in a:
	b=x*
	
SyntaxError: invalid syntax
>>> for x in a:
	b=x*x

	
>>> b
[]
>>> n=range(99-109)
>>> for x in n:
	print(x*x)

	
>>> x
[100, 200, 300, 400, 500]
>>> 
>>> 
>>> 
>>> 
>>> a=range(99-109)
>>> b=[x*x for x in a]
>>> b
[]
>>> for x in a:
	print(a*a)

	
>>> a
range(0, -10)
>>> a=range(99,109)
>>> b=[x*x for x in a}
SyntaxError: invalid syntax
>>> b=[x*x for x in a]
>>> b
[9801, 10000, 10201, 10404, 10609, 10816, 11025, 11236, 11449, 11664]
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>>  j=range(0,10)
SyntaxError: unexpected indent
>>> j=range(0,10)
>>> j
range(0, 10)
>>>  
