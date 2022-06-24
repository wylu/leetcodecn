package p500to599

/*
 * @lc app=leetcode.cn id=515 lang=golang
 *
 * [515] 在每个树行中找最大值
 *
 * https://leetcode.cn/problems/find-largest-value-in-each-tree-row/description/
 *
 * algorithms
 * Medium (66.08%)
 * Likes:    245
 * Dislikes: 0
 * Total Accepted:    86.3K
 * Total Submissions: 130.6K
 * Testcase Example:  '[1,3,2,5,3,null,9]'
 *
 * 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。
 *
 *
 *
 * 示例1：
 *
 *
 *
 *
 * 输入: root = [1,3,2,5,3,null,9]
 * 输出: [1,3,9]
 *
 *
 * 示例2：
 *
 *
 * 输入: root = [1,2,3]
 * 输出: [1,3]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 二叉树的节点个数的范围是 [0,10^4]
 * -2^31 <= Node.val <= 2^31 - 1
 *
 *
 *
 *
 */

/**
 * @File    :   515.在每个树行中找最大值.go
 * @Time    :   2022/06/24 21:49:54
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
func largestValues(root *TreeNode) []int {
	ans := []int{}
	if root == nil {
		return ans
	}

	que := []*TreeNode{root}
	for len(que) > 0 {
		size := len(que)
		level := que[0].Val
		for i := 0; i < size; i++ {
			root = que[0]
			que = que[1:]
			if root.Val > level {
				level = root.Val
			}
			if root.Left != nil {
				que = append(que, root.Left)
			}
			if root.Right != nil {
				que = append(que, root.Right)
			}
		}
		ans = append(ans, level)
	}

	return ans
}

// @lc code=end
