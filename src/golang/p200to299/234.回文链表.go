package p200to299

/*
 * @lc app=leetcode.cn id=234 lang=golang
 *
 * [234] 回文链表
 *
 * https://leetcode-cn.com/problems/palindrome-linked-list/description/
 *
 * algorithms
 * Easy (42.31%)
 * Likes:    564
 * Dislikes: 0
 * Total Accepted:    105.5K
 * Total Submissions: 247.8K
 * Testcase Example:  '[1,2]'
 *
 * 请判断一个链表是否为回文链表。
 *
 * 示例 1:
 *
 * 输入: 1->2
 * 输出: false
 *
 * 示例 2:
 *
 * 输入: 1->2->2->1
 * 输出: true
 *
 *
 * 进阶：
 * 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
 *
 */

/**
 * @File    :   234.回文链表.go
 * @Time    :   2020/07/17 22:04:26
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
func isPalindrome(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return true
	}

	// 快慢指针寻找链表中点
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	// 反转中点之后的链表
	l1, rl2 := head, reverseList(slow)

	for rl2 != nil {
		if l1.Val != rl2.Val {
			return false
		}
		l1, rl2 = l1.Next, rl2.Next
	}

	return true
}

func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	var pre *ListNode
	cur := head
	for cur != nil {
		tmp := cur.Next
		cur.Next = pre
		pre = cur
		cur = tmp
	}
	return pre
}

// @lc code=end

// version 2
// func isPalindrome(head *ListNode) bool {
// 	if head == nil || head.Next == nil {
// 		return true
// 	}

// 	n := 0
// 	for node := head; node != nil; node = node.Next {
// 		n++
// 	}

// 	l1, l2 := head, head
// 	for i := 0; i < n/2; i++ {
// 		l2 = l2.Next
// 	}

// 	rl2 := reverseList(l2)
// 	for i := 0; i < n/2; i++ {
// 		if l1.Val != rl2.Val {
// 			return false
// 		}
// 		l1, rl2 = l1.Next, rl2.Next
// 	}

// 	return true
// }

// func reverseList(head *ListNode) *ListNode {
// 	if head == nil || head.Next == nil {
// 		return head
// 	}

// 	var pre *ListNode
// 	cur := head
// 	for cur != nil {
// 		tmp := cur.Next
// 		cur.Next = pre
// 		pre = cur
// 		cur = tmp
// 	}
// 	return pre
// }

// version 1
// func isPalindrome(head *ListNode) bool {
// 	if head == nil || head.Next == nil {
// 		return true
// 	}

// 	vals := []int{}
// 	for head != nil {
// 		vals = append(vals, head.Val)
// 		head = head.Next
// 	}

// 	for i, j := 0, len(vals)-1; i < j; i, j = i+1, j-1 {
// 		if vals[i] != vals[j] {
// 			return false
// 		}
// 	}

// 	return true
// }
