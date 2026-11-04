class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = max(nums)
        total_moves = 0
        for n in nums:
            if n < largest:
                total_moves += (largest - n)
        return total_moves
sol = Solution()
sol.minMoves([2, 1, 3])
        