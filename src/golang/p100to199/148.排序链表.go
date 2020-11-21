package p100to199

/*
 * @lc app=leetcode.cn id=148 lang=golang
 *
 * [148] 排序链表
 *
 * https://leetcode-cn.com/problems/sort-list/description/
 *
 * algorithms
 * Medium (67.73%)
 * Likes:    878
 * Dislikes: 0
 * Total Accepted:    118.4K
 * Total Submissions: 174.8K
 * Testcase Example:  '[4,2,1,3]'
 *
 * 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
 *
 * 进阶：
 *
 *
 * 你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [4,2,1,3]
 * 输出：[1,2,3,4]
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = [-1,5,3,4,0]
 * 输出：[-1,0,3,4,5]
 *
 *
 * 示例 3：
 *
 *
 * 输入：head = []
 * 输出：[]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中节点的数目在范围 [0, 5 * 10^4] 内
 * -10^5
 *
 *
 */

/**
 * @File    :   148.排序链表.go
 * @Time    :   2020/11/21 22:50:33
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
func sortList(head *ListNode) *ListNode {
	merge := func(head1, head2 *ListNode) *ListNode {
		dummy := &ListNode{Val: 0}
		i, j, k := head1, head2, dummy

		for i != nil && j != nil {
			if i.Val <= j.Val {
				k.Next = i
				i = i.Next
			} else {
				k.Next = j
				j = j.Next
			}
			k = k.Next
		}

		if i != nil {
			k.Next = i
		}
		if j != nil {
			k.Next = j
		}
		return dummy.Next
	}

	var mergeSort func(head, tail *ListNode) *ListNode
	mergeSort = func(head, tail *ListNode) *ListNode {
		if head == nil {
			return head
		}
		if head.Next == tail {
			head.Next = nil
			return head
		}

		slow, fast := head, head
		for fast != tail {
			slow = slow.Next
			fast = fast.Next
			if fast != tail {
				fast = fast.Next
			}
		}

		return merge(mergeSort(head, slow), mergeSort(slow, tail))
	}

	return mergeSort(head, nil)
}

// @lc code=end
