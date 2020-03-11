class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        if sum(A) % 3 != 0:
            return False
        m, i, j, k, tmp2, tmp3 = len(A), 0, 0, 0, 0, 0
        tmp = sum(A) / 3
        for i in range(m):
            tmp2 = tmp2 + A[i]
            if tmp2 == tmp:
                i += 1
                break
        for j in range(i, m):
            tmp3 = tmp3 + A[j]
            if tmp3 == tmp:
                j += 1
                break
        if j < m and sum(A[j:]) == tmp:
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    n = s.canThreePartsEqualSum([1,-1,1,-1])
    print(n)