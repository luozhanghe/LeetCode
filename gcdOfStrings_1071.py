"""
1071. 字符串的最大公因子
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

示例 1：

输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"
示例 2：

输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"
示例 3：

输入：str1 = "LEET", str2 = "CODE"
输出：""
链接：https://leetcode-cn.com/problems/greatest-common-divisor-of-strings
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length1 = len(str1)
        length2 = len(str2)
        # 找出大小字符串分别赋值
        min_str = str2 if length1 >= length2 else str1
        max_str = str1 if length1 >= length2 else str2
        if min_str not in max_str: return ""
        length3 = len(min_str)
        length4 = len(max_str)
        result = None
        i = 1
        # 开始遍历，找出最长的公因子，赋值给result
        while i <= length3:
            # 如果能够被i整除则往下走
            if length3 % i == 0:
                # 截取字段 倍增 和原字符相等，相等则赋值给result
                if min_str[:i] * (length3 // i) == min_str and min_str[:i] * (length4 // i) == max_str:
                    result = min_str[:i]
            i += 1
        if result:
            return result
        else:
            return ""

#   官方解法：从大往下遍历。可以节约步数
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1), len(str2)), 0, -1):
            if (len(str1) % i) == 0 and (len(str2) % i) == 0:
                if str1[: i] * (len(str1) // i) == str1 and str1[: i] * (len(str2) // i) == str2:
                    return str1[: i]
        return ''



if __name__ == "__main__":
    s = Solution()
    print(s.gcdOfStrings(str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX", str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))