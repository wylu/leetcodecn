/*
 * @lc app=leetcode.cn id=1707 lang=cpp
 *
 * [1707] 与数组中元素的最大异或值
 *
 * https://leetcode-cn.com/problems/maximum-xor-with-an-element-from-array/description/
 *
 * algorithms
 * Hard (47.02%)
 * Likes:    78
 * Dislikes: 0
 * Total Accepted:    8.1K
 * Total Submissions: 17.2K
 * Testcase Example:  '[0,1,2,3,4]\n[[3,1],[1,3],[5,6]]'
 *
 * 给你一个由非负整数组成的数组 nums 。另有一个查询数组 queries ，其中 queries[i] = [xi, mi] 。
 * 
 * 第 i 个查询的答案是 xi 和任何 nums 数组中不超过 mi 的元素按位异或（XOR）得到的最大值。换句话说，答案是 max(nums[j]
 * XOR xi) ，其中所有 j 均满足 nums[j] <= mi 。如果 nums 中的所有元素都大于 mi，最终答案就是 -1 。
 * 
 * 返回一个整数数组 answer 作为查询的答案，其中 answer.length == queries.length 且 answer[i] 是第 i
 * 个查询的答案。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
 * 输出：[3,3,7]
 * 解释：
 * 1) 0 和 1 是仅有的两个不超过 1 的整数。0 XOR 3 = 3 而 1 XOR 3 = 2 。二者中的更大值是 3 。
 * 2) 1 XOR 2 = 3.
 * 3) 5 XOR 2 = 7.
 * 
 * 
 * 示例 2：
 * 
 * 输入：nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
 * 输出：[15,-1,5]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length, queries.length <= 10^5
 * queries[i].length == 2
 * 0 <= nums[j], xi, mi <= 10^9
 * 
 * 
 */

