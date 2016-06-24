fname = raw_input('Enter a file name:');

fhand = open(fname);

dicts = dict();

for lines in fhand:
	if lines.startswith('From '):
		line = lines.split();
		dicts[line[2]] = dicts.get(line[2], 0) + 1;
print dicts;
