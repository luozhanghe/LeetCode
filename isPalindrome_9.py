"""
9. 回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 判断输入的是否少于0，少于0，直接返回False
        if x < 0:
            return False
        str_tmp = ""
        # 把整形转为字符串型，然后从后面往前遍历，然后重新拼成一个字符串
        for i in range(len(str(x))-1, -1, -1):
            str_tmp += str(x)[i]
        if x == int(str_tmp):
            return True
        else:
            return False

if __name__ =="__main__":
    s = Solution()
    print(s.isPalindrome(12321))