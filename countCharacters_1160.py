"""
1160. 拼写单词
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。

假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。

注意：每次拼写时，chars 中的每个字母都只能用一次。

返回词汇表 words 中你掌握的所有单词的 长度之和。

示例 1：

输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释：
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
class Solution:
    def countCharacters(self, words: list, chars: str) -> int:
        # list_tmp = []
        result = 0
        for i in range(len(words)):
            # 暴力解法：轮询每个单词，看每个单词的字母是否在chars都能找到字母
            list_str = list(words[i])
            tmp_list = list(chars)
            list_length, tmp = len(list_str), len(list_str)
            for j in range(list_length):
                if list_str[j] in tmp_list:
                    # 能够找到，则单词长度减一，然后删除一个字母，满足题目每个字母只能用一次
                    list_length -= 1
                    tmp_list.remove(list_str[j])
            # 最后判断单子是否等于0,且单chars长度大于等于0，既满足条件
            if list_length == 0 and len(tmp_list) >= 0:
                result += tmp
        return result
if __name__ == "__main__":
    s = Solution()
    print(s.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))