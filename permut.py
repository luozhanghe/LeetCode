"""
leetcode 46题，给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
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
