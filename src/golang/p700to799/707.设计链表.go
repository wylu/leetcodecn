package p700to799

/*
 * @lc app=leetcode.cn id=707 lang=golang
 *
 * [707] 设计链表
 *
 * https://leetcode.cn/problems/design-linked-list/description/
 *
 * algorithms
 * Medium (34.53%)
 * Likes:    621
 * Dislikes: 0
 * Total Accepted:    166.8K
 * Total Submissions: 483.1K
 * Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n' +
  '[[],[1],[3],[1,2],[1],[1],[1]]'
 *
 * 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next
 * 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。
 *
 * 在链表类中实现这些功能：
 *
 *
 * get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
 * addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
 * addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
 * addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index
 * 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
 * deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
 *
 *
 *
 *
 * 示例：
 *
 * MyLinkedList linkedList = new MyLinkedList();
 * linkedList.addAtHead(1);
 * linkedList.addAtTail(3);
 * linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
 * linkedList.get(1);            //返回2
 * linkedList.deleteAtIndex(1);  //现在链表是1-> 3
 * linkedList.get(1);            //返回3
 *
 *
 *
 *
 * 提示：
 *
 *
 * 所有val值都在 [1, 1000] 之内。
 * 操作次数将在  [1, 1000] 之内。
 * 请不要使用内置的 LinkedList 库。
 *
 *
*/

/**
 * @File    :   707.设计链表.go
 * @Time    :   2022/09/23 20:02:15
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
type Node707 struct {
	Val  int
	Next *Node707
}

type MyLinkedList struct {
	head *Node707
	tail *Node707
}

func Constructor707() MyLinkedList {
	return MyLinkedList{head: &Node707{}}
}

func (this *MyLinkedList) getPrev(index int) *Node707 {
	if index < 0 {
		return nil
	}
	node := this.head
	for ; index > 0 && node != nil; index-- {
		node = node.Next
	}
	return node
}

func (this *MyLinkedList) Get(index int) int {
	if node := this.getPrev(index); node != nil && node.Next != nil {
		return node.Next.Val
	}
	return -1
}

func (this *MyLinkedList) AddAtHead(val int) {
	this.head.Next = &Node707{Val: val, Next: this.head.Next}
	if this.tail == nil {
		this.tail = this.head.Next
	}
}

func (this *MyLinkedList) AddAtTail(val int) {
	if this.tail == nil {
		this.AddAtHead(val)
		return
	}
	this.tail.Next = &Node707{Val: val}
	this.tail = this.tail.Next
}

func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if node := this.getPrev(index); node != nil {
		node.Next = &Node707{Val: val, Next: node.Next}
		if node.Next.Next == nil {
			this.tail = node.Next
		}
	}
}

func (this *MyLinkedList) DeleteAtIndex(index int) {
	if node := this.getPrev(index); node != nil && node.Next != nil {
		if node.Next == this.tail {
			this.tail = node
		}
		node.Next = node.Next.Next
	}
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */
// @lc code=end
