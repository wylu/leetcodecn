/*
 * @lc app=leetcode.cn id=1621 lang=cpp
 *
 * [1621] 大小为 K 的不重叠线段的数目
 *
 * https://leetcode-cn.com/problems/number-of-sets-of-k-non-overlapping-line-segments/description/
 *
 * algorithms
 * Medium (42.04%)
 * Likes:    18
 * Dislikes: 0
 * Total Accepted:    906
 * Total Submissions: 2.2K
 * Testcase Example:  '4\n2'
 *
 * 给你一维空间的 n 个点，其中第 i 个点（编号从 0 到 n-1）位于 x = i 处，请你找到 恰好 k 个不重叠
 * 线段且每个线段至少覆盖两个点的方案数。线段的两个端点必须都是 整数坐标 。这 k 个线段不需要全部覆盖全部 n 个点，且它们的端点 可以 重合。
 * 
 * 请你返回 k 个不重叠线段的方案数。由于答案可能很大，请将结果对 10^9 + 7 取余 后返回。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 4, k = 2
 * 输出：5
 * 解释：
 * 如图所示，两个线段分别用红色和蓝色标出。
 * 上图展示了 5 种不同的方案
 * {(0,2),(2,3)}，{(0,1),(1,3)}，{(0,1),(2,3)}，{(1,2),(2,3)}，{(0,1),(1,2)} 。
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 3, k = 1
 * 输出：3
 * 解释：总共有 3 种不同的方案 {(0,1)}, {(0,2)}, {(1,2)} 。
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：n = 30, k = 7
 * 输出：796297179
 * 解释：画 7 条线段的总方案数为 3796297200 种。将这个数对 10^9 + 7 取余得到 796297179 。
 * 
 * 
 * 示例 4：
 * 
 * 
 * 输入：n = 5, k = 3
 * 输出：7
 * 
 * 
 * 示例 5：
 * 
 * 
 * 输入：n = 3, k = 2
 * 输出：1
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 2 
 * 1 
 * 
 * 
 */

/**
 * @File    :   1621.大小为-k-的不重叠线段的数目.cpp
 * @Time    :   2020/10/29 11:34:28
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：动态规划
 * 思路与算法
 * 
 * 记 f[i][j] 表示使用 0 .. i 的点构造了 j 条线段的方案数。我们需要区分
 * 第 j 条线段的右端点是否就是 i，因此可以考虑把 f[i][j] 拆分成两个状态：
 * 
 * f[i][j][0] 表示第 j 条线段的右端点不是 i，也就是说我们没有办法继续
 * 延长第 j 条线段；
 * 
 * f[i][j][1] 表示第 j 条线段的右端点就是 i，也就是说我们可以选择是否
 * 继续延长第 j 条线段。
 * 
 * 如何进行状态转移呢？
 * 
 * 首先考虑 f[i][j][0]，因为第 j 条线段的右端点不是 i，因此第 i 个点
 * 没有用上，那么 0 .. i-1 的点构造了 j 条线段，即
 * 
 *   f[i][j][0] = f[i-1][j][0] + f[i-1][j][1]
 * 
 * 再考虑 f[i][j][1]，因为第 j 条线段的右端点就是 i，因此有两种情况：
 * 
 * 第 j 条线段长度为 1，那么 0 .. i-1 的点构造了 j−1 条线段，即
 * 
 *   f[i][j][1] = f[i-1][j-1][0] + f[i-1][j-1][1]
 * 
 * 第 j 条线段长度大于 1，那么删去第 j 条线段 i-1 .. i 的这一部分，
 * 0 .. i-1 的点仍然构造了 j 条线段，并且点 i−1 是属于第 j 条线段的，即
 * 
 *   f[i][j][1] = f[i-1][j][1]
 * 
 * 加上边界条件 f[0][0][0] = 1，最终答案即为 f[n-1][k][0] + f[n-1][k][1]
 * 
 * 方法二：组合数学
 * https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/discuss/898830/Python-O(N)-Solution-with-Prove
 * 
 * Intuition
 * Case 1: Given n points, take k segments, allowed to share endpoints.
 * Same as:
 * Case 2: Given n + k - 1 points, take k segments, not allowed to
 *         share endpoints.
 * 
 * Prove
 * In case 2, for each solution,
 * remove one point after the segments,
 * then we got one valid solution for case 1.
 * 
 * Reversly also right.
 * 
 * Explanation
 * Easy combination number C(n + k - 1, 2k).
 * 
 * Complexity
 * Time O(NM), Space O(1), Invoving large integer operation.
 * Time O(N), Space O(N) using inverse number.
 * 
 * Example:
 * n = 4, k = 2
 * 
 * ---+---+---+---+---
 *    0   1   2   3
 * 
 * solutions: (01,23), (01,12), (02,23), (01,13), (12,23)
 * 
 * insert a point to separate segments
 * 
 * ---+---+---+---+---+---
 *    0   1   x   2   3
 * 
 * solutions: (1x23),  (0x23),  (0123),  (01x3),  (01x2)
 * mapping:   (12,23), (02,23), (01,23), (01,13), (01,12)
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int numberOfSets(int n, int k) {
        int MOD = 1000000007;
        int f[1001][1001][2] = {0};
        f[0][0][0] = 1;

        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= k; j++) {
                f[i][j][0] = (f[i - 1][j][0] + f[i - 1][j][1]) % MOD;
                f[i][j][1] = f[i - 1][j][1];
                if (j > 0) {
                    f[i][j][1] += f[i - 1][j - 1][0];
                    f[i][j][1] %= MOD;
                    f[i][j][1] += f[i - 1][j - 1][1];
                    f[i][j][1] %= MOD;
                }
            }
        }

        return (f[n - 1][k][0] + f[n - 1][k][1]) % MOD;
    }
};
// @lc code=end

int main(int argc, char const *argv[]) {
    Solution solu;
    cout << solu.numberOfSets(30, 7) << endl;
    return 0;
}
