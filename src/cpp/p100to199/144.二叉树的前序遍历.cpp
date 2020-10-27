/*
 * @lc app=leetcode.cn id=144 lang=cpp
 *
 * [144] 二叉树的前序遍历
 *
 * https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
 *
 * algorithms
 * Medium (67.64%)
 * Likes:    413
 * Dislikes: 0
 * Total Accepted:    200.2K
 * Total Submissions: 295K
 * Testcase Example:  '[1,null,2,3]'
 *
 * 给定一个二叉树，返回它的 前序 遍历。
 * 
 * 示例:
 * 
 * 输入: [1,null,2,3]  
 * ⁠  1
 * ⁠   \
 * ⁠    2
 * ⁠   /
 * ⁠  3 
 * 
 * 输出: [1,2,3]
 * 
 * 
 * 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
 * 
 */

/**
 * @File    :   144.二叉树的前序遍历.cpp
 * @Time    :   2020/10/27 11:41:02
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right)
        : val(x), left(left), right(right) {}
};

// @lc code=start
class Solution {
public:
    vector<int> preorderTraversal(TreeNode *root) {
        if (!root) return {};

        stack<TreeNode *> st;
        st.emplace(root);

        vector<int> ans;
        while (!st.empty()) {
            root = st.top();
            st.pop();
            ans.emplace_back(root->val);
            if (root->right) st.emplace(root->right);
            if (root->left) st.emplace(root->left);
        }

        return ans;
    }
};
// @lc code=end
