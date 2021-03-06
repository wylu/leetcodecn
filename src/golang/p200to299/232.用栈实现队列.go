package p200to299

/*
 * @lc app=leetcode.cn id=232 lang=golang
 *
 * [232] 用栈实现队列
 *
 * https://leetcode-cn.com/problems/implement-queue-using-stacks/description/
 *
 * algorithms
 * Easy (68.63%)
 * Likes:    356
 * Dislikes: 0
 * Total Accepted:    109.7K
 * Total Submissions: 159.9K
 * Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
 *
 * 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：
 *
 * 实现 MyQueue 类：
 *
 *
 * void push(int x) 将元素 x 推到队列的末尾
 * int pop() 从队列的开头移除并返回元素
 * int peek() 返回队列开头的元素
 * boolean empty() 如果队列为空，返回 true ；否则，返回 false
 *
 *
 *
 *
 * 说明：
 *
 *
 * 你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty
 * 操作是合法的。
 * 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
 *
 *
 *
 *
 * 进阶：
 *
 *
 * 你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n)
 * ，即使其中一个操作可能花费较长时间。
 *
 *
 *
 *
 * 示例：
 *
 *
 * 输入：
 * ["MyQueue", "push", "push", "peek", "pop", "empty"]
 * [[], [1], [2], [], [], []]
 * 输出：
 * [null, null, null, 1, 1, false]
 *
 * 解释：
 * MyQueue myQueue = new MyQueue();
 * myQueue.push(1); // queue is: [1]
 * myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
 * myQueue.peek(); // return 1
 * myQueue.pop(); // return 1, queue is [2]
 * myQueue.empty(); // return false
 *
 *
 *
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= x <= 9
 * 最多调用 100 次 push、pop、peek 和 empty
 * 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）
 *
 *
 */

/**
 * @File    :   232.用栈实现队列.go
 * @Time    :   2021/03/06 22:11:36
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start

// MyQueue ...
type MyQueue struct {
	st1 []int
	st2 []int
}

// Constructor - Initialize your data structure here.
func Constructor() MyQueue {
	return MyQueue{}
}

// Push - Push element x to the back of queue.
func (q *MyQueue) Push(x int) {
	q.st1 = append(q.st1, x)
}

// Pop - Removes the element from in front of queue and returns that element.
func (q *MyQueue) Pop() int {
	res := q.Peek()
	q.st2 = q.st2[:len(q.st2)-1]
	return res
}

// Peek - Get the front element.
func (q *MyQueue) Peek() int {
	if len(q.st2) == 0 {
		for len(q.st1) > 0 {
			q.st2 = append(q.st2, q.st1[len(q.st1)-1])
			q.st1 = q.st1[:len(q.st1)-1]
		}
	}
	return q.st2[len(q.st2)-1]
}

// Empty - Returns whether the queue is empty.
func (q *MyQueue) Empty() bool {
	return len(q.st1) == 0 && len(q.st2) == 0
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
// @lc code=end
