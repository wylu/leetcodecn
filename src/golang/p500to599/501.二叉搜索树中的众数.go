package p500to599

/*
 * @lc app=leetcode.cn id=501 lang=golang
 *
 * [501] 二叉搜索树中的众数
 *
 * https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/description/
 *
 * algorithms
 * Easy (47.04%)
 * Likes:    163
 * Dislikes: 0
 * Total Accepted:    21.2K
 * Total Submissions: 45.1K
 * Testcase Example:  '[1,null,2,2]'
 *
 * 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
 *
 * 假定 BST 有如下定义：
 *
 *
 * 结点左子树中所含结点的值小于等于当前结点的值
 * 结点右子树中所含结点的值大于等于当前结点的值
 * 左子树和右子树都是二叉搜索树
 *
 *
 * 例如：
 * 给定 BST [1,null,2,2],
 *
 * ⁠  1
 * ⁠   \
 * ⁠    2
 * ⁠   /
 * ⁠  2
 *
 *
 * 返回[2].
 *
 * 提示：如果众数超过1个，不需考虑输出顺序
 *
 * 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
 *
 */

// @lc code=start
func findMode(root *TreeNode) []int {
	cnts, maxCnt := map[int]int{}, 0

	max := func(x, y int) int {
		if x > y {
			return x

		}
		return y
	}

	var dfs func(root *TreeNode)
	dfs = func(root *TreeNode) {
		if root == nil {
			return
		}
		cnts[root.Val]++
		maxCnt = max(maxCnt, cnts[root.Val])
		dfs(root.Left)
		dfs(root.Right)
	}

	dfs(root)
	ans := []int{}
	for k, v := range cnts {
		if v == maxCnt {
			ans = append(ans, k)
		}
	}
	return ans
}

// @lc code=end
