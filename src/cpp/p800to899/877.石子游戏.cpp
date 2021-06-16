/*
 * @lc app=leetcode.cn id=877 lang=cpp
 *
 * [877] 石子游戏
 *
 * https://leetcode-cn.com/problems/stone-game/description/
 *
 * algorithms
 * Medium (74.04%)
 * Likes:    265
 * Dislikes: 0
 * Total Accepted:    37.3K
 * Total Submissions: 50.3K
 * Testcase Example:  '[5,3,4,5]'
 *
 * 亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。
 * 
 * 游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
 * 
 * 亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。
 * 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
 * 
 * 假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。
 * 
 * 
 * 
 * 示例：
 * 
 * 
 * 输入：[5,3,4,5]
 * 输出：true
 * 解释：
 * 亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
 * 假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
 * 如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
 * 如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
 * 这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 2 <= piles.length <= 500
 * piles.length 是偶数。
 * 1 <= piles[i] <= 500
 * sum(piles) 是奇数。
 * 
 * 
 */

/**
 * @File    :   877.石子游戏.cpp
 * @Time    :   2021/06/16 08:47:24
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：动态规划
 * 
 * dp[i][j]：表示当数组剩下的部分为下标 i 到下标 j 时，当前玩家与另一个玩家的石子数
 *           之差的最大值，注意当前玩家不一定是先手。
 * 
 * 只有当 i <= j 时，数组剩下的部分才有意义，因此当 i > j 时，dp[i][j] = 0。
 * 
 * 当 i = j 时，只剩一个数字，当前玩家只取走这堆石子，因此对于所有
 * 0 <= i < len(piles)，都有 dp[i][i] = piles[i]。
 * 
 * 当 i < j 时，当前玩家可以选择 piles[i] 或 piles[j]，然后轮到另一个玩家在数组
 * 剩下的部分选取数字。在两种方案中，当前玩家会选择最优的方案，使得自己的石子数最大化。
 * 因此可以得到如下状态转移方程：
 * 
 * dp[i][j] = max(piles[i] − dp[i+1][j], piles[j] − dp[i][j−1])
 * 
 * 最后判断 dp[0][len(piles)−1] 的值，如果大于或等于 0，则先手得分大于或等于后手得分，
 * 因此先手成为赢家，否则后手成为赢家。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        int n = piles.size();
        vector<vector<int>> f(n, vector<int>(n));
        for (int i = 0; i < n; i++) f[i][i] = piles[i];

        for (int i = n - 2; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                f[i][j] = max(piles[i] - f[i + 1][j], piles[j] - f[i][j - 1]);
            }
        }
        return f[0][n - 1] > 0;
    }
};
// @lc code=end

// #define PII pair<int, int>

// class Solution {
//     map<PII, int> cache;

// public:
//     bool stoneGame(vector<int>& piles) {
//         return dfs(piles, 0, piles.size() - 1) > 0;
//     }

//     int dfs(vector<int>& piles, int L, int R) {
//         if (L == R) return piles[L];
//         PII key = PII{L, R};
//         if (cache.count(key)) return cache[key];
//         cache[key] = max(piles[L] - dfs(piles, L + 1, R),
//                          piles[R] - dfs(piles, L, R - 1));
//         return cache[key];
//     }
// };

int main(int argc, char const* argv[]) {
    Solution solu;
    vector<int> piles = {5, 3, 4, 5};
    cout << solu.stoneGame(piles) << endl;
    return 0;
}
