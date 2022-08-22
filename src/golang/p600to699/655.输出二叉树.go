package p600to699

import (
	"math"
	"strconv"
)

/*
 * @lc app=leetcode.cn id=655 lang=golang
 *
 * [655] 输出二叉树
 *
 * https://leetcode.cn/problems/print-binary-tree/description/
 *
 * algorithms
 * Medium (67.67%)
 * Likes:    169
 * Dislikes: 0
 * Total Accepted:    22.1K
 * Total Submissions: 32.6K
 * Testcase Example:  '[1,2]'
 *
 * 给你一棵二叉树的根节点 root ，请你构造一个下标从 0 开始、大小为 m x n 的字符串矩阵 res ，用以表示树的 格式化布局
 * 。构造此格式化布局矩阵需要遵循以下规则：
 *
 *
 * 树的 高度 为 height ，矩阵的行数 m 应该等于 height + 1 。
 * 矩阵的列数 n 应该等于 2^height+1 - 1 。
 * 根节点 需要放置在 顶行 的 正中间 ，对应位置为 res[0][(n-1)/2] 。
 * 对于放置在矩阵中的每个节点，设对应位置为 res[r][c] ，将其左子节点放置在 res[r+1][c-2^height-r-1] ，右子节点放置在
 * res[r+1][c+2^height-r-1] 。
 * 继续这一过程，直到树中的所有节点都妥善放置。
 * 任意空单元格都应该包含空字符串 "" 。
 *
 *
 * 返回构造得到的矩阵 res 。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [1,2]
 * 输出：
 * [["","1",""],
 * ["2","",""]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [1,2,3,null,4]
 * 输出：
 * [["","","","1","","",""],
 * ["","2","","","","3",""],
 * ["","","4","","","",""]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点数在范围 [1, 2^10] 内
 * -99 <= Node.val <= 99
 * 树的深度在范围 [1, 10] 内
 *
 *
 */

/**
 * @File    :   655.输出二叉树.go
 * @Time    :   2022/08/22 14:02:23
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
func printTree(root *TreeNode) [][]string {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	var getDepth func(*TreeNode) int
	getDepth = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		return 1 + max(getDepth(root.Left), getDepth(root.Right))
	}

	rows := getDepth(root)
	cols := int(math.Pow(2, float64(rows))) - 1
	ans := make([][]string, rows)
	for i := range ans {
		ans[i] = make([]string, cols)
	}

	var fill func(*TreeNode, int, int, int)
	fill = func(root *TreeNode, depth, left, right int) {
		if root == nil {
			return
		}
		c := left + (right-left)/2
		ans[depth][c] = strconv.Itoa(root.Val)
		fill(root.Left, depth+1, left, c-1)
		fill(root.Right, depth+1, c+1, right)
	}

	fill(root, 0, 0, cols-1)
	return ans
}

// @lc code=end
