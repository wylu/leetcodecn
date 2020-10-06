/*
 * @lc app=leetcode.cn id=834 lang=cpp
 *
 * [834] 树中距离之和
 *
 * https://leetcode-cn.com/problems/sum-of-distances-in-tree/description/
 *
 * algorithms
 * Hard (35.87%)
 * Likes:    132
 * Dislikes: 0
 * Total Accepted:    3.8K
 * Total Submissions: 8.6K
 * Testcase Example:  '6\n[[0,1],[0,2],[2,3],[2,4],[2,5]]'
 *
 * 给定一个无向、连通的树。树中有 N 个标记为 0...N-1 的节点以及 N-1 条边 。
 * 
 * 第 i 条边连接节点 edges[i][0] 和 edges[i][1] 。
 * 
 * 返回一个表示节点 i 与其他所有节点距离之和的列表 ans。
 * 
 * 示例 1:
 * 
 * 
 * 输入: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
 * 输出: [8,12,6,10,10,10]
 * 解释: 
 * 如下为给定的树的示意图：
 * ⁠ 0
 * ⁠/ \
 * 1   2
 * ⁠  /|\
 * ⁠ 3 4 5
 * 
 * 我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5) 
 * 也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。
 * 
 * 
 * 说明: 1 <= N <= 10000
 * 
 */

/**
 * @File    :   834.树中距离之和.cpp
 * @Time    :   2020/10/06 18:14:36
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
    vector<vector<int>> graph;
    int n;

public:
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>> &edges) {
        graph = vector<vector<int>>(n, vector<int>{});
        this->n = n;
        for (auto edge : edges) {
            graph[edge[0]].emplace_back(edge[1]);
            graph[edge[1]].emplace_back(edge[0]);
        }

        vector<int> ans(n, 0), cnt(n, 1);
        dfs(0, -1, ans, cnt);
        dfs2(0, -1, ans, cnt);
        return ans;
    }

    void dfs(int u, int parent, vector<int> &ans, vector<int> &cnt) {
        for (auto v : graph[u]) {
            if (v != parent) {
                dfs(v, u, ans, cnt);
                cnt[u] += cnt[v];
                ans[u] += ans[v] + cnt[v];
            }
        }
    };

    void dfs2(int u, int parent, vector<int> &ans, vector<int> &cnt) {
        for (auto v : graph[u]) {
            if (v != parent) {
                ans[v] = ans[u] + (n - cnt[v]) - cnt[v];
                dfs2(v, u, ans, cnt);
            }
        }
    };
};
// @lc code=end
