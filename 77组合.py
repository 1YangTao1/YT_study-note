n = 4
k = 2
def backstark(first=1,cur=[]):
    if len(cur)==k:
        return res.append(cur[:])
    else:
        for i in range(first,n+1):
            cur.append(i)
            backstark(i+1,cur)
            cur.pop()
res = []
backstark()
