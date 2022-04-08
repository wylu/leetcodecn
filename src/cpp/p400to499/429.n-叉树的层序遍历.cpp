/*
 * @lc app=leetcode.cn id=429 lang=cpp
 *
 * [429] N 叉树的层序遍历
 *
 * https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/description/
 *
 * algorithms
 * Medium (71.66%)
 * Likes:    258
 * Dislikes: 0
 * Total Accepted:    100.8K
 * Total Submissions: 140.7K
 * Testcase Example:  '[1,null,3,2,4,null,5,6]'
 *
 * 给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
 * 
 * 树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 
 * 输入：root = [1,null,3,2,4,null,5,6]
 * 输出：[[1],[3,2,4],[5,6]]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 
 * 输入：root =
 * [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
 * 输出：[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 树的高度不会超过 1000
 * 树的节点总数在 [0, 10^4] 之间
 * 
 * 
 */

/**
 * @File    :   429.n-叉树的层序遍历.cpp
 * @Time    :   2022/04/08 19:40:13
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

#include <bits/stdc++.h>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) { val = _val; }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};

// @lc code=start
class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> ans;
        if (root == nullptr) return ans;

        queue<Node*> que;
        que.emplace(root);

        vector<int> cur;
        while (!que.empty()) {
            int size = que.size();
            for (int i = 0; i < size; i++) {
                Node* node = que.front();
                que.pop();
                cur.push_back(node->val);
                for (auto& child : node->children) {
                    que.emplace(child);
                }
            }
            ans.emplace_back(cur);
            cur = {};
        }

        return ans;
    }
};
// @lc code=end
