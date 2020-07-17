package p200to299

/**
 * @File    :   datastruct.go
 * @Time    :   2020/07/05 22:41:11
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :   定义一些公共数据结构
 */

// ListNode - Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// MakeList - make a linked list
func MakeList(nums ...int) *ListNode {
	dummy := &ListNode{}
	node := dummy
	for _, num := range nums {
		node.Next = &ListNode{Val: num}
		node = node.Next
	}
	return dummy.Next
}

// TreeNode - Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
