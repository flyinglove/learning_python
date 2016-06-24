fname = raw_input('Enter file name:');

fhand = open(fname);

dicts = dict();

for lines in fhand:
	if lines.startswith('From '):
		line = lines.split();
		dicts[line[1]] = dicts.get(line[1], 0) + 1;
#print dicts;
max_send_num = None;
max_sender = None;
for item, value in dicts.items():
	if value > max_send_num:
		max_send_num = value;
		max_sender = item;
print max_sender, max_send_num;
