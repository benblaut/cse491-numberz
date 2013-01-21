import sieve_gen

for n, i in zip(range(10), sieve_gen.sieve()):
	print i

assert i == 31
