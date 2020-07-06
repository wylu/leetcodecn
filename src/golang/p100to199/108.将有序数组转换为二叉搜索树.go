package p100to199

/*
 * @lc app=leetcode.cn id=108 lang=golang
 *
 * [108] 将有序数组转换为二叉搜索树
 *
 * https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/description/
 *
 * algorithms
 * Easy (71.49%)
 * Likes:    492
 * Dislikes: 0
 * Total Accepted:    91.4K
 * Total Submissions: 125.2K
 * Testcase Example:  '[-10,-3,0,5,9]'
 *
 * 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
 *
 * 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
 *
 * 示例:
 *
 * 给定有序数组: [-10,-3,0,5,9],
 *
 * 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
 *
 * ⁠     0
 * ⁠    / \
 * ⁠  -3   9
 * ⁠  /   /
 * ⁠-10  5
 *
 *
 */

/**
 * @File    :   108.将有序数组转换为二叉搜索树.go
 * @Time    :   2020/07/03 21:52:20
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
func sortedArrayToBST(nums []int) *TreeNode {
	if nums == nil {
		return nil
	}
	return build(nums, 0, len(nums)-1)
}

func build(nums []int, left, right int) *TreeNode {
	if left > right {
		return nil
	}
	mid := (left + right + 1) / 2
	root := TreeNode{Val: nums[mid]}
	root.Left = build(nums, left, mid-1)
	root.Right = build(nums, mid+1, right)
	return &root
}

// @lc code=end
