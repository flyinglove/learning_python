import re;

fname = raw_input("Enter a file name:");

fhand = open(fname);
inp = fhand.read();
count = 0;
#print inp;
lst = re.findall('[0-9]+', inp);

for num in lst:
	num = float(num);
	count = count + num;
lst.sort()
print lst;
#sums = sum(lst);
#lens = len(lst);

print count;