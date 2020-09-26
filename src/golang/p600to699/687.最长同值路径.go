package p600to699

/*
 * @lc app=leetcode.cn id=687 lang=golang
 *
 * [687] 最长同值路径
 *
 * https://leetcode-cn.com/problems/longest-univalue-path/description/
 *
 * algorithms
 * Easy (41.81%)
 * Likes:    358
 * Dislikes: 0
 * Total Accepted:    23.9K
 * Total Submissions: 57.2K
 * Testcase Example:  '[5,4,5,1,1,5]'
 *
 * 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
 *
 * 注意：两个节点之间的路径长度由它们之间的边数表示。
 *
 * 示例 1:
 *
 * 输入:
 *
 *
 * ⁠             5
 * ⁠            / \
 * ⁠           4   5
 * ⁠          / \   \
 * ⁠         1   1   5
 *
 *
 * 输出:
 *
 *
 * 2
 *
 *
 * 示例 2:
 *
 * 输入:
 *
 *
 * ⁠             1
 * ⁠            / \
 * ⁠           4   5
 * ⁠          / \   \
 * ⁠         4   4   5
 *
 *
 * 输出:
 *
 *
 * 2
 *
 *
 * 注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
 *
 */

/**
 * @File    :   687.最长同值路径.go
 * @Time    :   2020/09/26 13:59:06
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func longestUnivaluePath(root *TreeNode) int {
	ans := 0
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

		left := dfs(root.Left)
		right := dfs(root.Right)

		leftPath, rightPath := 0, 0
		if root.Left != nil && root.Left.Val == root.Val {
			leftPath = left + 1
		}
		if root.Right != nil && root.Right.Val == root.Val {
			rightPath = right + 1
		}

		ans = max(ans, leftPath+rightPath)
		return max(leftPath, rightPath)
	}

	dfs(root)
	return ans
}

// @lc code=end