/**
 * @File    :   1707.与数组中元素的最大异或值.cpp
 * @Time    :   2021/05/23 17:45:06
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 前言
 * 本文需要读者了解字典树的相关知识，建议读者尝试解决「208. 实现 Trie (前缀树)」，
 * 在充分理解该题做法后继续阅读。
 * 
 * 方法一：离线询问 + 字典树
 * 思路
 * 
 * 我们先来解决一个弱化版的问题：去掉询问中 mi 的限制，如何求 xi 与 nums 数组任意
 * 元素的异或最大值？
 * 
 * 我们可以将 nums 中的每个元素看作一个长为 L 的二进制串，将其插入字典树中。
 * 
 * 例如 nums = [3,10,5,25,2]，取 L=5，对应的二进制串为 [00011,01010,00101,11001,00010]，
 * 将其插入字典树后得到的结果如下图。
 * 
 * https://assets.leetcode-cn.com/solution-static/1707/1.png
 * 
 * 为了最大化异或值，我们可以在字典树中进行一次与检索字符串类似的过程，从根节点出发，
 * 由于异或运算具有「相同得 0，不同得 1」的性质，为了尽可能多地取到 1，我们需要在
 * 每一步寻找与当前位相反的子节点，若该节点存在则将指针移动到该节点，否则只能移动到
 * 与当前位相同的子节点。（注意由于插入和查询的二进制串长度均为 L，非叶节点的两个
 * 子节点中，至少有一个是非空节点）
 * 
 * 以 xi = 25 = 11001 为例，下图展示了求取最大异或值的过程。
 * 
 * https://assets.leetcode-cn.com/solution-static/1707/2.png
 * 
 * 回到原问题，由于全部询问已经给出，我们不一定要按顺序回答询问，而是按照 mi 从小
 * 到大的顺序回答。
 * 
 * 首先将数组 nums 从小到大排序，将询问按照 mi 的大小从小到大排序。
 * 
 * 在回答每个询问前，将所有不超过 mi 的 nums 元素插入字典序中，由于 nums 已经排
 * 好序，我们可以维护一个指向 nums 数组元素的下标 idx，初始值为 0，每插入一个元素
 * 就将 idx 加一。对于每个询问，我们可以不断插入满足 nums[idx] <= mi 的元素，直至
 * 不满足该条件或 idx 指向了数组末尾。
 * 
 * 此时字典树中的元素就是 nums 中所有不超过 mi 的元素，这样就转换成了弱化版的问题。
 * 
 * 代码实现时，由于 nums 元素不超过 10^9，为简单起见，可取 L=30，即 10^9 的二进制
 * 串的长度。此外，由于对询问排序会打乱原询问的顺序，而我们需要按照原询问的顺序返回
 * 答案，因此可以在排序前，对每个询问附加一个其在 queries 中的下标。
 * 
 * 方法二：在线询问 + 字典树
 * 思路
 * 
 * 我们可以给字典树上的每个节点添加一个值 min，表示以该节点为根的子树所记录的元素
 * 的最小值。特别地，根节点的 min 表示字典树上记录的所有元素的最小值。
 * 
 * 首先将所有元素插入字典树，插入时更新字典树对应节点的 min 值。
 * 
 * 然后依次回答每个询问：若 mi 小于根节点的 min 值，说明 nums 中的所有元素都大于
 * mi，返回 -1；否则，做法类似方法一，只需要在循环内额外判断与当前位相反的子节点的
 * min 是否不超过 mi，若不超过则可以转移至该节点。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Trie {
public:
    const int L = 30;
    Trie* children[2] = {};
    int minimum = INT32_MAX;

    void insert(int val) {
        Trie* node = this;
        node->minimum = min(node->minimum, val);
        for (int i = L - 1; i >= 0; i--) {
            int bit = (val >> i) & 1;
            if (node->children[bit] == nullptr) {
                node->children[bit] = new Trie();
            }
            node = node->children[bit];
            node->minimum = min(node->minimum, val);
        }
    }

    int getMaxXor(int val, int limit) {
        Trie* node = this;
        if (node->minimum > limit) return -1;

        int ans = 0;
        for (int i = L - 1; i >= 0; i--) {
            int bit = (val >> i) & 1;
            if (node->children[bit ^ 1] != nullptr &&
                node->children[bit ^ 1]->minimum <= limit) {
                ans |= 1 << i;
                bit ^= 1;
            }
            node = node->children[bit];
        }
        return ans;
    }
};

class Solution {
public:
    vector<int> maximizeXor(vector<int>& nums, vector<vector<int>>& queries) {
        Trie* ti = new Trie();
        for (auto num : nums) ti->insert(num);

        int size = queries.size();
        vector<int> ans(size);
        for (int i = 0; i < size; i++) {
            ans[i] = ti->getMaxXor(queries[i][0], queries[i][1]);
        }

        return ans;
    }
};
// @lc code=end

// class Trie {
// public:
//     const int L = 30;
//     Trie* children[2] = {};

//     void insert(int val) {
//         Trie* node = this;
//         for (int i = L - 1; i >= 0; i--) {
//             int bit = (val >> i) & 1;
//             if (node->children[bit] == nullptr) {
//                 node->children[bit] = new Trie();
//             }
//             node = node->children[bit];
//         }
//     }

//     int getMaxXor(int val) {
//         int ans = 0;
//         Trie* node = this;
//         for (int i = L - 1; i >= 0; i--) {
//             int bit = (val >> i) & 1;
//             if (node->children[bit ^ 1] != nullptr) {
//                 ans |= 1 << i;
//                 bit ^= 1;
//             }
//             node = node->children[bit];
//         }
//         return ans;
//     }
// };

// class Solution {
// public:
//     vector<int> maximizeXor(vector<int>& nums, vector<vector<int>>& queries) {
//         sort(nums.begin(), nums.end());
//         int n = queries.size();
//         for (int i = 0; i < n; i++) {
//             queries[i].push_back(i);
//         }
//         sort(queries.begin(), queries.end(),
//              [](auto& x, auto& y) -> bool { return x[1] < y[1]; });

//         vector<int> ans(n);
//         Trie* ti = new Trie();
//         int idx = 0, size = nums.size();
//         for (auto& q : queries) {
//             int x = q[0], m = q[1], qid = q[2];
//             while (idx < size && nums[idx] <= m) ti->insert(nums[idx++]);

//             if (idx == 0) {
//                 ans[qid] = -1;  // 字典树为空
//             } else {
//                 ans[qid] = ti->getMaxXor(x);
//             }
//         }

//         return ans;
//     }
// };
