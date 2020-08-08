package p600to699

/*
 * @lc app=leetcode.cn id=632 lang=golang
 *
 * [632] 最小区间
 *
 * https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists/description/
 *
 * algorithms
 * Hard (58.70%)
 * Likes:    224
 * Dislikes: 0
 * Total Accepted:    14.5K
 * Total Submissions: 24.6K
 * Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
 *
 * 你有 k 个升序排列的整数列表。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
 *
 * 我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。
 *
 *
 *
 * 示例：
 *
 * 输入：[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
 * 输出：[20,24]
 * 解释：
 * 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
 * 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
 * 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 给定的列表可能包含重复元素，所以在这里升序表示 >= 。
 * 1 <= k <= 3500
 * -10^5 <= 元素的值 <= 10^5
 * 对于使用Java的用户，请注意传入类型已修改为List<List<Integer>>。重置代码模板后可以看到这项改动。
 *
 *
 */

/**
 * @File    :   632.最小区间.go
 * @Time    :   2020/08/08 10:46:06
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start

// Node ...
type Node struct {
	val int
	row int
	col int
}

// Heap ...
type Heap struct {
	nodes  []Node
	length int
}

// NewHeap ...
func NewHeap(size int) *Heap {
	return &Heap{
		nodes:  make([]Node, size),
		length: 0,
	}
}

func (heap *Heap) sinking(node Node) {
	i := 0
	for i*2+1 < heap.length {
		a, b := i*2+1, i*2+2
		if b < heap.length && heap.nodes[b].val < heap.nodes[a].val {
			a = b
		}
		if heap.nodes[a].val >= node.val {
			break
		}
		heap.nodes[i] = heap.nodes[a]
		i = a
	}
	heap.nodes[i] = node
}

func (heap *Heap) floating(i int, node Node) {
	for i > 0 {
		p := (i - 1) / 2
		if heap.nodes[p].val <= node.val {
			break
		}
		heap.nodes[i] = heap.nodes[p]
		i = p
	}
	heap.nodes[i] = node
}

// Push ...
func (heap *Heap) Push(node Node) {
	heap.floating(heap.length, node)
	heap.length++
}

// Pop ...
func (heap *Heap) Pop() Node {
	node := heap.nodes[0]
	heap.length--
	heap.sinking(heap.nodes[heap.length])
	return node
}

func smallestRange(nums [][]int) []int {
	lo, hi := -1000000, 1000000
	maxVal := -1000000
	k := len(nums)
	pq := NewHeap(k)
	for i := 0; i < k; i++ {
		pq.Push(Node{nums[i][0], i, 0})
		if nums[i][0] > maxVal {
			maxVal = nums[i][0]
		}
	}

	for true {
		node := pq.Pop()
		if maxVal-node.val < hi-lo {
			lo, hi = node.val, maxVal
		}

		if node.col == len(nums[node.row])-1 {
			break
		}

		node = Node{val: nums[node.row][node.col+1], row: node.row, col: node.col + 1}
		if node.val > maxVal {
			maxVal = node.val
		}
		pq.Push(node)
	}

	return []int{lo, hi}
}

// @lc code=end
