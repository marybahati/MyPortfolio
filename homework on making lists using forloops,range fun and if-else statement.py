Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lista=[]
>>> for a in range(0,100):
	if a%9==0:
		lista.append(a)

		
>>> lista
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
>>> 
>>> 
>>> listb=[]
>>> for b in range(0,100):
	if b%11==0:
		listb.append(b)

		
>>> listb
[0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> 
>>> 
>>> listc=lista+listb
>>> listc
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> listc.sort()
>>> listc
[0, 0, 9, 11, 18, 22, 27, 33, 36, 44, 45, 54, 55, 63, 66, 72, 77, 81, 88, 90, 99, 99]
>>> 
>>> 
>>> yearsx=[]
>>> for x in range(2019,2119):
	if x%4==0:
		yearsx.append(x)

		
>>> yearsx
[2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096, 2100, 2104, 2108, 2112, 2116]
>>> 
>>> 
>>> student1={'name':'Asha','yob':1998}
>>> student2={'name':'Sharon','yob':1997}
>>> student3={'name':'Eva','yob':1999}
>>> student4={'name':'Naima','yob':2000}
>>> student5={'name':'Gaya','yob':1995}
>>> students=[student1,student2,student3,student4,student5]
>>> for student in students:
	d=(2019-student['yob'])*365
	sms='Hello {},you are {} days old.'.format(student['name'],d)
	print(sms)

	
Hello Asha,you are 7665 days old.
Hello Sharon,you are 8030 days old.
Hello Eva,you are 7300 days old.
Hello Naima,you are 6935 days old.
Hello Gaya,you are 8760 days old.
>>> 
