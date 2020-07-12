package p300to399

import "sort"

/*
 * @lc app=leetcode.cn id=315 lang=golang
 *
 * [315] 计算右侧小于当前元素的个数
 *
 * https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/description/
 *
 * algorithms
 * Hard (38.20%)
 * Likes:    334
 * Dislikes: 0
 * Total Accepted:    25.5K
 * Total Submissions: 65.4K
 * Testcase Example:  '[5,2,6,1]'
 *
 * 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于
 * nums[i] 的元素的数量。
 *
 * 示例:
 *
 * 输入: [5,2,6,1]
 * 输出: [2,1,1,0]
 * 解释:
 * 5 的右侧有 2 个更小的元素 (2 和 1).
 * 2 的右侧仅有 1 个更小的元素 (1).
 * 6 的右侧有 1 个更小的元素 (1).
 * 1 的右侧有 0 个更小的元素.
 *
 *
 */

/**
 * @File    :   315.计算右侧小于当前元素的个数.go
 * @Time    :   2020/07/11 18:33:37
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 转化为动态维护前缀和的问题，用离散化优化空间
 *
 * 预备知识
 *「树状数组」是一种可以动态维护序列前缀和的数据结构，它的功能是：
 * - 单点更新 update(i, v)： 把序列 i 位置的数加上一个值 v，在该题中 v = 1（计数）
 * - 区间查询 query(i)： 查询序列 [1⋯i] 区间的区间和，即 i 位置的前缀和
 * 修改和查询的时间代价都是 O(logn)，其中 n 为需要维护前缀和的序列的长度。
 *
 * 思路与算法
 * 记题目给定的序列为 a，我们规定 a[i] 的取值集合为 a 的「值域」。我们用桶来表示
 * 值域中的每一个数，桶中记录这些数字出现的次数。假设 a = {5,5,2,3,6}，那么遍历
 * 这个序列得到的桶是这样的：
 *     index -> 1 2 3 4 5 6 7 8 9
 *     value -> 0 1 1 0 2 1 0 0 0
 *
 * 转化为动态维护前缀和问题
 * 记 value 序列为 v，我们可以看出它第 i−1 位的前缀和表示「有多少个数比 i 小」。
 * 那么我们可以从后往前遍历序列 a，记当前遍历到的元素为 a[i]，我们把 a[i] 对应
 * 的桶的值自增 1，记 a[i] = p，把 v 序列 p−1 位置的前缀和加入到答案中算贡献。
 * 为什么这么做是对的呢，因为我们在循环的过程中，我们把原序列分成了两部分，后半
 * 部分已经遍历过（已入桶），前半部分是待遍历的（未入桶），那么我们求到的 p−1
 * 位置的前缀和就是「已入桶」的元素中比 p 小的元素的个数总和。这种动态维护前缀和
 * 的问题我们可以用「树状数组」来解决。
 *
 * 用离散化优化空间
 * 我们显然可以用数组来实现这个桶，可问题是如果 a[i] 中有很大的元素，比如 10^9，
 * 我们就要开一个大小为 10^9 的桶，内存中是存不下的。这个桶数组中很多位置是 0，
 * 有效位置是稀疏的，我们要想一个办法让有效的位置全聚集到一起，减少无效位置的出现，
 * 这个时候我们就需要用到一个方法——离散化。离散化的方法有很多，但是目的是一样的，
 * 即把原序列的值域映射到一个连续的整数区间，并保证它们的偏序关系不变。这里我们
 * 将原数组去重后排序，原数组每个数映射到去重排序后这个数对应位置的下标，我们称
 * 这个下标为这个对应数字的 id。已知数字获取 id 可以在去重排序后的数组里面做
 * 二分查找，已知 id 获取数字可以直接把 id 作为下标访问去重排序数组的对应位置。
 */
// @lc code=start
func countSmaller(nums []int) []int {
	if nums == nil {
		return nil
	}
	n := len(nums)
	if n == 0 {
		return []int{}
	}

	a := discretization(nums)
	v := make([]int, len(a)+1)

	res := make([]int, 0, n)
	for i := n - 1; i >= 0; i-- {
		id := getID(a, nums[i])
		res = append(res, prefixSum(v, id-1))
		update(&v, id, 1)
	}

	// reverse
	for i, j := 0, n-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}

	return res
}

func discretization(nums []int) []int {
	set := map[int]bool{}
	for _, num := range nums {
		set[num] = true
	}
	a := make([]int, 0, len(set))
	for num := range set {
		a = append(a, num)
	}
	sort.Ints(a)
	return a
}

func getID(a []int, x int) int {
	return sort.SearchInts(a, x) + 1
}

func lowbit(x int) int {
	return x & (-x) // 2^k
}

func prefixSum(bit []int, k int) int {
	ans := 0
	for i := k; i > 0; i -= lowbit(i) {
		ans += bit[i]
	}
	return ans
}

func update(bit *[]int, i int, delta int) {
	for j := i; j < len(*bit); j += lowbit(j) {
		(*bit)[j] += delta
	}
}

// @lc code=end

// 暴破
// func countSmaller(nums []int) []int {
// 	if nums == nil {
// 		return nil
// 	}
// 	n := len(nums)
// 	if n == 0 {
// 		return []int{}
// 	}

// 	res := make([]int, n)
// 	for i := 0; i < n-1; i++ {
// 		cnt := 0
// 		for j := i + 1; j < n; j++ {
// 			if nums[j] < nums[i] {
// 				cnt++
// 			}
// 		}
// 		res[i] = cnt
// 	}
// 	return res
// }
