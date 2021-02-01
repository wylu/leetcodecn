/*
 * @lc app=leetcode.cn id=839 lang=cpp
 *
 * [839] 相似字符串组
 *
 * https://leetcode-cn.com/problems/similar-string-groups/description/
 *
 * algorithms
 * Hard (57.19%)
 * Likes:    115
 * Dislikes: 0
 * Total Accepted:    16.3K
 * Total Submissions: 28.4K
 * Testcase Example:  '["tars","rats","arts","star"]'
 *
 * 如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y
 * 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。
 * 
 * 例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与
 * "tars"，"rats"，或 "arts" 相似。
 * 
 * 总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts"
 * 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。
 * 
 * 给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。请问 strs 中有多少个相似字符串组？
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：strs = ["tars","rats","arts","star"]
 * 输出：2
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：strs = ["omv","ovm"]
 * 输出：1
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= strs.length <= 100
 * 1 <= strs[i].length <= 1000
 * sum(strs[i].length) <= 2 * 10^4
 * strs[i] 只包含小写字母。
 * strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。
 * 
 * 
 * 
 * 
 * 备注：
 * 
 * 字母异位词（anagram），一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。
 * 
 */

/**
 * @File    :   839.相似字符串组.cpp
 * @Time    :   2021/02/01 09:57:00
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：并查集
 * 思路及解法
 * 
 * 我们把每一个字符串看作点，字符串之间是否相似看作边，那么可以发现本题
 * 询问的是给定的图中有多少连通分量。于是可以想到使用并查集维护节点间的
 * 连通性。
 * 
 * 我们枚举给定序列中的任意一对字符串，检查其是否具有相似性，如果相似，
 * 那么我们就将这对字符串相连。
 * 
 * 在实际代码中，我们可以首先判断当前这对字符串是否已经连通，如果没有
 * 连通，我们再检查它们是否具有相似性，可以优化一定的时间复杂度的常数。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class UnionFind {
public:
    vector<int> par;
    int cnt;

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
};

class Solution {
public:
    int numSimilarGroups(vector<string>& strs) {
        int n = strs.size();
        UnionFind uf(n);
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n; j++) {
                if (isSimilar(strs[i], strs[j])) uf.unite(i, j);
            }
        }
        return uf.cnt;
    }

    bool isSimilar(string& s1, string& s2) {
        int cnt = 0, n = s1.length();
        for (int i = 0; i < n; i++) {
            if (s1[i] != s2[i]) cnt++;
            if (cnt > 2) return false;
        }
        return true;
    }
};
// @lc code=end
