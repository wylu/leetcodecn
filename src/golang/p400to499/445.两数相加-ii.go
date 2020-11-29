package p400to499

/*
 * @lc app=leetcode.cn id=445 lang=golang
 *
 * [445] 两数相加 II
 *
 * https://leetcode-cn.com/problems/add-two-numbers-ii/description/
 *
 * algorithms
 * Medium (58.07%)
 * Likes:    307
 * Dislikes: 0
 * Total Accepted:    56K
 * Total Submissions: 96.5K
 * Testcase Example:  '[7,2,4,3]\n[5,6,4]'
 *
 * 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
 *
 * 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
 *
 *
 *
 * 进阶：
 *
 * 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
 *
 *
 *
 * 示例：
 *
 * 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
 * 输出：7 -> 8 -> 0 -> 7
 *
 *
 */

/**
 * @File    :   445.两数相加-ii.go
 * @Time    :   2020/11/29 21:25:40
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
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	fill := func(nums *[]int, head *ListNode) {
		for head != nil {
			*nums = append(*nums, head.Val)
			head = head.Next
		}
	}

	nums1, nums2 := []int{}, []int{}
	fill(&nums1, l1)
	fill(&nums2, l2)

	var ans *ListNode
	carry := 0

	for len(nums1) > 0 || len(nums2) > 0 || carry > 0 {
		if len(nums1) > 0 {
			carry += nums1[len(nums1)-1]
			nums1 = nums1[:len(nums1)-1]
		}
		if len(nums2) > 0 {
			carry += nums2[len(nums2)-1]
			nums2 = nums2[:len(nums2)-1]
		}
		ans = &ListNode{Val: carry % 10, Next: ans}
		carry /= 10
	}

	return ans
}

// @lc code=end
