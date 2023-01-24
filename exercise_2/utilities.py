def mapArrayToMatrix(l, f):
	res = []

	for x in l:
		line = []
		for y in l:
			line.append(f(x, y))
		res.append(line)

	return res
