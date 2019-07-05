Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for x in range(900,950):
	if x%3==0 and x%5==0:
		print("Fizzbuzz")

		
Fizzbuzz
Fizzbuzz
Fizzbuzz
Fizzbuzz
>>> for x in range(900,950):
	if x%3==0 and x%5==0:
		print("{} Fizzbuzz")

		
{} Fizzbuzz
{} Fizzbuzz
{} Fizzbuzz
{} Fizzbuzz
>>> for x in range(900,950):
	if x%3==0 and x%5==0:
		print("{} Fizzbuzz".format(x))

		
900 Fizzbuzz
915 Fizzbuzz
930 Fizzbuzz
945 Fizzbuzz
>>> for x in range(900,950):
	if x%3==0 and x%5==0:
		print(x)

		
900
915
930
945
>>> for x in range(900,950):
	if x%3==0 and x%5==0:
		print(x)
	elif x%5==0:
		print("Fizz")
	elif x%3==0:
		print("buzz")
	else:
		print(x)

		
900
901
902
buzz
904
Fizz
buzz
907
908
buzz
Fizz
911
buzz
913
914
915
916
917
buzz
919
Fizz
buzz
922
923
buzz
Fizz
926
buzz
928
929
930
931
932
buzz
934
Fizz
buzz
937
938
buzz
Fizz
941
buzz
943
944
945
946
947
buzz
949
>>> for x in range(900,950):
	if x%3==0 and x%5==0:
		print("Fizzbuzz")
	elif x%5==0:
		print("Fizz")
	elif x%3==0:
		print("buzz")
	else:
		print(x)

		
Fizzbuzz
901
902
buzz
904
Fizz
buzz
907
908
buzz
Fizz
911
buzz
913
914
Fizzbuzz
916
917
buzz
919
Fizz
buzz
922
923
buzz
Fizz
926
buzz
928
929
Fizzbuzz
931
932
buzz
934
Fizz
buzz
937
938
buzz
Fizz
941
buzz
943
944
Fizzbuzz
946
947
buzz
949
>>> 
