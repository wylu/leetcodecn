package p700to799

/*
 * @lc app=leetcode.cn id=700 lang=golang
 *
 * [700] 二叉搜索树中的搜索
 *
 * https://leetcode-cn.com/problems/search-in-a-binary-search-tree/description/
 *
 * algorithms
 * Easy (77.24%)
 * Likes:    213
 * Dislikes: 0
 * Total Accepted:    113.2K
 * Total Submissions: 146.5K
 * Testcase Example:  '[4,2,7,1,3]\n2'
 *
 * 给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
 *
 * 例如，
 *
 *
 * 给定二叉搜索树:
 *
 * ⁠       4
 * ⁠      / \
 * ⁠     2   7
 * ⁠    / \
 * ⁠   1   3
 *
 * 和值: 2
 *
 *
 * 你应该返回如下子树:
 *
 *
 * ⁠     2
 * ⁠    / \
 * ⁠   1   3
 *
 *
 * 在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。
 *
 */

/**
 * @File    :   700.二叉搜索树中的搜索.go
 * @Time    :   2021/11/26 19:38:57
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func searchBST(root *TreeNode, val int) *TreeNode {
	for root != nil {
		if val == root.Val {
			return root
		}
		if val < root.Val {
			root = root.Left
		} else {
			root = root.Right
		}
	}
	return nil
}

// @lc code=end

// func searchBST(root *TreeNode, val int) *TreeNode {
// 	var inOrder func(*TreeNode) *TreeNode
// 	inOrder = func(root *TreeNode) *TreeNode {
// 		if root == nil || root.Val == val {
// 			return root
// 		}
// 		if val < root.Val {
// 			return inOrder(root.Left)
// 		}
// 		return inOrder(root.Right)
// 	}
// 	return inOrder(root)
// }
