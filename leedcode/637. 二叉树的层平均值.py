class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        def dfs(root,n):
            if not root:
                return 
            if n<len(counts):
                counts[n]+=1
                sums[n]+=root.val
            else:
                counts.append(1)
                sums.append(root.val)
            dfs(root.left,n+1)
            dfs(root.right,n+1)
        counts = []
        sums = []
        dfs(root,0)
        return [a/b for a,b in zip(sums,counts)]