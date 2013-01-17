import fib

for n, i in zip(range(3), fib.fib()):
    print i

# additional questions to address:
# - what the heck do 'zip' and 'range' do, and why are they there?
# "zip" iterates over two ranges, and "range" denotes a range from 0 to the number in parentheses (0-3, so a range of 4)
