# 题目描述，输入一个数组，找出第K个大的数字

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]


if __name__ == "__main__":
    s = Solution()
    i = s.findKthLargest([1, 3, 4], 3)
    print(i)
