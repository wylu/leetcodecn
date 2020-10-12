/*
 * @lc app=leetcode.cn id=530 lang=cpp
 *
 * [530] 二叉搜索树的最小绝对差
 *
 * https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/description/
 *
 * algorithms
 * Easy (60.02%)
 * Likes:    162
 * Dislikes: 0
 * Total Accepted:    31.6K
 * Total Submissions: 52.7K
 * Testcase Example:  '[1,null,3,2]'
 *
 * 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
 * 
 * 
 * 
 * 示例：
 * 
 * 输入：
 * 
 * ⁠  1
 * ⁠   \
 * ⁠    3
 * ⁠   /
 * ⁠  2
 * 
 * 输出：
 * 1
 * 
 * 解释：
 * 最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 树中至少有 2 个节点。
 * 本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/
 * 相同
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x) {}
};

// @lc code=start
class Solution {
public:
    int getMinimumDifference(TreeNode *root) {
        int ans = INT32_MAX;
        stack<TreeNode *> st;
        TreeNode *pre = nullptr;
        while (root || !st.empty()) {
            while (root) {
                st.emplace(root);
                root = root->left;
            }
            root = st.top();
            st.pop();
            if (pre) {
                ans = min(ans, root->val - pre->val);
            }
            pre = root;
            root = root->right;
        }
        return ans;
    }
};
// @lc code=end
