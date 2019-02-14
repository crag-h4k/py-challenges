#http://www.pythonchallenge.com/pc/def/equality.html
#One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

def third(url):
	from urllib import request
	import re

	raw = request.urlopen(url).read().decode()
	data = re.findall("<!--(.*?)-->", raw, re.DOTALL)[-1]
	solution = "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data))
	return solution

url = "http://www.pythonchallenge.com/pc/def/equality.html" #"ocr.html"
solution = third(url)

print('third challenge:',solution)
print('http://www.pythonchallenge.com/pc/def/' + str(solution) + '.php')
