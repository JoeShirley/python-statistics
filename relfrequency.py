items = []
try:
    while 1:
        new = raw_input("Enter a number: ")
        if new.isdigit():
            items.append(int(new))
except KeyboardInterrupt:
    print "\nFinished getting data\n"
total = 0
for item in items:
    total += item

for item in items:
    div = item / float(total)
    print str(div) + '\n'

print "Done printing relative frequencies"
