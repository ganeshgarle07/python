# set does not allow duplicate,unordered, mutable
s = {1,2,3,3}
print(s)
s= set([1,2,3,4])
print(s)
s = set('Hello')
print(s)

# s = set()
# s.add(1)
# s.add(2)
# s.add(3)
# print(s)
# s.remove(3) # s.discard(3) s.clear() s.pop()
# print(s)

# for i in s:
#     print(i)


odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}

# union of odds
u = odds.union(evens)
print("-------1", u)

i = odds.intersection(evens)
print("-------inter", i)
i = odds.intersection(primes)
print("-------inter", i)

diff = evens.difference(primes)
print("-------diff--1", diff)
diff = primes.difference(evens)
print("-------diff--2", diff)

diff = evens.symmetric_difference(primes)
print("-------sym", diff)
