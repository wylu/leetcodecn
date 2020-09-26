package p400to499

/*
 * @lc app=leetcode.cn id=437 lang=golang
 *
 * [437] 路径总和 III
 *
 * https://leetcode-cn.com/problems/path-sum-iii/description/
 *
 * algorithms
 * Medium (55.97%)
 * Likes:    584
 * Dislikes: 0
 * Total Accepted:    53K
 * Total Submissions: 94.6K
 * Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
 *
 * 给定一个二叉树，它的每个结点都存放着一个整数值。
 *
 * 找出路径和等于给定数值的路径总数。
 *
 * 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
 *
 * 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
 *
 * 示例：
 *
 * root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
 *
 * ⁠     10
 * ⁠    /  \
 * ⁠   5   -3
 * ⁠  / \    \
 * ⁠ 3   2   11
 * ⁠/ \   \
 * 3  -2   1
 *
 * 返回 3。和等于 8 的路径有:
 *
 * 1.  5 -> 3
 * 2.  5 -> 2 -> 1
 * 3.  -3 -> 11
 *
 *
 */

// @lc code=start
func pathSum(root *TreeNode, target int) int {
	ans, ps := 0, map[int]int{}
	ps[0] = 1

	var dfs func(root *TreeNode, tot int)
	dfs = func(root *TreeNode, tot int) {
		if root == nil {
			return
		}

		tot += root.Val
		ans += ps[tot-target]

		ps[tot]++
		dfs(root.Left, tot)
		dfs(root.Right, tot)
		ps[tot]--
	}

	dfs(root, 0)
	return ans
}

// @lc code=end
