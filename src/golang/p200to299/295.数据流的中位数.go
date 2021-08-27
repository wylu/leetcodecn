package p200to299

import "container/heap"

/*
 * @lc app=leetcode.cn id=295 lang=golang
 *
 * [295] 数据流的中位数
 *
 * https://leetcode-cn.com/problems/find-median-from-data-stream/description/
 *
 * algorithms
 * Hard (52.09%)
 * Likes:    516
 * Dislikes: 0
 * Total Accepted:    57.1K
 * Total Submissions: 109.7K
 * Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
  '[[],[1],[2],[],[3],[]]'
 *
 * 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
 *
 * 例如，
 *
 * [2,3,4] 的中位数是 3
 *
 * [2,3] 的中位数是 (2 + 3) / 2 = 2.5
 *
 * 设计一个支持以下两种操作的数据结构：
 *
 *
 * void addNum(int num) - 从数据流中添加一个整数到数据结构中。
 * double findMedian() - 返回目前所有元素的中位数。
 *
 *
 * 示例：
 *
 * addNum(1)
 * addNum(2)
 * findMedian() -> 1.5
 * addNum(3)
 * findMedian() -> 2
 *
 * 进阶:
 *
 *
 * 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
 * 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
 *
 *
*/

/**
 * @File    :   295.数据流的中位数.go
 * @Time    :   2021/08/27 21:16:37
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
type minHeap []int

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(v interface{}) { *h = append(*h, v.(int)) }
func (h *minHeap) Pop() interface{}   { o := *h; v := o[len(o)-1]; *h = o[:len(o)-1]; return v }

type maxHeap []int

func (h maxHeap) Len() int            { return len(h) }
func (h maxHeap) Less(i, j int) bool  { return h[i] > h[j] }
func (h maxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(v interface{}) { *h = append(*h, v.(int)) }
func (h *maxHeap) Pop() interface{}   { o := *h; v := o[len(o)-1]; *h = o[:len(o)-1]; return v }

type MedianFinder struct {
	minhp *minHeap
	maxhp *maxHeap
}

/** initialize your data structure here. */
func Constructor() MedianFinder {
	return MedianFinder{
		minhp: &minHeap{},
		maxhp: &maxHeap{},
	}
}

func (mf *MedianFinder) AddNum(num int) {
	heap.Push(mf.minhp, num)
	heap.Push(mf.maxhp, heap.Pop(mf.minhp))
	if len(*mf.maxhp) > len(*mf.minhp) {
		heap.Push(mf.minhp, heap.Pop(mf.maxhp))
	}
}

func (mf *MedianFinder) FindMedian() float64 {
	if len(*mf.minhp) > len(*mf.maxhp) {
		return float64((*mf.minhp)[0])
	}
	return float64((*mf.minhp)[0]+(*mf.maxhp)[0]) / 2
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */
// @lc code=end
