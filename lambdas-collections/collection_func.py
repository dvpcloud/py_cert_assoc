from functools import reduce
#map
domain = [1,2,3,4,5]

#function f(x) = x * 2
domain_range = map(lambda num: num * 2, domain)

print(domain_range) #map object
print(list(domain_range))

#filter
evens = filter(lambda num : num % 2 == 0, domain)
print(evens) # filter object
print(list(evens))

#reduce
domain_sum = reduce(lambda accum, num: accum + num,domain,0)
print(domain_sum)

#sorted with key
words = ['fig','Fourth','Cat','Boss','Apple','cup','angel','belt']

print(sorted(words))
print("sorted with key function")
print(sorted(words,key=str.lower, reverse=False))
print("using sort method using key")
words.sort(key=lambda s: s.lower(),reverse=True)
print(words)