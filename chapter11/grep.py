# coding: utf-8
import re;

reg_str = raw_input("Enter a regular expression:");
fname = raw_input("Enter a file name:");
fhand = open(fname);
#fhand = open('../mbox.txt');
if fname.find('/') != -1:
	fname = re.findall('\/([^<>/\*?|:]+\.*$)', fname)[0]
count = 0;

for lines in fhand:
	if re.search(reg_str, lines):
		count = count + 1;
# 格式化序列
print "%s had %d lines that matched %s ." % (fname, count, reg_str);