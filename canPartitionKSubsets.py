"""
698. 划分为k个相等的子集
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：

输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。

链接：https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets
"""


# class Solution:
#     def canPartitionKSubsets(self, nums, k: int) -> bool:
#         if k <= 0:
#             return False
#         if sum(nums) % k != 0:
#             return False
#         tmp, i, length, tmp2, j, m, n = sum(nums) // k, 0, len(nums), 0, 0, 0, 0
#         for i in range(k):
#             for j in range(m, length):
#                 tmp2 += nums[j]
#                 if tmp2 == tmp:
#                     n += 1
#                     m += j + 1
#                     break
#         if n == k:
#             return True
#         else:
#             return False
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)



if __name__ == "__main__":
    s = Solution()
    result = s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], k=4)
    print(result)
