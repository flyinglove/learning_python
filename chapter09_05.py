fname = raw_input('Enter a file name:');

fhand = open(fname);

dicts = dict();

for lines in fhand:
	if lines.startswith('From '):
		line = lines.split();
		domain_name = line[1].split('@');
		dicts[domain_name[1]] = dicts.get(domain_name[1], 0) + 1;
print dicts;