class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i,curr,total):
            if total == target:
                ans.append(curr[:])
                return
            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i]) # adding the number (we are considering the branch)
            dfs(i,curr,total+ nums[i]) # going to the branch if we take the number

            curr.pop() # poping the number (we are not considering the branch)
            dfs(i+1,curr,total) # going to the branch if we do not take the number

        dfs(0,[],0)
        return ans

