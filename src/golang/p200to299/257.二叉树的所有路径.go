package p200to299

import (
	"strconv"
	"strings"
)

/*
 * @lc app=leetcode.cn id=257 lang=golang
 *
 * [257] 二叉树的所有路径
 *
 * https://leetcode-cn.com/problems/binary-tree-paths/description/
 *
 * algorithms
 * Easy (64.95%)
 * Likes:    314
 * Dislikes: 0
 * Total Accepted:    52.7K
 * Total Submissions: 81.1K
 * Testcase Example:  '[1,2,3,null,5]'
 *
 * 给定一个二叉树，返回所有从根节点到叶子节点的路径。
 *
 * 说明: 叶子节点是指没有子节点的节点。
 *
 * 示例:
 *
 * 输入:
 *
 * ⁠  1
 * ⁠/   \
 * 2     3
 * ⁠\
 * ⁠ 5
 *
 * 输出: ["1->2->5", "1->3"]
 *
 * 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
 *
 */

/**
 * @File    :   257.二叉树的所有路径.go
 * @Time    :   2020/09/26 11:28:34
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func binaryTreePaths(root *TreeNode) []string {
	ans := []string{}
	stack := []string{}

	var dfs func(root *TreeNode)
	dfs = func(root *TreeNode) {
		if root == nil {
			return
		}

		stack = append(stack, strconv.Itoa(root.Val))
		if root.Left == nil && root.Right == nil {
			ans = append(ans, strings.Join(stack, "->"))
			stack = stack[:len(stack)-1]
			return
		}

		dfs(root.Left)
		dfs(root.Right)
		stack = stack[:len(stack)-1]
	}

	dfs(root)
	return ans
}

// @lc code=end
