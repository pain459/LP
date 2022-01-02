def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)



print(queue_time([5, 3, 4], 1))