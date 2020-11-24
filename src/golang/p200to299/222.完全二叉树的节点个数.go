package p200to299

/*
 * @lc app=leetcode.cn id=222 lang=golang
 *
 * [222] 完全二叉树的节点个数
 *
 * https://leetcode-cn.com/problems/count-complete-tree-nodes/description/
 *
 * algorithms
 * Medium (73.43%)
 * Likes:    339
 * Dislikes: 0
 * Total Accepted:    52.8K
 * Total Submissions: 69.8K
 * Testcase Example:  '[1,2,3,4,5,6]'
 *
 * 给出一个完全二叉树，求出该树的节点个数。
 *
 * 说明：
 *
 *
 * 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第
 * h 层，则该层包含 1~ 2^h 个节点。
 *
 * 示例:
 *
 * 输入:
 * ⁠   1
 * ⁠  / \
 * ⁠ 2   3
 * ⁠/ \  /
 * 4  5 6
 *
 * 输出: 6
 *
 */

/**
 * @File    :   222.完全二叉树的节点个数.go
 * @Time    :   2020/11/24 14:18:30
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：二分查找 + 位运算
 *
 * 对于任意二叉树，都可以通过广度优先搜索或深度优先搜索计算节点个数，
 * 时间复杂度和空间复杂度都是 O(n)，其中 n 是二叉树的节点个数。这道题
 * 规定了给出的是完全二叉树，因此可以利用完全二叉树的特性计算节点个数。
 *
 * 规定根节点位于第 0 层，完全二叉树的最大层数为 h。根据完全二叉树的
 * 特性可知，完全二叉树的最左边的节点一定位于最底层，因此从根节点出发，
 * 每次访问左子节点，直到遇到叶子节点，该叶子节点即为完全二叉树的最
 * 左边的节点，经过的路径长度即为最大层数 h。
 *
 * 当 0≤i<h 时，第 i 层包含 2^i个节点，最底层包含的节点数最少为 1，
 * 最多为 2^h。
 *
 * 当最底层包含 1 个节点时，完全二叉树的节点个数是 2^h
 * 当最底层包含 2^h 个节点时，完全二叉树的节点个数是 2^(h+1)-1
 *
 * 因此对于最大层数为 h 的完全二叉树，节点个数一定在 [2^h,2^(h+1)-1]
 * 的范围内，可以在该范围内通过二分查找的方式得到完全二叉树的节点个数。
 *
 * 具体做法是，根据节点个数范围的上下界得到当前需要判断的节点个数 k，
 * 如果第 k 个节点存在，则节点个数一定大于或等于 k，如果第 k 个节点
 * 不存在，则节点个数一定小于 k，由此可以将查找的范围缩小一半，直到
 * 得到节点个数。
 *
 * 如何判断第 k 个节点是否存在呢？如果第 k 个节点位于第 h 层，则 k
 * 的二进制表示包含 h+1 位，其中最高位是 1，其余各位从高到低表示从
 * 根节点到第 k 个节点的路径，0 表示移动到左子节点，1 表示移动到
 * 右子节点。通过位运算得到第 k 个节点对应的路径，判断该路径对应的
 * 节点是否存在，即可判断第 k 个节点是否存在。
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
func countNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}

	h, node := 0, root
	for node.Left != nil {
		h++
		node = node.Left
	}

	exist := func(k int) bool {
		bits, node := 1<<(h-1), root
		for bits > 0 && node != nil {
			if bits&k == 0 {
				node = node.Left
			} else {
				node = node.Right
			}
			bits >>= 1
		}
		return node != nil
	}

	left, right := 1<<h, (1<<(h+1))-1
	for left < right {
		mid := left + (right-left+1)/2
		if exist(mid) {
			left = mid
		} else {
			right = mid - 1
		}
	}

	return left
}

// @lc code=end
