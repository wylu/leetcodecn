/*
 * @lc app=leetcode.cn id=1617 lang=cpp
 *
 * [1617] 统计子树中城市之间最大距离
 *
 * https://leetcode-cn.com/problems/count-subtrees-with-max-distance-between-cities/description/
 *
 * algorithms
 * Hard (63.00%)
 * Likes:    40
 * Dislikes: 0
 * Total Accepted:    2K
 * Total Submissions: 3.1K
 * Testcase Example:  '4\n[[1,2],[2,3],[2,4]]'
 *
 * 给你 n 个城市，编号为从 1 到 n 。同时给你一个大小为 n-1 的数组 edges ，其中 edges[i] = [ui, vi] 表示城市 ui
 * 和 vi 之间有一条双向边。题目保证任意城市之间只有唯一的一条路径。换句话说，所有城市形成了一棵 树 。
 * 
 * 一棵 子树
 * 是城市的一个子集，且子集中任意城市之间可以通过子集中的其他城市和边到达。两个子树被认为不一样的条件是至少有一个城市在其中一棵子树中存在，但在另一棵子树中不存在。
 * 
 * 对于 d 从 1 到 n-1 ，请你找到城市间 最大距离 恰好为 d 的所有子树数目。
 * 
 * 请你返回一个大小为 n-1 的数组，其中第 d 个元素（下标从 1 开始）是城市间 最大距离 恰好等于 d 的子树数目。
 * 
 * 请注意，两个城市间距离定义为它们之间需要经过的边的数目。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 
 * 输入：n = 4, edges = [[1,2],[2,3],[2,4]]
 * 输出：[3,4,0]
 * 解释：
 * 子树 {1,2}, {2,3} 和 {2,4} 最大距离都是 1 。
 * 子树 {1,2,3}, {1,2,4}, {2,3,4} 和 {1,2,3,4} 最大距离都为 2 。
 * 不存在城市间最大距离为 3 的子树。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 2, edges = [[1,2]]
 * 输出：[1]
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：n = 3, edges = [[1,2],[2,3]]
 * 输出：[2,1]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 2 <= n <= 15
 * edges.length == n-1
 * edges[i].length == 2
 * 1 <= ui, vi <= n
 * 题目保证 (ui, vi) 所表示的边互不相同。
 * 
 * 
 */

/**
 * @File    :   1617.统计子树中城市之间最大距离.cpp
 * @Time    :   2022/03/26 18:08:28
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 注意到数据范围 N <= 15，我们可以枚举子集的构成方式。（这里吐槽一下题目的命名，
 * 用“子树”这个叫法，很容易让人误解，因此我们下面统一称为“子集”。）
 * 
 * 对于每一种子集，我们可以用树形动态规划进行求解。对于每一个节点，我们要求出以其
 * 为根节点的子树中的最大距离和最大深度。最大深度很容易求得，最大距离则需要分几种
 * 情况进行讨论：
 * 
 * 1.从该节点到该字数中深度最大的节点
 * 2.从以该节点的一个孩子节点为根节点的子树中深度最大的节点，到以该节点的另一个
 *   孩子节点为根节点的子树中深度最大的节点
 * 3.从以该节点的一个孩子节点为根节点的子树中的一个节点，到同一子树中的另一节点
 * 
 * 容易看出，第一种和第三种情况比较容易解决，我们只要利用对孩子节点进行递归得到的
 * 结果即可计算出来。对于第二种情况，我们则需要记录所有孩子节点的最大深度中最大的
 * 两个值。
 * 
 * 需要注意的是，我们在 DFS 过程中还需要记录访问过的城市数量，最后与子集中的城市
 * 数量进行比较，如果二者不相等，则说明该子集不连通，是一个非法的子集，应当予以排除。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
#define PII pair<int, int>

class Solution {
    vector<vector<int>> adj;
    int cities = 0;
    bitset<16> bs;

    PII dfs(int u, int d, int p) {
        int max_dist = 0, max_depth = d;
        cities++;
        int m1 = -1, m2 = -1;
        for (int v : adj[u]) {
            if (bs[v] && v != p) {
                auto [dis, dep] = dfs(v, d + 1, u);
                max_depth = max(max_depth, dep);
                max_dist = max(max_dist, dis);
                if (m1 < dep) {
                    m2 = m1;
                    m1 = dep;
                } else if (m2 < dep) {
                    m2 = dep;
                }
            }
        }

        max_dist = max(max_dist, max_depth - d);
        if (m2 > 0) {
            max_dist = max(max_dist, m1 + m2 - d * 2);
        }
        return {max_dist, max_depth};
    }

public:
    vector<int> countSubgraphsForEachDiameter(int n,
                                              vector<vector<int>>& edges) {
        vector<int> ans(n - 1);
        adj = vector<vector<int>>(n);
        for (auto e : edges) {
            int u = e[0] - 1, v = e[1] - 1;
            adj[u].emplace_back(v);
            adj[v].emplace_back(u);
        }

        for (int i = 1; i < (1 << n); i++) {
            bs = bitset<16>(i);
            cities = 0;
            auto [max_dist, max_depth] = dfs(__builtin_ctz(i), 0, -1);
            if (cities == bs.count() && max_dist > 0) ans[max_dist - 1]++;
        }

        return ans;
    }
};
// @lc code=end
