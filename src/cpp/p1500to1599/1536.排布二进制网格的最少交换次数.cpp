/*
 * @lc app=leetcode.cn id=1536 lang=cpp
 *
 * [1536] 排布二进制网格的最少交换次数
 *
 * https://leetcode-cn.com/problems/minimum-swaps-to-arrange-a-binary-grid/description/
 *
 * algorithms
 * Medium (38.94%)
 * Likes:    14
 * Dislikes: 0
 * Total Accepted:    2.6K
 * Total Submissions: 6.6K
 * Testcase Example:  '[[0,0,1],[1,1,0],[1,0,0]]'
 *
 * 给你一个 n x n 的二进制网格 grid，每一次操作中，你可以选择网格的 相邻两行 进行交换。
 * 
 * 一个符合要求的网格需要满足主对角线以上的格子全部都是 0 。
 * 
 * 请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 -1 。
 * 
 * 主对角线指的是从 (1, 1) 到 (n, n) 的这些格子。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 输入：grid = [[0,0,1],[1,1,0],[1,0,0]]
 * 输出：3
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 输入：grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
 * 输出：-1
 * 解释：所有行都是一样的，交换相邻行无法使网格符合要求。
 * 
 * 
 * 示例 3：
 * 
 * 
 * 
 * 输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
 * 输出：0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * n == grid.length
 * n == grid[i].length
 * 1 <= n <= 200
 * grid[i][j] 要么是 0 要么是 1 。
 * 
 * 
 */

/**
 * @File    :   1536.排布二进制网格的最少交换次数.cpp
 * @Time    :   2020/08/05 21:24:40
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int minSwaps(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            for (int j = n - 1; j > 0; j--) {
                if (grid[i][j]) {
                    a[i] = j;
                    break;
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            int j = i;
            while (j < n) {
                if (a[j] <= i) {
                    break;
                }
                j++;
            }

            if (j == n) {
                return -1;
            }

            while (j > i) {
                swap(a[j], a[j - 1]);
                j--;
                ans++;
            }
        }

        return ans;
    }
};
// @lc code=end
