/*
 * @lc app=leetcode.cn id=675 lang=cpp
 *
 * [675] 为高尔夫比赛砍树
 *
 * https://leetcode.cn/problems/cut-off-trees-for-golf-event/description/
 *
 * algorithms
 * Hard (53.22%)
 * Likes:    175
 * Dislikes: 0
 * Total Accepted:    15.6K
 * Total Submissions: 29.3K
 * Testcase Example:  '[[1,2,3],[0,0,4],[7,6,5]]'
 *
 * 你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个 m x n 的矩阵表示， 在这个矩阵中：
 * 
 * 
 * 0 表示障碍，无法触碰
 * 1 表示地面，可以行走
 * 比 1 大的数 表示有树的单元格，可以行走，数值表示树的高度
 * 
 * 
 * 每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。
 * 
 * 你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 1（即变为地面）。
 * 
 * 你将从 (0, 0) 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。
 * 
 * 可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：forest = [[1,2,3],[0,0,4],[7,6,5]]
 * 输出：6
 * 解释：沿着上面的路径，你可以用 6 步，按从最矮到最高的顺序砍掉这些树。
 * 
 * 示例 2：
 * 
 * 
 * 输入：forest = [[1,2,3],[0,0,0],[7,6,5]]
 * 输出：-1
 * 解释：由于中间一行被障碍阻塞，无法访问最下面一行中的树。
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：forest = [[2,3,4],[0,0,5],[8,7,6]]
 * 输出：6
 * 解释：可以按与示例 1 相同的路径来砍掉所有的树。
 * (0,0) 位置的树，可以直接砍去，不用算步数。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * m == forest.length
 * n == forest[i].length
 * 1 <= m, n <= 50
 * 0 <= forest[i][j] <= 10^9
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   675.为高尔夫比赛砍树.cpp
 * @Time    :   2022/05/23 22:08:58
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
#define PII pair<int, int>

class Solution {
    int d[5] = {0, 1, 0, -1, 0};

public:
    int cutOffTree(vector<vector<int>> &forest) {
        vector<PII> trees;
        int row = forest.size(), col = forest[0].size();
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (forest[i][j] > 1) trees.emplace_back(i, j);
            }
        }
        sort(trees.begin(), trees.end(),
             [&](const PII &a, const PII &b) -> bool {
                 return forest[a.first][a.second] < forest[b.first][b.second];
             });

        int ans = 0, cx = 0, cy = 0;
        for (int i = 0; i < trees.size(); i++) {
            int step = bfs(forest, cx, cy, trees[i].first, trees[i].second);
            if (step == -1) return -1;
            ans += step;
            cx = trees[i].first, cy = trees[i].second;
        }

        return ans;
    }

    int bfs(vector<vector<int>> &forest, int sx, int sy, int tx, int ty) {
        if (sx == tx && sy == ty) return 0;

        int row = forest.size(), col = forest[0].size(), step = 0;
        queue<PII> que;
        vector<vector<bool>> seen(row, vector<bool>(col, false));
        que.emplace(sx, sy);
        seen[sx][sy] = true;

        while (!que.empty()) {
            step++;
            int sz = que.size();
            for (int i = 0; i < sz; i++) {
                auto [cx, cy] = que.front();
                que.pop();
                for (int j = 0; j < 4; j++) {
                    int nx = cx + d[j];
                    int ny = cy + d[j + 1];
                    if (nx >= 0 && nx < row && ny >= 0 && ny < col &&
                        !seen[nx][ny] && forest[nx][ny]) {
                        if (nx == tx && ny == ty) return step;
                        que.emplace(nx, ny);
                        seen[nx][ny] = true;
                    }
                }
            }
        }

        return -1;
    }
};
// @lc code=end
