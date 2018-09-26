import math

xs = []
ys = []

def testInt(value):
    if value:
        test = list(str(value))
        searchfor = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if test[0] == '-' and len(test) > 1:
            start = 1
        else:
            start = 0
        for i in range(start, len(test), 1):
            if not test[i] in searchfor:
                return False
        return True
    else:
        return False


print "Welcome to the regression solver. Enter points with two integers seperated by a comma"
print "Ex: 1,4"

try:
    while 1:
        new = raw_input("Enter a point: ")
        if ',' in new:
            arg1, arg2 = new.split(',')
            if testInt(arg1) and arg2.isdigit():
                for i in range(int(arg2)):
                    xs.append(int(arg1))
                    ys.append(int(arg2))
except KeyboardInterrupt:
    print "\nFinished getting data\n"

sigxy = 0
sigxsq = 0
sigysq = 0
sigx = 0
sigy = 0
n = len(xs)
i = 0
for x in xs:
    y = ys[i]
    sigxy += x * y
    sigxsq += x ** 2
    sigysq += y ** 2
    sigx += x
    sigy += y
    i += 1

b = ((n * sigxy) - (sigx * sigy)) / float((n * sigxsq) - (sigx ** 2))

a = (sigy / float(n)) - (float(b) * (sigx / float(n)))

r = ((n * sigxy) - (sigx * sigy)) / math.sqrt(((n * sigxsq) - (sigx ** 2)) * ((n * sigysq) - (sigy ** 2)))

print "Equation is: %s + %sx" % (a, b)
print "r value is: %s" % r
