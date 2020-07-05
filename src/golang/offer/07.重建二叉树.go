package offer

/**
 * @File    :   07.重建二叉树.go
 * @Time    :   2020/07/05 23:27:12
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
func buildTree(preorder []int, inorder []int) *TreeNode {
	if preorder == nil || inorder == nil || len(preorder) != len(inorder) {
		return nil
	}
	inIdx := make(map[int]int, len(inorder))
	for i := 0; i < len(inorder); i++ {
		inIdx[inorder[i]] = i
	}
	return build(0, preorder, 0, len(preorder)-1, inIdx)
}

func build(si int, pre []int, sp, ep int, inIdx map[int]int) *TreeNode {
	if sp > ep {
		return nil
	}

	root := TreeNode{Val: pre[sp]}
	idx := inIdx[root.Val]
	llen := idx - si

	root.Left = build(si, pre, sp+1, sp+llen, inIdx)
	root.Right = build(idx+1, pre, sp+llen+1, ep, inIdx)
	return &root
}
