package p100to199

import "math"

/*
 * @lc app=leetcode.cn id=124 lang=golang
 *
 * [124] 二叉树中的最大路径和
 *
 * https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
 *
 * algorithms
 * Hard (43.16%)
 * Likes:    720
 * Dislikes: 0
 * Total Accepted:    77.1K
 * Total Submissions: 178.5K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个非空二叉树，返回其最大路径和。
 *
 * 本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
 *
 *
 *
 * 示例 1：
 *
 * 输入：[1,2,3]
 *
 * ⁠      1
 * ⁠     / \
 * ⁠    2   3
 *
 * 输出：6
 *
 *
 * 示例 2：
 *
 * 输入：[-10,9,20,null,null,15,7]
 *
 * -10
 * / \
 * 9  20
 * /  \
 * 15   7
 *
 * 输出：42
 *
 */

/**
 * @File    :   124.二叉树中的最大路径和.go
 * @Time    :   2020/09/26 18:56:35
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func maxPathSum(root *TreeNode) int {
	ans := math.MinInt32
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	var dfs func(root *TreeNode) int
	dfs = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		left := max(dfs(root.Left), 0)
		right := max(dfs(root.Right), 0)
		ans = max(ans, root.Val+left+right)
		return root.Val + max(left, right)
	}

	dfs(root)
	return ans
}

// @lc code=end
