Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[[1,2,3],[4,5,6],[7,8,9]]
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
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=(1,2,3,4)
>>> b=('a'.'b','c','d')
SyntaxError: invalid syntax
>>> b=('a','b','c','d')
>>> for x in a:
	print(x)

	
1
2
3
4
>>> c=list(a)
>>> c
[1, 2, 3, 4]
>>> d=[x for x in a]
>>> d
[1, 2, 3, 4]
>>> a
(1, 2, 3, 4)
>>> f=a+b
>>> f
(1, 2, 3, 4, 'a', 'b', 'c', 'd')
>>> a*3
(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
>>> 'b' in b
True
>>> 'e' in b
False
>>> 's' in a
False
>>> 'i' in a
False
>>> y=(x)
>>> y
4
>>> x=[1,2,3,4]
>>> y=(x)
>>> y
[1, 2, 3, 4]
>>> y=(z for z in x)
>>> y
<generator object <genexpr> at 0x034C8C70>
>>> a=[1,2,3,1,4,2,5,3,7]
>>> b=set(a)
>>> b
{1, 2, 3, 4, 5, 7}
>>> c=['a','b','a','c','c']
>>> c
['a', 'b', 'a', 'c', 'c']
>>> c={'a','b','a','c','c'}
>>> c
{'c', 'b', 'a'}
>>> d={'a','A','b','B'}
>>> d
{'A', 'B', 'b', 'a'}
>>> d={'a','A','b','B','a','b'}
>>> d
{'A', 'B', 'b', 'a'}
>>> s1={1,2,3,4}
>>> s2={3,4,5,6}
>>> s2.add(7)
>>> s2
{3, 4, 5, 6, 7}
>>> s2.remove(7)
>>> s2
{3, 4, 5, 6}
>>> s1.discard(4)
>>> s1
{1, 2, 3}
>>> s2.remove(7)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s2.remove(7)
KeyError: 7
>>> s1.discard(4)
>>> s2.difference(s1)
{4, 5, 6}
>>> s1.difference(s2)
{1, 2}
>>> s1.intersection
<built-in method intersection of set object at 0x034C2828>
>>> 

>>> 

>>> 

>>> 

>>> 9
>>>  s1.intersection(s2)
SyntaxError: unexpected indent
>>> s1.intersection(s2)
{3}
>>> s2.intersection(s1)
{3}
>>> s2.union(s1)
{1, 2, 3, 4, 5, 6}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6}
>>> s2.update({10,11,12})
>>> s2
{3, 4, 5, 6, 10, 11, 12}
>>> codes={'kenya':254, 'uganda':256, 'tanzania':255}
>>> codes['kenya']
254
>>> codes['kenya']=250
>>> codes
{'kenya': 250, 'uganda': 256, 'tanzania': 255}
>>> codes['rwanda']=252
>>> codes
{'kenya': 250, 'uganda': 256, 'tanzania': 255, 'rwanda': 252}
>>> codes.pop
<built-in method pop of dict object at 0x0093A2D0>
>>> codes.pop('rwanda')
252
>>> codess
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    codess
NameError: name 'codess' is not defined
>>> codes
{'kenya': 250, 'uganda': 256, 'tanzania': 255}
>>> codes.keys()
dict_keys(['kenya', 'uganda', 'tanzania'])
>>> codes values()
SyntaxError: invalid syntax
>>> codes.values
<built-in method values of dict object at 0x0093A2D0>
>>> codes.values()
dict_values([250, 256, 255])
>>> for key in codes.keys():
	print(key)

	
kenya
uganda
tanzania
>>> for value in codes.values():
	print(values)

	
Traceback (most recent call last):
  File "<pyshell#99>", line 2, in <module>
    print(values)
NameError: name 'values' is not defined
>>> for value in codes.values():
	print(x)

	
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
>>> fox x in codes.values():
	
SyntaxError: invalid syntax
>>> for x in codes.values():
	print(x)

	
250
256
255
>>> m=dict()
>>> m['a']=10
>>> m['b']=20
>>> n
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> m
{'a': 10, 'b': 20}
>>> n=range(10)
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
>>> n=range(11)
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
10
>>> for x in range(11):
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
10
>>> z=[x*x for x in n]
>>> z
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> m=dict(z)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    m=dict(z)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> a=['a','b','c','d','e','f','i','j','k']
>>> a=range[11]
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    a=range[11]
TypeError: 'type' object is not subscriptable
>>> a=range(10)
>>> for x in a:
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
>>> y=[x*x for x in a]
>>> y
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> z=dict
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
>>> 


>>> z=dict()
>>> z
{}
>>> z['a']=0
>>> z['b']=81
>>> z
{'a': 0, 'b': 81}
>>> range.values
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    range.values
AttributeError: type object 'range' has no attribute 'values'
>>> for x in z.values():
	print(x)

	
0
81
>>> m=dict()
>>> m['key']=0,1,2,3,4,5,6,7,8,9
>>> m['value']=0,1,2,9,16,49,64,81
>>> m
{'key': (0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 'value': (0, 1, 2, 9, 16, 49, 64, 81)}
>>> m=dict()
>>> m['n']=n*n
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    m['n']=n*n
TypeError: unsupported operand type(s) for *: 'range' and 'range'
>>> m[0]=o*0,m[1]=1*1,m[2]=2*2,m[3]=3*3,m[4]=4*4,m[5]=5*5,m[6]=6*6,m=7*7,m[8]=8*8,m[9]=9*9
SyntaxError: can't assign to operator
>>>  m[0]=0*0,m[1]=1*1,m[2]=2*2,m[3]=3*3,m[4]=4*4,m[5]=5*5,m[6]=6*6,m=7*7,m[8]=8*8,m[9]=9*9
SyntaxError: unexpected indent
>>> m[0]=0*0,m[1]=1*1,m[2]=2*2,m[3]=3*3,m[4]=4*4,m[5]=5*5,m[6]=6*6,m=7*7,m[8]=8*8,m[9]=9*9
SyntaxError: can't assign to operator
>>> b=dict()
>>> for p in range(10):
	m[p]=p*p

	
>>> 
>>> print(m)
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> fruits=['melon','pineapple','mangoes','banana','kiwi','passion','peach','strawberry','pears','avocado']
>>> k=dict()
>>> for x in fruits:
	k[x]=len x
	
SyntaxError: invalid syntax
>>>  for x in fruits:
	k[x]=lenx
	
SyntaxError: unexpected indent
>>> for x in fruits:
	k[x]=len x
	
SyntaxError: invalid syntax
>>> for x in fruits:
	k[x]=lenx

	
Traceback (most recent call last):
  File "<pyshell#177>", line 2, in <module>
    k[x]=lenx
NameError: name 'lenx' is not defined
>>> for x in fruits:
	k[x]=lenx
	print(x)

	
Traceback (most recent call last):
  File "<pyshell#180>", line 2, in <module>
    k[x]=lenx
NameError: name 'lenx' is not defined
>>> for x in fruits:
	k[x]=len(x)

	
>>> print(k)
{'melon': 5, 'pineapple': 9, 'mangoes': 7, 'banana': 6, 'kiwi': 4, 'passion': 7, 'peach': 5, 'strawberry': 10, 'pears': 5, 'avocado': 7}
>>> 
