from functools import reduce

nums = [3,2,4,5,7,8,9]

evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n : n+2, evens))

sum = reduce(lambda a,b : a+b,doubles)



print(evens)
print(doubles)
print(sum)