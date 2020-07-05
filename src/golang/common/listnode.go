package common

import (
	"strconv"
	"strings"
)

// ListNode - Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// ToString - convert linked list to string.
func (node *ListNode) ToString() string {
	outs := []string{}
	for node != nil {
		outs = append(outs, strconv.Itoa(node.Val))
		node = node.Next
	}
	return strings.Join(outs, " -> ")
}

// MkLinkedList - make a linked list using given numbers.
func MkLinkedList(nums ...int) *ListNode {
	head := &ListNode{}
	cur := head
	for _, x := range nums {
		cur.Next = &ListNode{Val: x}
		cur = cur.Next
	}
	return head.Next
}
