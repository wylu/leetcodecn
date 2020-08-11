package p1to99

/*
 * @lc app=leetcode.cn id=99 lang=golang
 *
 * [99] 恢复二叉搜索树
 *
 * https://leetcode-cn.com/problems/recover-binary-search-tree/description/
 *
 * algorithms
 * Hard (62.09%)
 * Likes:    319
 * Dislikes: 0
 * Total Accepted:    36.3K
 * Total Submissions: 58.5K
 * Testcase Example:  '[1,3,null,null,2]'
 *
 * 二叉搜索树中的两个节点被错误地交换。
 *
 * 请在不改变其结构的情况下，恢复这棵树。
 *
 * 示例 1:
 *
 * 输入: [1,3,null,null,2]
 *
 *   1
 *  /
 * 3
 *  \
 *   2
 *
 * 输出: [3,1,null,null,2]
 *
 *   3
 *  /
 * 1
 *  \
 *   2
 *
 *
 * 示例 2:
 *
 * 输入: [3,1,4,null,null,2]
 *
 * ⁠  3
 * ⁠ / \
 * 1   4
 *    /
 *   2
 *
 * 输出: [2,1,4,null,null,3]
 *
 * ⁠  2
 *  ⁠/ \
 * 1   4
 *    /
 * ⁠  3
 *
 * 进阶:
 *
 *
 * 使用 O(n) 空间复杂度的解法很容易实现。
 * 你能想出一个只使用常数空间的解决方案吗？
 *
 *
 */

/**
 * @File    :   99.恢复二叉搜索树.go
 * @Time    :   2020/08/11 22:59:58
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
func recoverTree(root *TreeNode) {
	if root == nil {
		return
	}

	var first, second, pre *TreeNode

	for root != nil {
		if root.Left == nil {
			if pre != nil && root.Val < pre.Val {
				second = root
				if first == nil {
					first = pre
				}
			}
			pre = root
			root = root.Right
			continue
		}

		precursor := root.Left
		for precursor.Right != nil && precursor.Right != root {
			precursor = precursor.Right
		}

		if precursor.Right == nil {
			precursor.Right = root
			root = root.Left
		} else {
			if pre != nil && root.Val < pre.Val {
				second = root
				if first == nil {
					first = pre
				}
			}
			precursor.Right = nil
			pre = root
			root = root.Right
		}
	}

	first.Val, second.Val = second.Val, first.Val
}

// @lc code=end
