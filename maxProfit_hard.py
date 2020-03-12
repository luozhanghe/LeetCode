#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 9:34 上午
# @Author  : 罗樟河
# @File    : maxProfit_hard.py
# @Software: PyCharm


class Solution:
    def maxProfit(self, prices) -> int:
        tmp_list = []
        tmp_profit = 0
        if not prices:
            return 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                tmp_profit += prices[i] - prices[i - 1]
            else:
                if tmp_profit > 0:
                    tmp_list.append(tmp_profit)
                tmp_profit = 0
        tmp_list.append(tmp_profit)
        profit_list = sorted(tmp_list)
        if len(profit_list) > 1:
            profit = profit_list[-1] + profit_list[-2]
        else:
            profit = profit_list[0]
        return profit


if __name__ == "__main__":
    s = Solution()
    count = s.maxProfit([1,2,4,2,5,7,2,4,9,0])
    print(count)
