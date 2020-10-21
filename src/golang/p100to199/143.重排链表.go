package p100to199

/*
 * @lc app=leetcode.cn id=143 lang=golang
 *
 * [143] 重排链表
 *
 * https://leetcode-cn.com/problems/reorder-list/description/
 *
 * algorithms
 * Medium (56.55%)
 * Likes:    340
 * Dislikes: 0
 * Total Accepted:    43.4K
 * Total Submissions: 76K
 * Testcase Example:  '[1,2,3,4]'
 *
 * 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
 * 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
 *
 * 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
 *
 * 示例 1:
 *
 * 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
 *
 * 示例 2:
 *
 * 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
 *
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode) {
	nodes := []*ListNode{}
	for head != nil {
		nodes = append(nodes, head)
		head = head.Next
	}

	i, j := 0, len(nodes)-1
	dummy := &ListNode{Val: 0}
	cur := dummy
	for i < j {
		cur.Next = nodes[i]
		cur = cur.Next
		i++
		cur.Next = nodes[j]
		cur = cur.Next
		j--
	}

	if i == j {
		cur.Next = nodes[i]
		cur.Next.Next = nil
	} else {
		cur.Next = nil
	}
}

// @lc code=end
