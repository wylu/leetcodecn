/*
 * @lc app=leetcode.cn id=106 lang=cpp
 *
 * [106] 从中序与后序遍历序列构造二叉树
 *
 * https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
 *
 * algorithms
 * Medium (69.74%)
 * Likes:    317
 * Dislikes: 0
 * Total Accepted:    56.5K
 * Total Submissions: 80.2K
 * Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
 *
 * 根据一棵树的中序遍历与后序遍历构造二叉树。
 * 
 * 注意:
 * 你可以假设树中没有重复的元素。
 * 
 * 例如，给出
 * 
 * 中序遍历 inorder = [9,3,15,20,7]
 * 后序遍历 postorder = [9,15,7,20,3]
 * 
 * 返回如下的二叉树：
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * 
 */

/**
 * @File    :   106.从中序与后序遍历序列构造二叉树.cpp
 * @Time    :   2020/09/25 10:07:25
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
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// @lc code=start
class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (inorder.size() == 0 || inorder.size() != postorder.size()) {
            return nullptr;
        }

        unordered_map<int, int> indices;
        for (int i = 0; i < inorder.size(); i++) {
            indices.insert({inorder[i], i});
        }

        return build(inorder, 0, postorder, 0, postorder.size() - 1, indices);
    }

    TreeNode* build(vector<int>& inorder, int si, vector<int>& postorder,
                    int sp, int ep, unordered_map<int, int>& indices) {
        if (sp > ep) {
            return nullptr;
        }

        TreeNode* root = new TreeNode(postorder[ep]);
        int idx = indices.find(root->val)->second;
        int llen = idx - si;

        root->left = build(inorder, si, postorder, sp, sp + llen - 1, indices);
        root->right =
            build(inorder, idx + 1, postorder, sp + llen, ep - 1, indices);

        return root;
    }
};
// @lc code=end
