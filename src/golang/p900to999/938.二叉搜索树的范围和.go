package p900to999

/*
 * @lc app=leetcode.cn id=938 lang=golang
 *
 * [938] 二叉搜索树的范围和
 *
 * https://leetcode-cn.com/problems/range-sum-of-bst/description/
 *
 * algorithms
 * Easy (81.78%)
 * Likes:    221
 * Dislikes: 0
 * Total Accepted:    87.5K
 * Total Submissions: 107K
 * Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'
 *
 * 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
 * 输出：32
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
 * 输出：23
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点数目在范围 [1, 2 * 10^4] 内
 * 1 <= Node.val <= 105
 * 1 <= low <= high <= 105
 * 所有 Node.val 互不相同
 *
 *
 */

/**
 * @File    :   938.二叉搜索树的范围和.go
 * @Time    :   2021/04/28 22:59:12
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
func rangeSumBST(root *TreeNode, low int, high int) int {
	ans := 0

	var dfs func(root *TreeNode)
	dfs = func(root *TreeNode) {
		if root == nil {
			return
		}

		dfs(root.Left)
		if root.Val >= low && root.Val <= high {
			ans += root.Val
		}
		dfs(root.Right)
	}

	dfs(root)
	return ans
}

// @lc code=end
