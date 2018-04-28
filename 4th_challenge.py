#http://www.pythonchallenge.com/pc/def/linkedlist.html
#follow the chain
#<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough. -->
#nothing = 12345 and the next nothing is 44827
# 12345->44827->45439->94485->72198
# 12345->4487->72758->71301
def fourth():
	from urllib import request
	import re

	
	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
	first_nothing = str(12345)

	new_url = url + first_nothing
	nothing = [new_url]

	for i in range(400):

		raw = request.urlopen(nothing[i]).read().decode()
		#data = re.findall("<!--(.*?)-->", raw, re.DOTALL)[-1]
		next_nothing  = re.findall("[0-9]{5}", raw, re.DOTALL)
		
		string_nothing = str(next_nothing)
		new = string_nothing.strip("'[]")
		
		url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
		url = url + new
		nothing.append(url)
		
		print("raw",raw)
		print("next_nothing",next_nothing)
		print("new",new)
		print("url",url)
		print("i",i)

	print(nothing)
	return nothing

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
#solution = fourth()
print(fourth())
#print('fourth challenge:',solution)
#print('http://www.pythonchallenge.com/pc/def/' + str(solution) + '.php')
