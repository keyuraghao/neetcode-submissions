class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # following is a good a viable solution to be done in an interview
        # this issue is that when getting the max count the time complexity becomes O(26n)
        count = {}
        left = 0
        longest_length = 0
        max_frequency = 0 # using this we can get the solution down to O(n) time
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            max_frequency = max(max_frequency,count[s[right]]) # for optimising the solution to O(n) time
            # while (right - left + 1) - max(count.values()) > k: # this is where the time complexity becomes O(26n) because we are trying to get the max value from the hash map
            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1

            longest_length = max(longest_length, right - left + 1)

        return longest_length