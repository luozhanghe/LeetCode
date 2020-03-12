"""
56. 合并区间
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:

    def merge(self, intervals):
        #先把intervals按照第一个值进行排序
        intervals.sort()
        n = len(intervals)
        if n == 0:
            return []
        result = [intervals[0]]
        for i in range(1,n):
            #此时必有重合，则重合区间的右值为最大的那个
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1],intervals[i][1])
            #无重合则直接添加区间
            else:
                result.append(intervals[i])
        return result



if __name__ == '__main__':
    s = Solution()
    result = s.merge([[1,4],[1,2],[5,8]])
    print (result)
