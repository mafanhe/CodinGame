__author__ = 'mafanhe'

n = int(input())
a = 0
l = []

for i in input().split():
    v = int(i)
    l.append(v-a)
    a = v

max_loss = 0
sum_num = 0
for i in l:
    sum_num += i
    if sum_num > 0:
        sum_num = 0
    if sum_num < max_loss:
        max_loss = sum_num

print(max_loss)
