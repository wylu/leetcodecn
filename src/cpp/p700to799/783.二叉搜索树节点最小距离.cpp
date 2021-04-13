/*
 * @lc app=leetcode.cn id=783 lang=cpp
 *
 * [783] 二叉搜索树节点最小距离
 *
 * https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/description/
 *
 * algorithms
 * Easy (58.95%)
 * Likes:    172
 * Dislikes: 0
 * Total Accepted:    56.6K
 * Total Submissions: 96.1K
 * Testcase Example:  '[4,2,6,1,3]'
 *
 * 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
 * 
 * 注意：本题与
 * 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
 * 相同
 * 
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：root = [4,2,6,1,3]
 * 输出：1
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：root = [1,0,48,null,null,12,49]
 * 输出：1
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 树中节点数目在范围 [2, 100] 内
 * 0 <= Node.val <= 10^5
 * 
 * 
 * 
 * 
 */

/**
 * @File    :   783.二叉搜索树节点最小距离.cpp
 * @Time    :   2021/04/13 21:51:10
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
    TreeNode *pre = nullptr;
    int ans = INT32_MAX;

public:
    int minDiffInBST(TreeNode *root) {
        dfs(root);
        return ans;
    }

    void dfs(TreeNode *root) {
        if (root->left) dfs(root->left);
        if (pre) ans = min(ans, root->val - pre->val);
        pre = root;
        if (root->right) dfs(root->right);
    }
};
// @lc code=end
