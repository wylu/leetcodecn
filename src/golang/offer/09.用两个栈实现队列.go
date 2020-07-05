package offer

/**
 * @File    :   09.用两个栈实现队列.go
 * @Time    :   2020/07/05 23:39:22
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// CQueue - A queue.
type CQueue struct {
	stack1 []int
	stack2 []int
}

// Constructor - Create a queue.
func Constructor() CQueue {
	return CQueue{
		stack1: []int{},
		stack2: []int{},
	}
}

// AppendTail offer a value to queue.
func (cq *CQueue) AppendTail(value int) {
	cq.stack1 = append(cq.stack1, value)
}

// DeleteHead poll a value from queue.
func (cq *CQueue) DeleteHead() int {
	if len(cq.stack2) == 0 {
		for i := len(cq.stack1) - 1; i >= 0; i-- {
			tail := len(cq.stack1) - 1
			cq.stack2 = append(cq.stack2, cq.stack1[tail])
			cq.stack1 = cq.stack1[:tail]
		}
	}
	tail := len(cq.stack2) - 1
	if tail < 0 {
		return -1
	}
	res := cq.stack2[tail]
	cq.stack2 = cq.stack2[:tail]
	return res
}

/**
 * Your CQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AppendTail(value);
 * param_2 := obj.DeleteHead();
 */
