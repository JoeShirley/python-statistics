import sys


class stats():
    def __init__(self):
        self.items = []
        self.mean = 0
        self.mode = 0
        self.med = 0
        self.range = 0
        self.grouped = False
        self.num_groups = 0
        self.start()

    def testInt(self, value):
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

    def start(self):
        print "Input your numerical data here, press Control-C when finished"
        print "Split two numbers with a : to add a frequency. e.x. 3:12 would add 12 threes"
        g = raw_input("Do you want to group the data (y/n)? ").lower()
        while not (g == 'y' or g == 'n'):
            g = raw_input("Invalid! select 'y' or 'n'").lower()
        if g == 'y':
            self.grouped = True
            num = raw_input("How many groups (enter a whole number)? ")
            while not num.isdigit():
                num = raw_input("Enter a whole number: ")
            self.num_groups = str(num)
        else:
            self.grouped = False
        try:
            while 1:
                new = raw_input("Enter a number: ")
                if ':' in new:
                    arg1, arg2 = new.split(':')
                    if self.testInt(arg1) and arg2.isdigit():
                        for i in range(int(arg2)):
                            self.items.append(int(arg1))
                elif self.testInt(new):
                    self.items.append(int(new))
        except KeyboardInterrupt:
            print "\nFinished getting data\n"

        pop_sam = raw_input("Is this population or sample data? (pop/sam)").lower()
        while not (pop_sam == "sam" or pop_sam == "pop"):
            pop_sam = raw_input("Invalid! Input 'pop' for population or 'sam' for sample: ").lower()
        self.type = pop_sam
        self.items.sort()
        self.range = self.items[-1] - self.items[0]
        if self.grouped:
            split = int((int(self.range) / float(self.num_groups)) + 0.5)
            min = self.items[0]
            self.groups = {}
            bottom_val = min
            for i in range(0,int(self.num_groups),1):
                top_val = bottom_val + split - 1
                group = "%d-%d" % (bottom_val, top_val)
                self.groups[group] = 0
                for item in self.items:
                    if bottom_val <= item <= top_val:
                        self.groups[group] += 1
                bottom_val += split

        else:
            total = 0
            for item in self.items:
                total += item
            self.mean = (float(total) / len(self.items))
            self.med = self.median()


            mode_stuff = self.counter()
            modes = []
            biggest = 0
            for x, y in mode_stuff.items():
                if y > biggest:
                    modes[:] = []
                    modes.append(x)
                    biggest = y
                elif y == biggest:
                    modes.append(x)
                else:
                    pass
            m = ""
            for item in modes:
                m += "%s," % item
            self.mode = m.rstrip(',')

            self.vari = self.variance()
            self.std_dev = self.standard_dev()

    def median(self):
        data = self.items
        i = (len(data) / 2)
        if len(data) % 2:
            return data[i]
        else:
            return (data[i] + data[(i - 1)]) / 2.0

    def standard_dev(self):
        return float(self.variance()) ** 0.5

    def variance(self):
        total = 0
        for item in self.items:
            new = (float(item) - self.mean) ** 2
            total += new
        if self.type == "pop":
            return total / float(len(self.items))
        elif self.type == "sam":
            return total / float(len(self.items) - 1)
        else:
            print "Something went terribly wrong, try again"
            sys.exit(1)

    def rel_frequency(self):
        total = 0
        count = self.counter()
        stuff = {}
        for x, y in count.items():
            total += y

        for x, y in count.items():
            div = y / float(total)
            stuff[str(x)] = div
        return stuff

    def counter(self):
        dict_ = {}
        for new in self.items:
            if new in dict_:
                dict_[new] += 1
            else:
                dict_[new] = 1
        return dict_

    def show_rel_frequency(self):
        for x, y in self.rel_frequency().items():
            print "%s: %s" % (x, y)

    def show_counter(self):
        if self.grouped:
            for x, y in self.groups.items():
                print "%s: %s" % (x, y)
        else:
            for x, y in self.counter().items():
                print "%s: %s" % (x, y)

    def show_raw(self):
        i = 0
        for item in self.items:
            i += 1
            print "Index %d: %d" % (i, item)


current_table = 'one'
table_list = ['one']
globals()[current_table] = stats()
commands = ['help', 'show', 'refresh', 'exit', 'table']
values = ['rel_frequency', 'frequency', 'mode', 'median', 'mean', 'range', 'variance', 'std_dev', 'raw']


def help():
    print "Valid commands are:"
    print "help: display this prompt"
    print "show <value>: shows a value associated with your data"
    print "refresh: change the data in the table"
    print "table <name>: select a different table to view or make a new one"
    print "exit: quit the prompt"


def restart():
    globals()[current_table].start()


def show(thing):
    global current_table
    if thing in values:
        if thing == 'rel_frequency':
            print ""
            globals()[current_table].show_rel_frequency()
            print""
        elif thing == 'frequency':
            print ""
            globals()[current_table].show_counter()
            print ""
        elif thing == 'raw':
            print ""
            globals()[current_table].show_raw()
            print ""
        elif thing == 'mode':
            print '\n' + str(globals()[current_table].mode) + '\n'
        elif thing == 'median':
            print '\n' + str(globals()[current_table].med) + '\n'
        elif thing == 'mean':
            print '\n' + str(globals()[current_table].mean) + '\n'
        elif thing == 'range':
            print '\n' + str(globals()[current_table].range) + '\n'
        elif thing == 'variance':
            print '\n' + str(globals()[current_table].vari) + '\n'
        elif thing == 'std_dev':
            print '\n' + str(globals()[current_table].std_dev) + '\n'
        else:
            print "Invalid! Valid options are:"
            for item in values: print "\t%s" % item
    else:
        print "Valid options are:"
        for item in values: print "\t%s" % item


def table(arg):
    global current_table
    if arg in table_list:
        print "Switching to table %s" % arg
        current_table = arg
    else:
        print "Table %s does not exist, creating a new one of that name" % arg
        table_list.append(arg)
        current_table = arg
        globals()[current_table] = stats()

try:
    print "\nHere is an interactive prompt so that you can learn about your data"
    print "Try using the help command to see what you can do\n"
    while 1:
        command = raw_input("numberCruncher --> ").lower()
        command = command.split(' ')

        if command[0] in commands:
            if command[0] == "help":
                help()
            elif command[0] == "show":
                try:
                    show(command[1].lower())
                except IndexError:
                    print "You need to specify a value to show"
                    print "Valid values are:"
                    for item in values: print "\t%s" % item

            elif command[0] == "refresh":
                restart()
            elif command[0] == 'exit':
                print "All done, have a nice day"
                sys.exit(0)
            elif command[0] == 'table':
                try:
                    table(command[1])
                except IndexError:
                    print "Valid tables are:"
                    for i in table_list: print "\t%s" % i
            else:
                print "Invalid command\n"
                help()
        else:
            print "Invalid command!\n"
            help()


except KeyboardInterrupt:
    print "\nExiting, have a nice day!"
    sys.exit(0)
