/*
 * @lc app=leetcode.cn id=687 lang=cpp
 *
 * [687] 最长同值路径
 *
 * https://leetcode.cn/problems/longest-univalue-path/description/
 *
 * algorithms
 * Medium (46.65%)
 * Likes:    695
 * Dislikes: 0
 * Total Accepted:    67.1K
 * Total Submissions: 143.9K
 * Testcase Example:  '[5,4,5,1,1,null,5]'
 *
 * 给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。
 * 
 * 两个节点之间的路径长度 由它们之间的边数表示。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 
 * 
 * 
 * 输入：root = [5,4,5,1,1,5]
 * 输出：2
 * 
 * 
 * 示例 2:
 * 
 * 
 * 
 * 
 * 输入：root = [1,4,5,4,4,5]
 * 输出：2
 * 
 * 
 * 
 * 
 * 提示:
 * 
 * 
 * 树的节点数的范围是 [0, 10^4] 
 * -1000 <= Node.val <= 1000
 * 树的深度将不超过 1000 
 * 
 * 
 */

/**
 * @File    :   687.最长同值路径.cpp
 * @Time    :   2022/09/02 19:39:49
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
    int ans = 0;

public:
    int longestUnivaluePath(TreeNode *root) {
        dfs(root);
        return ans;
    }

    int dfs(TreeNode *root) {
        if (root == nullptr) return 0;

        int lc = dfs(root->left);
        int rc = dfs(root->right);

        int left = 0, right = 0;
        if (root->left && root->val == root->left->val) left = lc + 1;
        if (root->right && root->val == root->right->val) right = rc + 1;
        ans = max(ans, left + right);

        return max(left, right);
    }
};
// @lc code=end
