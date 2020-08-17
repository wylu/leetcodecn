package p100to199

/*
 * @lc app=leetcode.cn id=145 lang=golang
 *
 * [145] 二叉树的后序遍历
 *
 * https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
 *
 * algorithms
 * Hard (72.17%)
 * Likes:    375
 * Dislikes: 0
 * Total Accepted:    108.5K
 * Total Submissions: 150.3K
 * Testcase Example:  '[1,null,2,3]'
 *
 * 给定一个二叉树，返回它的 后序 遍历。
 *
 * 示例:
 *
 * 输入: [1,null,2,3]
 * ⁠  1
 * ⁠   \
 * ⁠    2
 * ⁠   /
 * ⁠  3
 *
 * 输出: [3,2,1]
 *
 * 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
 *
 */

/**
 * @File    :   145.二叉树的后序遍历.go
 * @Time    :   2020/08/17 21:53:29
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// @lc code=start
func postorderTraversal(root *TreeNode) []int {
	ans := []int{}
	if root == nil {
		return ans
	}

	stack := []*TreeNode{root}
	for len(stack) != 0 {
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		ans = append(ans, root.Val)

		if root.Left != nil {
			stack = append(stack, root.Left)
		}
		if root.Right != nil {
			stack = append(stack, root.Right)
		}
	}

	reverse145(&ans)
	return ans
}

func reverse145(ans *[]int) {
	for i, j := 0, len(*ans)-1; i < j; i, j = i+1, j-1 {
		(*ans)[i], (*ans)[j] = (*ans)[j], (*ans)[i]
	}
}

// @lc code=end
