candidates = [10,1,2,7,6,1,5]
target = 8
candidates.sort()
def backstack(cur,target,index):
    if target==0:
        if cur in res:
            return 
        else:
            return res.append(cur[:])
    for i in range(index,n):
        a = target-candidates[i]
        if a<0:
            break
        cur.append(candidates[i])
        backstack(cur,a,i+1)
        cur.pop()

n=len(candidates)
res = []
backstack([],target,0)
print(res)

