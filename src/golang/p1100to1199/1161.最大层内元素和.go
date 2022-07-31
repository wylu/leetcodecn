package p1100to1199

import (
	"math"
)

/*
 * @lc app=leetcode.cn id=1161 lang=golang
 *
 * [1161] 最大层内元素和
 *
 * https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree/description/
 *
 * algorithms
 * Medium (65.11%)
 * Likes:    74
 * Dislikes: 0
 * Total Accepted:    17.5K
 * Total Submissions: 27K
 * Testcase Example:  '[1,7,0,7,-8,null,null]'
 *
 * 给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。
 *
 * 请返回层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：root = [1,7,0,7,-8,null,null]
 * 输出：2
 * 解释：
 * 第 1 层各元素之和为 1，
 * 第 2 层各元素之和为 7 + 0 = 7，
 * 第 3 层各元素之和为 7 + -8 = -1，
 * 所以我们返回第 2 层的层号，它的层内元素之和最大。
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [989,null,10250,98693,-89388,null,null,null,-32127]
 * 输出：2
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中的节点数在 [1, 10^4]范围内
 * -10^5 <= Node.val <= 10^5
 *
 *
 */

/**
 * @File    :   1161.最大层内元素和.go
 * @Time    :   2022/07/31 10:07:58
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
func maxLevelSum(root *TreeNode) int {
	ans, total := 0, math.MinInt32
	que := []*TreeNode{root}
	for level := 1; len(que) > 0; level++ {
		cur, size := 0, len(que)
		for i := 0; i < size; i++ {
			root = que[0]
			que = que[1:]
			cur += root.Val
			if root.Left != nil {
				que = append(que, root.Left)
			}
			if root.Right != nil {
				que = append(que, root.Right)
			}
		}

		if cur > total {
			ans, total = level, cur
		}
	}

	return ans
}

// @lc code=end
