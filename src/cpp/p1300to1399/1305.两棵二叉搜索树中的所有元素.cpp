/*
 * @lc app=leetcode.cn id=1305 lang=cpp
 *
 * [1305] 两棵二叉搜索树中的所有元素
 *
 * https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/description/
 *
 * algorithms
 * Medium (76.12%)
 * Likes:    88
 * Dislikes: 0
 * Total Accepted:    20.4K
 * Total Submissions: 26.8K
 * Testcase Example:  '[2,1,4]\r\n[1,0,3]\r'
 *
 * 给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 
 * 输入：root1 = [2,1,4], root2 = [1,0,3]
 * 输出：[0,1,1,2,3,4]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 
 * 输入：root1 = [1,null,8], root2 = [8,1]
 * 输出：[1,1,8,8]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 每棵树的节点数在 [0, 5000] 范围内
 * -10^5 <= Node.val <= 10^5
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   1305.两棵二叉搜索树中的所有元素.cpp
 * @Time    :   2022/05/01 08:48:28
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

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
    vector<int> getAllElements(TreeNode *root1, TreeNode *root2) {
        vector<int> vals1, vals2;
        dfs(vals1, root1);
        dfs(vals2, root2);

        vector<int> ans;
        int i = 0, j = 0, m = vals1.size(), n = vals2.size();
        while (i < m || j < n) {
            if (i < m && j < n) {
                ans.push_back(vals1[i] <= vals2[j] ? vals1[i++] : vals2[j++]);
            } else if (i < m) {
                ans.push_back(vals1[i++]);
            } else if (j < n) {
                ans.push_back(vals2[j++]);
            }
        }
        return ans;
    }

    void dfs(vector<int> &values, TreeNode *root) {
        if (root == nullptr) return;

        dfs(values, root->left);
        values.push_back(root->val);
        dfs(values, root->right);
    }
};
// @lc code=end
