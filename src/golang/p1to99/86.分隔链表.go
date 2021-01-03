package p1to99

/*
 * @lc app=leetcode.cn id=86 lang=golang
 *
 * [86] 分隔链表
 *
 * https://leetcode-cn.com/problems/partition-list/description/
 *
 * algorithms
 * Medium (60.91%)
 * Likes:    310
 * Dislikes: 0
 * Total Accepted:    66.5K
 * Total Submissions: 109.2K
 * Testcase Example:  '[1,4,3,2,5,2]\n3'
 *
 * 给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。
 *
 * 你应当保留两个分区中每个节点的初始相对位置。
 *
 *
 *
 * 示例：
 *
 *
 * 输入：head = 1->4->3->2->5->2, x = 3
 * 输出：1->2->2->4->3->5
 *
 *
 */

/**
 * @File    :   86.分隔链表.go
 * @Time    :   2021/01/03 12:11:19
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func partition(head *ListNode, x int) *ListNode {
	h1, h2 := &ListNode{}, &ListNode{}
	c1, c2 := h1, h2

	for head != nil {
		if head.Val < x {
			c1.Next = head
			c1 = c1.Next
		} else {
			c2.Next = head
			c2 = c2.Next
		}
		head = head.Next
	}

	c1.Next = h2.Next
	c2.Next = nil
	return h1.Next
}

// @lc code=end
