import sieve_iter

for i in sieve_iter.sieve():
	print i

	if i >= 10:
		break

assert i == 11
