/*
 * @lc app=leetcode.cn id=99 lang=cpp
 *
 * [99] 恢复二叉搜索树
 *
 * https://leetcode-cn.com/problems/recover-binary-search-tree/description/
 *
 * algorithms
 * Hard (62.12%)
 * Likes:    323
 * Dislikes: 0
 * Total Accepted:    36.9K
 * Total Submissions: 59.4K
 * Testcase Example:  '[1,3,null,null,2]'
 *
 * 二叉搜索树中的两个节点被错误地交换。
 * 
 * 请在不改变其结构的情况下，恢复这棵树。
 * 
 * 示例 1:
 * 
 * 输入: [1,3,null,null,2]
 * 
 *   1
 *  /
 * 3
 *  \
 *   2
 * 
 * 输出: [3,1,null,null,2]
 * 
 *   3
 *  /
 * 1
 *  \
 *   2
 * 
 * 
 * 示例 2:
 * 
 * 输入: [3,1,4,null,null,2]
 * 
 * ⁠  3
 *  ⁠/ \
 * 1   4
 *    /
 *   2
 * 
 * 输出: [2,1,4,null,null,3]
 * 
 *  ⁠ 2
 * ⁠ / \
 * 1   4
 *    /
 * ⁠  3
 * 
 * 进阶:
 * 
 * 
 * 使用 O(n) 空间复杂度的解法很容易实现。
 * 你能想出一个只使用常数空间的解决方案吗？
 * 
 * 
 */

/**
 * @File    :   99.恢复二叉搜索树.cpp
 * @Time    :   2020/08/15 23:16:10
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
    void recoverTree(TreeNode *root) {
        if (root == nullptr) {
            return;
        }

        TreeNode *first = nullptr, *second = nullptr, *pre = nullptr;

        while (root != nullptr) {
            if (root->left == nullptr) {
                if (pre != nullptr && root->val < pre->val) {
                    second = root;
                    if (first == nullptr) {
                        first = pre;
                    }
                }
                pre = root;
                root = root->right;
                continue;
            }

            TreeNode *precursor = root->left;
            while (precursor->right != nullptr && precursor->right != root) {
                precursor = precursor->right;
            }

            if (precursor->right == nullptr) {
                precursor->right = root;
                root = root->left;
            } else {
                if (pre != nullptr && root->val < pre->val) {
                    second = root;
                    if (first == nullptr) {
                        first = pre;
                    }
                }
                precursor->right = nullptr;
                pre = root;
                root = root->right;
            }
        }

        swap(first->val, second->val);
    }
};
// @lc code=end

int main(int argc, char const *argv[]) {
    Solution solu;

    TreeNode *root = new TreeNode(1);
    root->left = new TreeNode(3);
    root->left->right = new TreeNode(2);

    solu.recoverTree(root);
    return 0;
}
