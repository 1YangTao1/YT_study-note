nums = [1,1,1,2,2,3]
k = 2
res = []
dicts = {}
for i in nums:
    if i in dicts:
        dicts[i]+=1
    else:
        dicts[i]=1
for _ in range(k):
    p = 0
    m = 0
    for x in dicts:
        if dicts[x]>p:
            p=dicts[x]
            m = x
    dicts[m]=0
    res.append(m)
print(res)





