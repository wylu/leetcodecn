package p700to799

/*
 * @lc app=leetcode.cn id=701 lang=golang
 *
 * [701] 二叉搜索树中的插入操作
 *
 * https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/description/
 *
 * algorithms
 * Medium (72.25%)
 * Likes:    111
 * Dislikes: 0
 * Total Accepted:    32K
 * Total Submissions: 44.3K
 * Testcase Example:  '[4,2,7,1,3]\n5'
 *
 * 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。
 * 输入数据保证，新值和原始二叉搜索树中的任意节点值都不同。
 *
 * 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。
 *
 *
 *
 * 例如,
 *
 * 给定二叉搜索树:
 *
 * ⁠       4
 * ⁠      / \
 * ⁠     2   7
 * ⁠    / \
 * ⁠   1   3
 *
 * 和 插入的值: 5
 *
 *
 * 你可以返回这个二叉搜索树:
 *
 * ⁠        4
 * ⁠      /   \
 * ⁠     2     7
 * ⁠    / \   /
 * ⁠   1   3 5
 *
 *
 * 或者这个树也是有效的:
 *
 * ⁠        5
 * ⁠      /   \
 * ⁠     2     7
 * ⁠    / \
 * ⁠   1   3
 * ⁠        \
 * ⁠         4
 *
 *
 *
 *
 * 提示：
 *
 *
 * 给定的树上的节点数介于 0 和 10^4 之间
 * 每个节点都有一个唯一整数值，取值范围从 0 到 10^8
 * -10^8 <= val <= 10^8
 * 新值和原始二叉搜索树中的任意节点值都不同
 *
 *
 */

/**
 * @File    :   701.二叉搜索树中的插入操作.go
 * @Time    :   2020/09/30 13:06:11
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func insertIntoBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return &TreeNode{Val: val}
	}

	var dfs func(root *TreeNode)
	dfs = func(root *TreeNode) {
		if val < root.Val {
			if root.Left != nil {
				dfs(root.Left)
			} else {
				root.Left = &TreeNode{Val: val}
			}
		} else {
			if root.Right != nil {
				dfs(root.Right)
			} else {
				root.Right = &TreeNode{Val: val}
			}
		}
	}

	dfs(root)
	return root
}

// @lc code=end
