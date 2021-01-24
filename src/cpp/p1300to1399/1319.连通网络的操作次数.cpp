/*
 * @lc app=leetcode.cn id=1319 lang=cpp
 *
 * [1319] 连通网络的操作次数
 *
 * https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected/description/
 *
 * algorithms
 * Medium (56.27%)
 * Likes:    70
 * Dislikes: 0
 * Total Accepted:    11.8K
 * Total Submissions: 20.9K
 * Testcase Example:  '4\n[[0,1],[0,2],[1,2]]'
 *
 * 用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] =
 * [a, b] 连接了计算机 a 和 b。
 * 
 * 网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。
 * 
 * 给你这个计算机网络的初始布线
 * connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回
 * -1 。 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 输入：n = 4, connections = [[0,1],[0,2],[1,2]]
 * 输出：1
 * 解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
 * 输出：2
 * 
 * 
 * 示例 3：
 * 
 * 输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
 * 输出：-1
 * 解释：线缆数量不足。
 * 
 * 
 * 示例 4：
 * 
 * 输入：n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
 * 输出：0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 10^5
 * 1 <= connections.length <= min(n*(n-1)/2, 10^5)
 * connections[i].length == 2
 * 0 <= connections[i][0], connections[i][1] < n
 * connections[i][0] != connections[i][1]
 * 没有重复的连接。
 * 两台计算机不会通过多条线缆连接。
 * 
 * 
 */

/**
 * @File    :   1319.连通网络的操作次数.cpp
 * @Time    :   2021/01/24 22:55:11
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class UnionFind {
    vector<int> par;
    int cnt;

public:
    UnionFind(int n) : par(n), cnt(n) { iota(par.begin(), par.end(), 0); }

    int find(int x) {
        if (par[x] != x) par[x] = find(par[x]);
        return par[x];
    }

    void unite(int x, int y) {
        int fx = find(x), fy = find(y);
        if (fx == fy) return;
        par[fx] = fy;
        cnt--;
    }

    int getCnt() { return cnt; }
};

class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        if (connections.size() < n - 1) return -1;
        UnionFind uf(n);
        for (auto& conn : connections) uf.unite(conn[0], conn[1]);
        return uf.getCnt() - 1;
    }
};
// @lc code=end
