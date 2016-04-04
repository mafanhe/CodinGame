import random

a=[random.randrange(50) for i in range(9)]
b=a[:]

b.sort()
print a
print b
sum_=sum(a)

avg=sum(b)*1.0/len(b)
half_sum=sum_/2

print sum_,avg
for i in a:
    sum_-=i
    if sum_<half_sum:
        print i
        break