package p100to199

/*
 * @lc app=leetcode.cn id=117 lang=golang
 *
 * [117] 填充每个节点的下一个右侧节点指针 II
 *
 * https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/description/
 *
 * algorithms
 * Medium (54.75%)
 * Likes:    230
 * Dislikes: 0
 * Total Accepted:    36.6K
 * Total Submissions: 66.8K
 * Testcase Example:  '[1,2,3,4,5,null,7]'
 *
 * 给定一个二叉树
 *
 * struct Node {
 * ⁠ int val;
 * ⁠ Node *left;
 * ⁠ Node *right;
 * ⁠ Node *next;
 * }
 *
 * 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
 *
 * 初始状态下，所有 next 指针都被设置为 NULL。
 *
 *
 *
 * 进阶：
 *
 *
 * 你只能使用常量级额外空间。
 * 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 *
 *
 *
 *
 * 示例：
 *
 *
 *
 * 输入：root = [1,2,3,4,5,null,7]
 * 输出：[1,#,2,3,#,4,5,7,#]
 * 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
 *
 *
 *
 * 提示：
 *
 *
 * 树中的节点数小于 6000
 * -100 <= node.val <= 100
 *
 *
 *
 *
 *
 *
 *
 */

/**
 * @File    :   117.填充每个节点的下一个右侧节点指针-ii.go
 * @Time    :   2020/09/28 10:34:09
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func connect(root *Node) *Node {
	tree := root

	for root != nil {
		dummy := &Node{}
		cur := dummy

		for root != nil {
			if root.Left != nil {
				cur.Next = root.Left
				cur = root.Left
			}
			if root.Right != nil {
				cur.Next = root.Right
				cur = root.Right
			}
			root = root.Next
		}

		root = dummy.Next
	}

	return tree
}

// @lc code=end
