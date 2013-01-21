def sieve():
	_primeslist = [2]

	while 1:
		yield next(_primeslist)

def _is_prime(primes, n):
    for i in primes:
        if n % i == 0:
            return False
    return True

def next(_primeslist):
    start = _primeslist[-1] + 1
    while 1:
        if _is_prime(_primeslist, start):
            _primeslist.append(start)
            return start

        start += 1
