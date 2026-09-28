class Solution:
    def maximumCandies(self, candies, k):
        left = 1
        right = max(candies)
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            children = 0

            for pile in candies:
                children += pile // mid

            if children >= k:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer