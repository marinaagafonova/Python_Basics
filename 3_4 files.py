d = {}
maths = 0;
physics = 0;
russian = 0;
count = 0;
with open("input.txt", 'r') as inf:
	for string in inf:
		temp = string.split(';')
		count +=1
		maths += int(temp[1])
		physics += int(temp[2])
		russian += int(temp[3])
		d[temp[0]] = (int(temp[1]) + int(temp[2]) + int(temp[3]))/3
with open("output.txt", 'w') as ouf:
	ouf.truncate(0)
	for value in d.values():
		ouf.write(str(value))
		ouf.write('\n')
	result = str(maths/count) + " " + str(physics/count) + " " + str(russian/count)
	ouf.write(result)
