
fname = "mbox-short.txt"
fhand = open(fname)
for line in fhand:
    line =line.upper()
    print(line.strip())
