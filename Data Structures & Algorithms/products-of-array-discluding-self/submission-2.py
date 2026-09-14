# we will sovle using the best time O(n) but we need space O(n) extra space 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2,-1,-1):
            postfix[i] = postfix[i+1] * nums[i+1]

        ans = []

        for i in range(n):
            ans.append(prefix[i] * postfix[i])
        
        return ans