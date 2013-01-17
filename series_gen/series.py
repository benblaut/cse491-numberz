# this is an implementation of the 'series' functionality using
# a generator.

def adder():
    n = 0 #2
    while 1: #3 #8 #13
        n += 1 #4 #9 #14
        yield n #5 #10 #15
