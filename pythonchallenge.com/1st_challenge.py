def first():
#http://www.pythonchallenge.com/pc/def/map.html
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	clue = 'g fmnc wms bgblr rpylqjyrc gr zw fylb rfyrq ufyr amknsrcpq ypc dmp bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle sqgle qrpgle kyicrpylq gq pcamkkclbcb lmu ynnjw ml rfc spj'
	clue_1 = 'map'
	shift = 2
	chars = []
	for i in clue_1:
		if i.strip() and i in alphabet:
			chars.append(alphabet[(alphabet.index(i) + shift) % 26])
		else:
			chars.append(i)
	solution = ''.join(chars)

	return solution

solution = str(first())
print('first challenge\n', solution)
print('http://www.pythonchallenge.com/pc/def/' + solution + '.html')
