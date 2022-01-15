package p300to399

import "container/heap"

/*
 * @lc app=leetcode.cn id=373 lang=golang
 *
 * [373] 查找和最小的 K 对数字
 *
 * https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/description/
 *
 * algorithms
 * Medium (41.26%)
 * Likes:    330
 * Dislikes: 0
 * Total Accepted:    35.8K
 * Total Submissions: 86.8K
 * Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
 *
 * 给定两个以 升序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。
 *
 * 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。
 *
 * 请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
 * 输出: [1,2],[1,4],[1,6]
 * 解释: 返回序列中的前 3 对数：
 * ⁠    [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
 *
 *
 * 示例 2:
 *
 *
 * 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
 * 输出: [1,1],[1,1]
 * 解释: 返回序列中的前 2 对数：
 * [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 *
 *
 * 示例 3:
 *
 *
 * 输入: nums1 = [1,2], nums2 = [3], k = 3
 * 输出: [1,3],[2,3]
 * 解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
 *
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= nums1.length, nums2.length <= 10^5
 * -10^9 <= nums1[i], nums2[i] <= 10^9
 * nums1 和 nums2 均为升序排列
 * 1 <= k <= 1000
 *
 *
 */

/**
 * @File    :   373.查找和最小的-k-对数字.go
 * @Time    :   2022/01/14 19:36:05
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：优先队列
 * 思路
 *
 * 本题与「719. 找出第 k 小的距离对」相似，可以参考该题的解法。对于已经
 * 按升序排列的两个数组 nums1, nums2，长度分别为 length1, length2，我们
 * 可以知道和最小的数对一定为 (nums1[0], nums2[0])，和最大的数对一定为
 * (nums1[length1-1], nums2[length2-1])。本题要求找到最小的 k 个数对，
 * 最直接的办法是可以将所有的数对求出来，然后利用排序或者 TopK 解法求出
 * 最小的 k 个数对即可。实际求解时可以不用求出所有的数对，只需从所有符合
 * 待选的数对中选出最小的即可，假设当前已选的前 n 小数对的索引分别为
 * (a1,b1),(a2,b2),(a3,b3),...,(an,bn)，由于两个数组都是按照升序进行
 * 排序的，则可以推出第 n+1 小的数对的索引选择范围为 (a1+1,b1),(a1,b1+1),
 * (a2+1,b2),(a2,b2+1),(a3+1,b3),(a3,b3+1),...,(an+1,bn),(an,bn+1)，
 *
 * 假设我们利用堆的特性可以求出待选范围中最小数对的索引为 (ai,bi)，同时
 * 将新的待选的数对 (ai+1,bi),(ai,bi+1) 加入到堆中，直到我们选出 k 个
 * 数对即可。
 *
 * 如果我们每次都将已选的数对 (ai,bi) 的待选索引 (ai+1,bi),(ai,bi+1)
 * 加入到堆中则可能出现重复的问题，一般需要设置标记位解决去重的问题。我们
 * 可以将 nums1 的前 k 个索引数对 (0,0),(1,0),...,(k-1,0) 加入到队列中，
 * 每次从队列中取出元素 (x,y) 时，我们只需要将 nums2 的索引增加即可，
 * 这样避免了重复加入元素的问题。
 */

// @lc code=start
type pair373 struct{ i, j int }
type hp373 struct {
	data         []pair373
	nums1, nums2 []int
}

func (h hp373) Len() int { return len(h.data) }
func (h hp373) Less(i, j int) bool {
	a, b := h.data[i], h.data[j]
	return h.nums1[a.i]+h.nums2[a.j] < h.nums1[b.i]+h.nums2[b.j]
}
func (h hp373) Swap(i, j int)       { h.data[i], h.data[j] = h.data[j], h.data[i] }
func (h *hp373) Push(v interface{}) { h.data = append(h.data, v.(pair373)) }
func (h *hp373) Pop() interface{}   { a := h.data; v := a[len(a)-1]; h.data = a[:len(a)-1]; return v }

func kSmallestPairs(nums1 []int, nums2 []int, k int) [][]int {
	m, n := len(nums1), len(nums2)
	h := &hp373{nil, nums1, nums2}
	for i := 0; i < k && i < m; i++ {
		h.data = append(h.data, pair373{i, 0})
	}

	ans := [][]int{}
	for h.Len() > 0 && len(ans) < k {
		p := heap.Pop(h).(pair373)
		i, j := p.i, p.j
		ans = append(ans, []int{nums1[i], nums2[j]})
		if j+1 < n {
			heap.Push(h, pair373{i, j + 1})
		}
	}

	return ans
}

// @lc code=end

// func kSmallestPairs(nums1 []int, nums2 []int, k int) [][]int {
// 	min := func(x, y int) int {
// 		if x < y {
// 			return x
// 		}
// 		return y
// 	}

// 	ans := [][]int{}
// 	m, n := min(len(nums1), k), min(len(nums2), k)
// 	for i := 0; i < m; i++ {
// 		for j := 0; j < n; j++ {
// 			ans = append(ans, []int{nums1[i], nums2[j]})
// 		}
// 	}

// 	sort.Slice(ans, func(i, j int) bool {
// 		return ans[i][0]+ans[i][1] < ans[j][0]+ans[j][1]
// 	})

// 	return ans[:min(len(ans), k)]
// }
