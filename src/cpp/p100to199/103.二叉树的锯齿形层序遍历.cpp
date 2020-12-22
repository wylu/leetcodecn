/*
 * @lc app=leetcode.cn id=103 lang=cpp
 *
 * [103] 二叉树的锯齿形层序遍历
 *
 * https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
 *
 * algorithms
 * Medium (55.46%)
 * Likes:    341
 * Dislikes: 0
 * Total Accepted:    97.5K
 * Total Submissions: 172.6K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
 * 
 * 例如：
 * 给定二叉树 [3,9,20,null,null,15,7],
 * 
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * 
 * 返回锯齿形层序遍历如下：
 * 
 * 
 * [
 * ⁠ [3],
 * ⁠ [20,9],
 * ⁠ [15,7]
 * ]
 * 
 * 
 */

/**
 * @File    :   103.二叉树的锯齿形层序遍历.cpp
 * @Time    :   2020/12/22 17:11:20
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
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// @lc code=start
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode *root) {
        if (!root) return {};

        vector<vector<int>> ans;
        vector<int> level;
        bool flag = true;
        queue<TreeNode *> q;
        q.emplace(root);

        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode *root = q.front();
                q.pop();
                level.push_back(root->val);

                if (root->left) q.emplace(root->left);
                if (root->right) q.emplace(root->right);
            }

            if (!flag) reverse(level.begin(), level.end());
            ans.emplace_back(level);
            level = vector<int>();
            flag = !flag;
        }

        return ans;
    }
};
// @lc code=end
