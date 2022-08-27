package p600to699

/*
 * @lc app=leetcode.cn id=662 lang=golang
 *
 * [662] 二叉树最大宽度
 *
 * https://leetcode.cn/problems/maximum-width-of-binary-tree/description/
 *
 * algorithms
 * Medium (42.17%)
 * Likes:    450
 * Dislikes: 0
 * Total Accepted:    60.6K
 * Total Submissions: 143.8K
 * Testcase Example:  '[1,3,2,5,3,null,9]'
 *
 * 给你一棵二叉树的根节点 root ，返回树的 最大宽度 。
 *
 * 树的 最大宽度 是所有层中最大的 宽度 。
 *
 *
 *
 * 每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的
 * null 节点，这些 null 节点也计入长度。
 *
 * 题目数据保证答案将会在  32 位 带符号整数范围内。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [1,3,2,5,3,null,9]
 * 输出：4
 * 解释：最大宽度出现在树的第 3 层，宽度为 4 (5,3,null,9) 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [1,3,2,5,null,null,9,6,null,7]
 * 输出：7
 * 解释：最大宽度出现在树的第 4 层，宽度为 7 (6,null,null,null,null,null,7) 。
 *
 *
 * 示例 3：
 *
 *
 * 输入：root = [1,3,2,5]
 * 输出：2
 * 解释：最大宽度出现在树的第 2 层，宽度为 2 (3,2) 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点的数目范围是 [1, 3000]
 * -100 <= Node.val <= 100
 *
 *
 *
 *
 */

/**
 * @File    :   662.二叉树最大宽度.go
 * @Time    :   2022/08/27 11:44:19
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
func widthOfBinaryTree(root *TreeNode) int {
	type pair struct {
		node  *TreeNode
		index int
	}

	ans := 0
	que := []*pair{{root, 0}}

	for len(que) > 0 {
		n := len(que)
		width := que[n-1].index - que[0].index + 1
		if width > ans {
			ans = width
		}

		for i := 0; i < n; i++ {
			p := que[0]
			que = que[1:]

			if p.node.Left != nil {
				que = append(que, &pair{p.node.Left, p.index << 1})
			}
			if p.node.Right != nil {
				que = append(que, &pair{p.node.Right, (p.index << 1) + 1})
			}
		}
	}

	return ans
}

// @lc code=end
