import sieve_iter

find = 100
sieve = sieve_iter.sieve()
i = iter(sieve)
for n in range(find - 1):
	found = i.next()
print found
assert found == 541
