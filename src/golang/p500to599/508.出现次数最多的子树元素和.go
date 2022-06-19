package p500to599

import (
	"math"
)

/*
 * @lc app=leetcode.cn id=508 lang=golang
 *
 * [508] 出现次数最多的子树元素和
 *
 * https://leetcode.cn/problems/most-frequent-subtree-sum/description/
 *
 * algorithms
 * Medium (71.10%)
 * Likes:    158
 * Dislikes: 0
 * Total Accepted:    21.4K
 * Total Submissions: 30.3K
 * Testcase Example:  '[5,2,-3]'
 *
 * 给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。
 *
 * 一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入: root = [5,2,-3]
 * 输出: [2,-3,4]
 *
 *
 * 示例 2：
 *
 *
 *
 *
 * 输入: root = [5,2,-5]
 * 输出: [2]
 *
 *
 *
 *
 * 提示:
 *
 *
 * 节点数在 [1, 10^4] 范围内
 * -10^5 <= Node.val <= 10^5
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
func findFrequentTreeSum(root *TreeNode) []int {
	cnt := map[int]int{}
	maxCnt := math.MinInt32

	var postorder func(*TreeNode) int
	postorder = func(tn *TreeNode) int {
		if tn == nil {
			return 0
		}

		val := tn.Val + postorder(tn.Left) + postorder(tn.Right)
		cnt[val]++
		if cnt[val] > maxCnt {
			maxCnt = cnt[val]
		}
		return val
	}

	postorder(root)

	ans := []int{}
	for k, v := range cnt {
		if v == maxCnt {
			ans = append(ans, k)
		}
	}
	return ans
}

// @lc code=end
