import sieve_gen

find = 100
gen = sieve_gen.sieve()
for i in range(find - 1):
	found = next(gen)
print found
assert found == 541
