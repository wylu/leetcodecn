package p600to699

import (
	"strconv"
	"strings"
)

/*
 * @lc app=leetcode.cn id=606 lang=golang
 *
 * [606] 根据二叉树创建字符串
 *
 * https://leetcode-cn.com/problems/construct-string-from-binary-tree/description/
 *
 * algorithms
 * Easy (61.94%)
 * Likes:    293
 * Dislikes: 0
 * Total Accepted:    51.2K
 * Total Submissions: 82.7K
 * Testcase Example:  '[1,2,3,4]'
 *
 * 你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
 *
 * 空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。
 *
 * 示例 1:
 *
 *
 * 输入: 二叉树: [1,2,3,4]
 * ⁠      1
 * ⁠    /   \
 * ⁠   2     3
 * ⁠  /
 * ⁠ 4
 *
 * 输出: "1(2(4))(3)"
 *
 * 解释: 原本将是“1(2(4)())(3())”，
 * 在你省略所有不必要的空括号对之后，
 * 它将是“1(2(4))(3)”。
 *
 *
 * 示例 2:
 *
 *
 * 输入: 二叉树: [1,2,3,null,4]
 * ⁠      1
 * ⁠    /   \
 * ⁠   2     3
 * ⁠    \
 * ⁠     4
 *
 * 输出: "1(2()(4))(3)"
 *
 * 解释: 和第一个示例相似，
 * 除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。
 *
 *
 */

/**
 * @File    :   606.根据二叉树创建字符串.go
 * @Time    :   2022/03/19 19:22:47
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
func tree2str(root *TreeNode) string {
	ans := &strings.Builder{}
	stk := []*TreeNode{root}
	seen := map[*TreeNode]bool{}
	for len(stk) > 0 {
		node := stk[len(stk)-1]
		if seen[node] {
			if node != root {
				ans.WriteByte(')')
			}
			stk = stk[:len(stk)-1]
		} else {
			seen[node] = true
			if node != root {
				ans.WriteByte('(')
			}
			ans.WriteString(strconv.Itoa(node.Val))
			if node.Left == nil && node.Right != nil {
				ans.WriteString("()")
			}
			if node.Right != nil {
				stk = append(stk, node.Right)
			}
			if node.Left != nil {
				stk = append(stk, node.Left)
			}
		}
	}
	return ans.String()
}

// @lc code=end

// func tree2str(root *TreeNode) string {
// 	if root == nil {
// 		return ""
// 	}

// 	cur := strconv.Itoa(root.Val)
// 	left := tree2str(root.Left)
// 	right := tree2str(root.Right)
// 	switch {
// 	case left == "" && right == "":
// 		return cur
// 	case left == "" && right != "":
// 		return cur + "()(" + right + ")"
// 	case left != "" && right == "":
// 		return cur + "(" + left + ")"
// 	default:
// 		return cur + "(" + left + ")(" + right + ")"
// 	}
// }
