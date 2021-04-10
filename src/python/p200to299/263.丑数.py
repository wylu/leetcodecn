#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#
# https://leetcode-cn.com/problems/ugly-number/description/
#
# algorithms
# Easy (50.44%)
# Likes:    201
# Dislikes: 0
# Total Accepted:    61K
# Total Submissions: 121K
# Testcase Example:  '6'
#
# 给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
#
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。
#
#
#
# 示例 1：
#
#
# 输入：n = 6
# 输出：true
# 解释：6 = 2 × 3
#
# 示例 2：
#
#
# 输入：n = 8
# 输出：true
# 解释：8 = 2 × 2 × 2
#
#
# 示例 3：
#
#
# 输入：n = 14
# 输出：false
# 解释：14 不是丑数，因为它包含了另外一个质因数 7 。
#
#
# 示例 4：
#
#
# 输入：n = 1
# 输出：true
# 解释：1 通常被视为丑数。
#
#
#
#
# 提示：
#
#
# -2^31 <= n <= 2^31 - 1
#
#
#


# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        while n > 0:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                break
        return n == 1


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.isUgly(6))
    print(solu.isUgly(8))
    print(solu.isUgly(14))
    print(solu.isUgly(1))
    print(solu.isUgly(0))
    print(solu.isUgly(2**31 - 1))
    print(solu.isUgly(-6))
    print(solu.isUgly(-8))
    print(solu.isUgly(-14))
    print(solu.isUgly(-2**31))
