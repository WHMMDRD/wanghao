def fun(string):
	if(len(string)==0|len(string)==1):
		return string
	else:
		return  fun(string[1:])+string[0]
 string="abcd"
print(fun(string))