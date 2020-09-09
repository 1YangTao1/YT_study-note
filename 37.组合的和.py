candidates = [2,3,6,7]
target = 7
def backstack(cur,target,index):
    if target==0:
        return res.append(cur[:])
    for i in range(index,n):
        a = target-candidates[i]
        if a<0:
            break
        cur.append(candidates[i])
        backstack(cur,a,i)
        cur.pop()

n = len(candidates)
res = []
backstack([],target,0)
print(res)