"""
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list1 = []
        length = len(nums)
        # 从数组第一个元素开始遍历，找到数组其他值与其相加是否和target相等，相等则返回两个元素的下标
        for j in range(length):
            i = 1 + j
            while i < length:
                tmp = nums[j] + nums[i]
                i = i + 1
                if tmp == target:
                    list1.append(j)
                    list1.append(i - 1)
                    return list1


if __name__ == '__main__':
    A = Solution()
    nums = [-1, -2, -3, -4, -5]
    a = A.twoSum(nums, -8)
    print(a)
