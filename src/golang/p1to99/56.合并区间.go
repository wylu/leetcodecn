package p1to99

import "sort"

/*
 * @lc app=leetcode.cn id=56 lang=golang
 *
 * [56] 合并区间
 *
 * https://leetcode-cn.com/problems/merge-intervals/description/
 *
 * algorithms
 * Medium (43.10%)
 * Likes:    626
 * Dislikes: 0
 * Total Accepted:    148.1K
 * Total Submissions: 343.5K
 * Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
 *
 * 给出一个区间的集合，请合并所有重叠的区间。
 *
 *
 *
 * 示例 1:
 *
 * 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
 * 输出: [[1,6],[8,10],[15,18]]
 * 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
 *
 *
 * 示例 2:
 *
 * 输入: intervals = [[1,4],[4,5]]
 * 输出: [[1,5]]
 * 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
 *
 * 注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。
 *
 *
 *
 * 提示：
 *
 *
 * intervals[i][0] <= intervals[i][1]
 *
 *
 */

/**
 * @File    :   56.合并区间.go
 * @Time    :   2020/09/26 23:27:29
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：排序
 *
 * 思路
 *
 * 如果我们按照区间的左端点排序，那么在排完序的列表中，可以合并的区间一定是连续的。
 *
 * 算法
 *
 * 我们用数组 merged 存储最终的答案。
 *
 * 首先，我们将列表中的区间按照左端点升序排序。然后我们将第一个区间加入 merged
 * 数组中，并按顺序依次考虑之后的每个区间：
 *
 * 如果当前区间的左端点在数组 merged 中最后一个区间的右端点之后，那么它们不会
 * 重合，我们可以直接将这个区间加入数组 merged 的末尾；
 *
 * 否则，它们重合，我们需要用当前区间的右端点更新数组 merged 中最后一个区间的
 * 右端点，将其置为二者的较大值。
 */

// @lc code=start
func merge(intervals [][]int) [][]int {
	ans := [][]int{}
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] <= intervals[j][0]
	})

	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	for _, interval := range intervals {
		n := len(ans)
		if n == 0 || interval[0] > ans[n-1][1] {
			ans = append(ans, interval)
		} else {
			ans[n-1][1] = max(ans[n-1][1], interval[1])
		}
	}

	return ans
}

// @lc code=end
