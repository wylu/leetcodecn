package p500to599

/*
 * @lc app=leetcode.cn id=589 lang=golang
 *
 * [589] N 叉树的前序遍历
 *
 * https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/
 *
 * algorithms
 * Easy (75.55%)
 * Likes:    243
 * Dislikes: 0
 * Total Accepted:    119.8K
 * Total Submissions: 158.6K
 * Testcase Example:  '[1,null,3,2,4,null,5,6]'
 *
 * 给定一个 n 叉树的根节点  root ，返回 其节点值的 前序遍历 。
 *
 * n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：root = [1,null,3,2,4,null,5,6]
 * 输出：[1,3,5,6,2,4]
 *
 *
 * 示例 2：
 *
 *
 *
 *
 * 输入：root =
 * [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
 * 输出：[1,2,3,6,7,11,14,4,8,12,5,9,13,10]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 节点总数在范围 [0, 10^4]内
 * 0 <= Node.val <= 10^4
 * n 叉树的高度小于或等于 1000
 *
 *
 *
 *
 * 进阶：递归法很简单，你可以使用迭代法完成此题吗?
 *
 */

/**
 * @File    :   589.n-叉树的前序遍历.go
 * @Time    :   2022/03/10 14:04:14
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func preorder(root *Node) []int {
	ans := []int{}
	stk := []*Node{}
	if root != nil {
		stk = append(stk, root)
	}

	for len(stk) > 0 {
		root = stk[len(stk)-1]
		stk = stk[:len(stk)-1]
		ans = append(ans, root.Val)
		for i := len(root.Children) - 1; i >= 0; i-- {
			stk = append(stk, root.Children[i])
		}
	}

	return ans
}

// @lc code=end

// func preorder(root *Node) []int {
// 	ans := []int{}

// 	var dfs func(*Node)
// 	dfs = func(root *Node) {
// 		if root == nil {
// 			return
// 		}

// 		ans = append(ans, root.Val)
// 		for _, ch := range root.Children {
// 			dfs(ch)
// 		}
// 	}

// 	dfs(root)
// 	return ans
// }
