package p500to599

/*
 * @lc app=leetcode.cn id=513 lang=golang
 *
 * [513] 找树左下角的值
 *
 * https://leetcode.cn/problems/find-bottom-left-tree-value/description/
 *
 * algorithms
 * Medium (74.06%)
 * Likes:    318
 * Dislikes: 0
 * Total Accepted:    110.6K
 * Total Submissions: 149.3K
 * Testcase Example:  '[2,1,3]'
 *
 * 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
 *
 * 假设二叉树中至少有一个节点。
 *
 *
 *
 * 示例 1:
 *
 *
 *
 *
 * 输入: root = [2,1,3]
 * 输出: 1
 *
 *
 * 示例 2:
 *
 * ⁠
 *
 *
 * 输入: [1,2,3,4,null,5,6,null,null,7]
 * 输出: 7
 *
 *
 *
 *
 * 提示:
 *
 *
 * 二叉树的节点个数的范围是 [1,10^4]
 * -2^31
 *
 *
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
func findBottomLeftValue(root *TreeNode) int {
	ans, depth := root.Val, 0

	var dfs func(*TreeNode, int)
	dfs = func(root *TreeNode, d int) {
		if root == nil {
			return
		}

		dfs(root.Left, d+1)
		if d > depth {
			ans, depth = root.Val, d
		}
		dfs(root.Right, d+1)
	}

	dfs(root, 0)
	return ans
}

// @lc code=end
