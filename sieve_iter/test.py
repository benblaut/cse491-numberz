import sieve_iter

def test1():
	for i in sieve_iter.sieve():
		print i

		if i >= 10:
			break

	assert i == 11

def test2():
	for n, i in zip(range(10), sieve_iter.sieve()):
		print i

	assert i == 31

def test3():
	sieve = sieve_iter.sieve()
	i = iter(sieve)
	print i.next()
	print i.next()
	print i.next()
	assert i.next() == 11
	

test1()
print
test2()
print
test3()

