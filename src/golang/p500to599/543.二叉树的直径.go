package p500to599

/*
 * @lc app=leetcode.cn id=543 lang=golang
 *
 * [543] 二叉树的直径
 *
 * https://leetcode-cn.com/problems/diameter-of-binary-tree/description/
 *
 * algorithms
 * Easy (51.64%)
 * Likes:    489
 * Dislikes: 0
 * Total Accepted:    72.7K
 * Total Submissions: 140.8K
 * Testcase Example:  '[1,2,3,4,5]'
 *
 * 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
 *
 *
 *
 * 示例 :
 * 给定二叉树
 *
 * ⁠         1
 * ⁠        / \
 * ⁠       2   3
 * ⁠      / \
 * ⁠     4   5
 *
 *
 * 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
 *
 *
 *
 * 注意：两结点之间的路径长度是以它们之间边的数目表示。
 *
 */

// @lc code=start
func diameterOfBinaryTree(root *TreeNode) int {
	if root == nil {
		return 0
	}
	ans := 0
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	var dfs func(root *TreeNode) int
	dfs = func(root *TreeNode) int {
		left, right := 0, 0
		if root.Left != nil {
			left = 1 + dfs(root.Left)
		}
		if root.Right != nil {
			right = 1 + dfs(root.Right)
		}
		ans = max(ans, left+right)
		return max(left, right)
	}

	dfs(root)
	return ans
}

// @lc code=end
