# coding: utf-8
import re;

reg_str = raw_input("Enter a regular expression:");

fhand = open('../mbox.txt');

count = 0;

for lines in fhand:
	if re.search(reg_str, lines):
		count = count + 1;
# 格式化序列
print "mbox-txt had %d lines that matched %s ." % (count, reg_str);