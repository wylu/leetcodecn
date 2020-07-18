package p100to199

/*
 * @lc app=leetcode.cn id=106 lang=golang
 *
 * [106] 从中序与后序遍历序列构造二叉树
 *
 * https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
 *
 * algorithms
 * Medium (68.83%)
 * Likes:    242
 * Dislikes: 0
 * Total Accepted:    42.9K
 * Total Submissions: 62.1K
 * Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
 *
 * 根据一棵树的中序遍历与后序遍历构造二叉树。
 *
 * 注意:
 * 你可以假设树中没有重复的元素。
 *
 * 例如，给出
 *
 * 中序遍历 inorder = [9,3,15,20,7]
 * 后序遍历 postorder = [9,15,7,20,3]
 *
 * 返回如下的二叉树：
 *
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 *
 *
 */

/**
 * @File    :   106.从中序与后序遍历序列构造二叉树.go
 * @Time    :   2020/07/18 13:32:12
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
func buildTree106(inorder []int, postorder []int) *TreeNode {
	if inorder == nil || postorder == nil || len(inorder) != len(postorder) {
		return nil
	}

	inIdx := make(map[int]int, len(inorder))
	for i := 0; i < len(inorder); i++ {
		inIdx[inorder[i]] = i
	}

	return _build106(0, postorder, 0, len(postorder)-1, inIdx)
}

func _build106(si int, post []int, sp, ep int, inIdx map[int]int) *TreeNode {
	if sp > ep {
		return nil
	}

	root := &TreeNode{Val: post[ep]}
	idx := inIdx[root.Val]
	llen := idx - si

	root.Left = _build106(si, post, sp, sp+llen-1, inIdx)
	root.Right = _build106(idx+1, post, sp+llen, ep-1, inIdx)

	return root
}

// @lc code=end
