package common

/**
 * @File    :   treenode.go
 * @Time    :   2020/07/05 16:42:21
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// TreeNode - Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// MkTreeFromPreAndIn build a binary tree using preorder traversal sequence
// and inorder traversal sequence.
// Note: All node values must be unique.
//
// @param pre Preorder traversal sequence.
// @param in Inorder traversal sequence.
// @return Root of binary tree.
func MkTreeFromPreAndIn(pre, in []int) *TreeNode {
	if pre == nil || in == nil || len(pre) != len(in) {
		return nil
	}

	inIdx := make(map[int]int, len(in))
	for i := 0; i < len(in); i++ {
		inIdx[in[i]] = i
	}

	return mkFromPreAndIn(0, pre, 0, len(pre)-1, inIdx)
}

func mkFromPreAndIn(si int, pre []int, sp, ep int, inIdx map[int]int) *TreeNode {
	if sp > ep {
		return nil
	}

	root := TreeNode{Val: pre[sp]}
	idx := inIdx[root.Val]
	llen := idx - si

	root.Left = mkFromPreAndIn(si, pre, sp+1, sp+llen, inIdx)
	root.Right = mkFromPreAndIn(idx+1, pre, sp+llen+1, ep, inIdx)
	return &root
}

// BuildTreeFromPreAndIn build a binary tree using preorder traversal sequence
// and inorder traversal sequence.
//
// @param pre Preorder traversal sequence.
// @param in Inorder traversal sequence.
// @return Root of binary tree.
func BuildTreeFromPreAndIn(pre, in []int) *TreeNode {
	if pre == nil || in == nil || len(pre) != len(in) {
		return nil
	}
	return buildFromPreAndIn(pre, 0, len(pre)-1, in, 0, len(in)-1)
}

func buildFromPreAndIn(pre []int, sp, ep int, in []int, si, ei int) *TreeNode {
	if sp > ep {
		return nil
	}

	root := TreeNode{Val: pre[sp]}
	// 中序遍历序列根结点索引
	idx := si
	for idx <= ei && in[idx] != root.Val {
		idx++
	}

	// 左子树序列长度
	llen := idx - si
	// 左右子树序列中点（右子树序列起始点）
	mpre := sp + 1 + llen

	root.Left = buildFromPreAndIn(pre, sp+1, mpre-1, in, si, idx-1)
	root.Right = buildFromPreAndIn(pre, mpre, ep, in, idx+1, ei)
	return &root
}

// MkTreeFromInAndPost 利用中序遍历序列和后序遍历序列构建一颗二叉树
// 前提：所有结点的值唯一
//
// @param in 中序遍历序列
// @param post 后序遍历序列
// @return 返回树的根结点
func MkTreeFromInAndPost(in, post []int) *TreeNode {
	if in == nil || post == nil || len(in) != len(post) {
		return nil
	}

	inIdx := make(map[int]int, len(in))
	for i := 0; i < len(in); i++ {
		inIdx[in[i]] = i
	}

	return mkFromInAndPost(0, post, 0, len(post)-1, inIdx)
}

func mkFromInAndPost(si int, post []int, sp, ep int, inIdx map[int]int) *TreeNode {
	if sp > ep {
		return nil
	}

	root := TreeNode{Val: post[ep]}
	idx := inIdx[root.Val]
	llen := idx - si

	root.Left = mkFromInAndPost(si, post, sp, sp+llen-1, inIdx)
	root.Right = mkFromInAndPost(idx+1, post, sp+llen, ep-1, inIdx)
	return &root
}

// BuildTreeFromInAndPost 利用中序遍历序列和后序遍历序列构建一颗二叉树
//
// @param in 中序遍历序列
// @param post 后序遍历序列
// @return 返回树的根结点
func BuildTreeFromInAndPost(in, post []int) *TreeNode {
	if in == nil || post == nil || len(in) != len(post) {
		return nil
	}
	return buildFromInAndPost(in, 0, len(in)-1, post, 0, len(post)-1)
}

func buildFromInAndPost(in []int, si, ei int, post []int, sp, ep int) *TreeNode {
	if sp > ep {
		return nil
	}

	root := TreeNode{Val: post[ep]}
	// 中序遍历序列根结点索引
	idx := si
	for idx <= ei && in[idx] != root.Val {
		idx++
	}

	// 左子树序列长度
	llen := idx - si
	// 左右子树序列中点（右子树序列起始点）
	mpost := sp + llen

	root.Left = buildFromInAndPost(in, si, idx-1, post, sp, mpost-1)
	root.Right = buildFromInAndPost(in, idx+1, ei, post, mpost, ep-1)
	return &root
}
