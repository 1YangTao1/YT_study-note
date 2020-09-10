n = 4
res = ['1']
r = 1
while r<n:
    p,q = 0,1
    tmp = []
    r+=1
    while q<=len(res):
        if q==len(res):
            tmp.extend([str(q-p),res[p]])
        elif res[p]!=res[q]:
            tmp.extend([str(q-p),res[p]])
            p = q
        q+=1
    res = tmp
print(res)