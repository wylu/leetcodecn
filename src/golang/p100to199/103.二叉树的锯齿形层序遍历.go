package p100to199

/*
 * @lc app=leetcode.cn id=103 lang=golang
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
 * @File    :   103.二叉树的锯齿形层序遍历.go
 * @Time    :   2020/12/23 19:24:19
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
func zigzagLevelOrder(root *TreeNode) [][]int {
	ans := [][]int{}
	q := []*TreeNode{root}
	flag, level := true, []int{}

	if root == nil {
		return ans
	}

	reverse := func(s *[]int) {
		for i, j := 0, len(*s)-1; i < j; i, j = i+1, j-1 {
			(*s)[i], (*s)[j] = (*s)[j], (*s)[i]
		}
	}

	for len(q) > 0 {
		for i, size := 0, len(q); i < size; i++ {
			root = q[0]
			q = q[1:]
			level = append(level, root.Val)

			if root.Left != nil {
				q = append(q, root.Left)
			}
			if root.Right != nil {
				q = append(q, root.Right)
			}
		}

		if !flag {
			reverse(&level)
		}
		ans = append(ans, level)
		level, flag = []int{}, !flag
	}

	return ans
}

// @lc code=end
