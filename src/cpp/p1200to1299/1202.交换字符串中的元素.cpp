/*
 * @lc app=leetcode.cn id=1202 lang=cpp
 *
 * [1202] 交换字符串中的元素
 *
 * https://leetcode-cn.com/problems/smallest-string-with-swaps/description/
 *
 * algorithms
 * Medium (49.49%)
 * Likes:    202
 * Dislikes: 0
 * Total Accepted:    21.9K
 * Total Submissions: 44.2K
 * Testcase Example:  '"dcab"\n[[0,3],[1,2]]'
 *
 * 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0
 * 开始）。
 * 
 * 你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
 * 
 * 返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 输入：s = "dcab", pairs = [[0,3],[1,2]]
 * 输出："bacd"
 * 解释： 
 * 交换 s[0] 和 s[3], s = "bcad"
 * 交换 s[1] 和 s[2], s = "bacd"
 * 
 * 
 * 示例 2：
 * 
 * 输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
 * 输出："abcd"
 * 解释：
 * 交换 s[0] 和 s[3], s = "bcad"
 * 交换 s[0] 和 s[2], s = "acbd"
 * 交换 s[1] 和 s[2], s = "abcd"
 * 
 * 示例 3：
 * 
 * 输入：s = "cba", pairs = [[0,1],[1,2]]
 * 输出："abc"
 * 解释：
 * 交换 s[0] 和 s[1], s = "bca"
 * 交换 s[1] 和 s[2], s = "bac"
 * 交换 s[0] 和 s[1], s = "abc"
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 10^5
 * 0 <= pairs.length <= 10^5
 * 0 <= pairs[i][0], pairs[i][1] < s.length
 * s 中只含有小写英文字母
 * 
 * 
 */

/**
 * @File    :   1202.交换字符串中的元素.cpp
 * @Time    :   2021/01/13 09:00:46
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：并查集
 * 思路及解法
 * 
 * 既然可以任意地交换通过「索引对」直接相连的字符，那么我们也任意地交换
 * 通过「索引对」间接相连的字符。我们利用这个性质将该字符串抽象：将每
 * 一个字符抽象为「点」，那么这些「索引对」即为「边」，我们只需要维护这个
 * 「图」的连通性即可。对于同属一个连通块（极大连通子图）内的字符，我们
 * 可以任意地交换它们。
 * 
 * 这样我们的思路就很清晰了：利用并查集维护任意两点的连通性，将同属一个
 * 连通块内的点提取出来，直接排序后放置回其在字符串中的原位置即可。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class UnionFind {
    vector<int> par;

public:
    UnionFind(int n) : par(vector<int>(n)) { iota(par.begin(), par.end(), 0); }

    void unite(int x, int y) { par[find(x)] = par[find(y)]; }

    int find(int x) {
        if (par[x] != x) par[x] = find(par[x]);
        return par[x];
    }
};

class Solution {
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        int n = s.length();
        UnionFind uf(n);

        for (auto& item : pairs) uf.unite(item[0], item[1]);

        unordered_map<int, vector<char>> blocks;
        for (int i = 0; i < n; i++) blocks[uf.find(i)].push_back(s[i]);

        for (auto& it : blocks) sort(it.second.rbegin(), it.second.rend());

        string ans = "";
        for (int i = 0; i < n; i++) {
            int bid = uf.find(i);
            ans += blocks[bid].back();
            blocks[bid].pop_back();
        }

        return ans;
    }
};
// @lc code=end
