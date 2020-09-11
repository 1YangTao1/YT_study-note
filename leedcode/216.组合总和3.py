k = 3
n = 7
keep = [x for x in range(1,10)]
def backstack(cur,n,index):
    if n==0 and len(cur)==k:
        return res.append(cur[:])
    for i in range(index,len(keep)):
        a = n-keep[i]
        if a<0:
            break
        cur.append(keep[i])
        backstack(cur,a,i+1)
        cur.pop()
res = []
backstack([],n,0)
print(res)