package p700to799

import "math"

/*
 * @lc app=leetcode.cn id=783 lang=golang
 *
 * [783] 二叉搜索树节点最小距离
 *
 * https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/description/
 *
 * algorithms
 * Easy (58.95%)
 * Likes:    172
 * Dislikes: 0
 * Total Accepted:    56.6K
 * Total Submissions: 96.1K
 * Testcase Example:  '[4,2,6,1,3]'
 *
 * 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
 *
 * 注意：本题与
 * 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
 * 相同
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [4,2,6,1,3]
 * 输出：1
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [1,0,48,null,null,12,49]
 * 输出：1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点数目在范围 [2, 100] 内
 * 0 <= Node.val <= 10^5
 *
 *
 *
 *
 */

/**
 * @File    :   783.二叉搜索树节点最小距离.go
 * @Time    :   2021/04/13 22:41:14
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
func minDiffInBST(root *TreeNode) int {
	ans := math.MaxInt32
	var pre *TreeNode

	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	var dfs func(root *TreeNode)
	dfs = func(root *TreeNode) {
		if root.Left != nil {
			dfs(root.Left)
		}
		if pre != nil {
			ans = min(ans, root.Val-pre.Val)
		}
		pre = root
		if root.Right != nil {
			dfs(root.Right)
		}
	}

	dfs(root)
	return ans
}

// @lc code=end
