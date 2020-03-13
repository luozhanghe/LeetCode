"""
169. 多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

链接：https://leetcode-cn.com/problems/majority-element
"""
class Solution:
    def majorityElement(self, nums: list) -> int:
        # 用一个字典把出现的值作为key, 出现的次数作为value存起来。
        dict_tmp = {}
        for i in range(len(nums)):
            if nums[i] not in dict_tmp.keys():
                dict_tmp[nums[i]] = 1
            else:
                dict_tmp[nums[i]] += 1
        # 用两个列表把key,value一一对应存起来
        # list1,list2 = [], []
        # for key, value in dict_tmp.items():
        #     list1.append(value)
        #     list2.append(key)
        # # 返回出现次数最多的一个数
        # return list2[list1.index(max(list1))]
        return max(dict_tmp.keys(), key=dict_tmp.get)

if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))