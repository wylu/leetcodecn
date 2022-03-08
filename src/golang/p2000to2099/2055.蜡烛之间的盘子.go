package p2000to2099

/*
 * @lc app=leetcode.cn id=2055 lang=golang
 *
 * [2055] 蜡烛之间的盘子
 *
 * https://leetcode-cn.com/problems/plates-between-candles/description/
 *
 * algorithms
 * Medium (42.29%)
 * Likes:    93
 * Dislikes: 0
 * Total Accepted:    18.2K
 * Total Submissions: 42.9K
 * Testcase Example:  '"**|**|***|"\n[[2,5],[5,9]]'
 *
 * 给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0 开始的字符串 s ，它只包含字符 '*' 和 '|' ，其中 '*' 表示一个 盘子
 * ，'|' 表示一支 蜡烛 。
 *
 * 同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] 表示 子字符串
 * s[lefti...righti] （包含左右端点的字符）。对于每个查询，你需要找到 子字符串中 在 两支蜡烛之间 的盘子的 数目 。如果一个盘子在
 * 子字符串中 左边和右边 都 至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间 。
 *
 *
 * 比方说，s = "||**||**|*" ，查询 [3, 8] ，表示的是子字符串 "*||**|" 。子字符串中在两支蜡烛之间的盘子数目为 2
 * ，子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
 *
 *
 * 请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。
 *
 *
 *
 * 示例 1:
 *
 *
 *
 * 输入：s = "**|**|***|", queries = [[2,5],[5,9]]
 * 输出：[2,3]
 * 解释：
 * - queries[0] 有两个盘子在蜡烛之间。
 * - queries[1] 有三个盘子在蜡烛之间。
 *
 *
 * 示例 2:
 *
 *
 *
 * 输入：s = "***|**|*****|**||**|*", queries =
 * [[1,17],[4,5],[14,17],[5,11],[15,16]]
 * 输出：[9,0,0,0,0]
 * 解释：
 * - queries[0] 有 9 个盘子在蜡烛之间。
 * - 另一个查询没有盘子在蜡烛之间。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 3 <= s.length <= 10^5
 * s 只包含字符 '*' 和 '|' 。
 * 1 <= queries.length <= 10^5
 * queries[i].length == 2
 * 0 <= lefti <= righti < s.length
 *
 *
 */

/**
 * @File    :   2055.蜡烛之间的盘子.go
 * @Time    :   2022/03/08 16:30:28
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：预处理 + 前缀和
 * 思路和算法
 *
 * 对于每一个询问，我们只需要找到给定区间内最左侧和最右侧的两个蜡烛，这样两个蜡烛
 * 之间的所有盘子都是符合条件的。
 *
 * 对于寻找蜡烛，我们可以预处理区间内每个位置左侧的第一个蜡烛和右侧的第一个蜡烛。
 * 这样区间左端点 left[i] 右侧的第一个蜡烛即为区间最左侧的蜡烛，区间右端点 right[i]
 * 左侧的第一个蜡烛即为区间最右侧的蜡烛。
 *
 * 对于计算盘子数量，我们可以计算盘子数量的前缀和 preSum。假设找到的两蜡烛的位置
 * 分别为 x 和 y，那么两位置之间的盘子数量即为 preSum[y] - preSum[x-1]。
 *
 * 这样我们就通过预处理，将寻找蜡烛和计算盘子数量两个操作的时间复杂度降至 O(1)，
 * 因此对于每个询问，时间复杂度为 O(1)。
 *
 * 在实际代码中，可能某个位置的左侧或右侧是不存在蜡烛的，此时我们将对应数组的值
 * 记为 -1。当 x 为 -1 或者 y 为 -1 或者 x >= y 时，不存在满足条件的盘子。同时
 * 注意到因为 x 位置是蜡烛，所以盘子数量也可以表示为 preSum[y] - preSum[x]，
 * 这个写法可以防止 x 为 0 时数组越界。
 */

// @lc code=start
func platesBetweenCandles(s string, queries [][]int) []int {
	n := len(s)
	ps := make([]int, n+1)
	lts, rts := make([]int, n), make([]int, n)
	tot, cur := 0, -1
	for i, ch := range s {
		if ch == '*' {
			tot++
		} else {
			cur = i
		}
		ps[i+1] = tot
		lts[i] = cur
	}

	for i, cur := n-1, -1; i >= 0; i-- {
		if s[i] == '|' {
			cur = i
		}
		rts[i] = cur
	}

	ans := make([]int, len(queries))
	for i, q := range queries {
		x, y := rts[q[0]], lts[q[1]]
		if x >= 0 && y >= 0 && x < y {
			ans[i] = ps[y+1] - ps[x]
		}
	}

	return ans
}

// @lc code=end

// func platesBetweenCandles(s string, queries [][]int) []int {
// 	n := len(s)
// 	cnt := make([]int, n+1)
// 	pos := []int{}
// 	for i, ch := range s {
// 		if ch == '|' {
// 			cnt[i+1] = 1
// 			pos = append(pos, i)
// 		}
// 		cnt[i+1] += cnt[i]
// 	}

// 	search := func(arr []int, x int) int {
// 		left, right := 0, len(arr)
// 		for left < right {
// 			mid := (left + right) / 2
// 			if arr[mid] < x {
// 				left = mid + 1
// 			} else {
// 				right = mid
// 			}
// 		}
// 		return left
// 	}

// 	ans := []int{}
// 	for _, query := range queries {
// 		lt, rt := query[0], query[1]
// 		if rt-lt <= 1 {
// 			ans = append(ans, 0)
// 			continue
// 		}

// 		p := search(pos, lt)
// 		if p == len(pos) || pos[p] >= rt-1 {
// 			ans = append(ans, 0)
// 			continue
// 		}

// 		q := search(pos, rt)
// 		if q == len(pos) || pos[q] != rt {
// 			if q == 0 || pos[q-1] <= p+1 {
// 				ans = append(ans, 0)
// 				continue
// 			}
// 			q--
// 		}

// 		x, y := pos[p], pos[q]
// 		ans = append(ans, (y-x+1)-(cnt[y+1]-cnt[x]))
// 	}

// 	return ans
// }
