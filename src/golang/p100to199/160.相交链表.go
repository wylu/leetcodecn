package p100to199

/*
 * @lc app=leetcode.cn id=160 lang=golang
 *
 * [160] 相交链表
 *
 * https://leetcode-cn.com/problems/intersection-of-two-linked-lists/description/
 *
 * algorithms
 * Easy (60.25%)
 * Likes:    1220
 * Dislikes: 0
 * Total Accepted:    272.6K
 * Total Submissions: 452.4K
 * Testcase Example:  '8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3'
 *
 * 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
 *
 * 图示两个链表在节点 c1 开始相交：
 *
 *
 *
 * 题目数据 保证 整个链式结构中不存在环。
 *
 * 注意，函数返回结果后，链表必须 保持其原始结构 。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2,
 * skipB = 3
 * 输出：Intersected at '8'
 * 解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
 * 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
 * 在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
 *
 *
 * 示例 2：
 *
 *
 *
 *
 * 输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB
 * = 1
 * 输出：Intersected at '2'
 * 解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
 * 从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
 * 在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
 *
 *
 * 示例 3：
 *
 *
 *
 *
 * 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
 * 输出：null
 * 解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
 * 由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
 * 这两个链表不相交，因此返回 null 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * listA 中节点数目为 m
 * listB 中节点数目为 n
 * 0 <= m, n <= 3 * 10^4
 * 1 <= Node.val <= 10^5
 * 0 <= skipA <= m
 * 0 <= skipB <= n
 * 如果 listA 和 listB 没有交点，intersectVal 为 0
 * 如果 listA 和 listB 有交点，intersectVal == listA[skipA + 1] == listB[skipB + 1]
 *
 *
 *
 *
 * 进阶：你能否设计一个时间复杂度 O(n) 、仅用 O(1) 内存的解决方案？
 *
 */

/**
 * @File    :   160.相交链表.go
 * @Time    :   2021/06/05 08:54:42
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 双指针法
 *
 * 创建两个指针 ca 和 cb，分别初始化为链表 A 和 B 的头结点。
 * 然后让它们同时向后逐结点遍历。
 * 当 ca 到达链表的尾部时，将它重定位到链表 B 的头结点；
 * 当 cb 到达链表的尾部时，将它重定位到链表 A 的头结点；
 * 若在某一时刻 ca 和 cb 相遇，则 ca/cb 为相交结点。
 *
 * 为什么这样可行, 可以这样思考:
 *
 * 设 a 为链表 A 独有的部分，b 为链表 B 独有的部分，all 为 A 和 B
 * 共有的部分。则有：
 *   a + all + b = b + all + a
 *
 * 距离相同，速度相同，ca 和 cb 最终必定相遇于相交结点（如果存在，
 * 否则 ca 和 cb 会因同时到达链表尾部而终止循环）
 */

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// @lc code=start
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	ca, cb := headA, headB
	for ca != cb {
		if ca != nil {
			ca = ca.Next
		} else {
			ca = headB
		}

		if cb != nil {
			cb = cb.Next
		} else {
			cb = headA
		}
	}
	return ca
}

// @lc code=end
