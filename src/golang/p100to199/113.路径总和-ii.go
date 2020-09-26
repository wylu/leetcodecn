package p100to199

/*
 * @lc app=leetcode.cn id=113 lang=golang
 *
 * [113] 路径总和 II
 *
 * https://leetcode-cn.com/problems/path-sum-ii/description/
 *
 * algorithms
 * Medium (60.91%)
 * Likes:    306
 * Dislikes: 0
 * Total Accepted:    70.1K
 * Total Submissions: 115K
 * Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
 *
 * 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
 *
 * 说明: 叶子节点是指没有子节点的节点。
 *
 * 示例:
 * 给定如下二叉树，以及目标和 sum = 22，
 *
 * ⁠             5
 * ⁠            / \
 * ⁠           4   8
 * ⁠          /   / \
 * ⁠         11  13  4
 * ⁠        /  \    / \
 * ⁠       7    2  5   1
 *
 *
 * 返回:
 *
 * [
 * ⁠  [5,4,11,2],
 * ⁠  [5,8,4,5]
 * ]
 *
 *
 */

/**
 * @File    :   113.路径总和-ii.go
 * @Time    :   2020/09/26 10:22:51
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func pathSum(root *TreeNode, sum int) [][]int {
	ans := [][]int{}
	stack := []int{}

	var dfs func(root *TreeNode, target int)
	dfs = func(root *TreeNode, target int) {
		if root == nil {
			return
		}
		if root.Left == nil && root.Right == nil {
			if root.Val == target {
				path := make([]int, len(stack))
				copy(path, stack)
				path = append(path, root.Val)
				ans = append(ans, path)
			}
			return
		}
		stack = append(stack, root.Val)
		dfs(root.Left, target-root.Val)
		dfs(root.Right, target-root.Val)
		stack = stack[:len(stack)-1]
	}

	dfs(root, sum)
	return ans
}

// @lc code=end
