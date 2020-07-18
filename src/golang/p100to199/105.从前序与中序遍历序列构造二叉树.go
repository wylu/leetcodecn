package p100to199

/*
 * @lc app=leetcode.cn id=105 lang=golang
 *
 * [105] 从前序与中序遍历序列构造二叉树
 *
 * https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
 *
 * algorithms
 * Medium (67.34%)
 * Likes:    575
 * Dislikes: 0
 * Total Accepted:    95.4K
 * Total Submissions: 141.4K
 * Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
 *
 * 根据一棵树的前序遍历与中序遍历构造二叉树。
 *
 * 注意:
 * 你可以假设树中没有重复的元素。
 *
 * 例如，给出
 *
 * 前序遍历 preorder = [3,9,20,15,7]
 * 中序遍历 inorder = [9,3,15,20,7]
 *
 * 返回如下的二叉树：
 *
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 *
 */

/**
 * @File    :   105.从前序与中序遍历序列构造二叉树.go
 * @Time    :   2020/07/18 13:09:36
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
func buildTree(preorder []int, inorder []int) *TreeNode {
	if preorder == nil || inorder == nil || len(preorder) != len(inorder) {
		return nil
	}

	inIdx := make(map[int]int, len(inorder))
	for i := 0; i < len(inorder); i++ {
		inIdx[inorder[i]] = i
	}

	return _build(0, preorder, 0, len(preorder)-1, inIdx)
}

func _build(si int, pre []int, sp, ep int, inIdx map[int]int) *TreeNode {
	if sp > ep {
		return nil
	}

	root := &TreeNode{Val: pre[sp]}
	idx := inIdx[root.Val]
	llen := idx - si

	root.Left = _build(si, pre, sp+1, sp+llen, inIdx)
	root.Right = _build(idx+1, pre, sp+llen+1, ep, inIdx)

	return root
}

// @lc code=end
