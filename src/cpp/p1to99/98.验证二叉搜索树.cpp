/*
 * @lc app=leetcode.cn id=98 lang=cpp
 *
 * [98] 验证二叉搜索树
 *
 * https://leetcode-cn.com/problems/validate-binary-search-tree/description/
 *
 * algorithms
 * Medium (32.65%)
 * Likes:    817
 * Dislikes: 0
 * Total Accepted:    184.9K
 * Total Submissions: 566.3K
 * Testcase Example:  '[2,1,3]'
 *
 * 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
 * 
 * 假设一个二叉搜索树具有如下特征：
 * 
 * 
 * 节点的左子树只包含小于当前节点的数。
 * 节点的右子树只包含大于当前节点的数。
 * 所有左子树和右子树自身必须也是二叉搜索树。
 * 
 * 
 * 示例 1:
 * 
 * 输入:
 * ⁠   2
 * ⁠  / \
 * ⁠ 1   3
 * 输出: true
 * 
 * 
 * 示例 2:
 * 
 * 输入:
 * ⁠    5
 * ⁠   / \
 * ⁠  1   4
 *  / \
 * 3   6
 * 输出: false
 * 解释: 输入为: [5,1,4,null,null,3,6]。
 * 根节点的值为 5 ，但是其右子节点值为 4 。
 * 
 * 
 */

/**
 * @File    :   98.验证二叉搜索树.cpp
 * @Time    :   2020/10/29 23:33:53
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
    bool isValidBST(TreeNode *root) {
        long pre = long(INT32_MIN) - 1;
        stack<TreeNode *> st;
        while (root || !st.empty()) {
            while (root) {
                st.emplace(root);
                root = root->left;
            }

            root = st.top();
            st.pop();
            if (root->val <= pre) {
                return false;
            }
            pre = root->val;
            root = root->right;
        }
        return true;
    }
};
// @lc code=end

int main(int argc, char const *argv[]) {
    TreeNode *root = new TreeNode(5);
    root->left = new TreeNode(1);
    root->right = new TreeNode(4);
    root->right->left = new TreeNode(3);
    root->right->right = new TreeNode(6);

    Solution solu;
    cout << solu.isValidBST(root) << endl;
    return 0;
}
