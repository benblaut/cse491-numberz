import sieve_iter

for n, i in zip(range(10), sieve_iter.sieve()):
	print i

assert i == 31
