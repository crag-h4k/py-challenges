def second(url):
	from urllib import request
	import re	
	
	raw = request.urlopen(url).read().decode()
	data = re.findall("<!--(.*?)-->", raw, re.DOTALL)[-1]
	solution = "".join(re.findall("[A-Za-z]", data))
	return solution

url = "http://www.pythonchallenge.com/pc/def/ocr.html" #"ocr.html"
solution = second(url)

print('second challenge:',solution)
print('http://www.pythonchallenge.com/pc/def/' + solution + '.html')
