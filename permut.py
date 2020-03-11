class Solution:
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        answer = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i + 1:]
            for y in self.permute(n):
                answer.append([num] + y)
        return answer


if __name__ == "__main__":
    s = Solution()
    list1 = s.permute([1, 2, 3])
    print(list1)
