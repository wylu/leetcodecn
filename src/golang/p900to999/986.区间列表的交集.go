package p900to999

/*
 * @lc app=leetcode.cn id=986 lang=golang
 *
 * [986] 区间列表的交集
 *
 * https://leetcode-cn.com/problems/interval-list-intersections/description/
 *
 * algorithms
 * Medium (65.37%)
 * Likes:    95
 * Dislikes: 0
 * Total Accepted:    10.2K
 * Total Submissions: 15.5K
 * Testcase Example:  '[[0,2],[5,10],[13,23],[24,25]]\n[[1,5],[8,12],[15,24],[25,26]]'
 *
 * 给定两个由一些 闭区间 组成的列表，每个区间列表都是成对不相交的，并且已经排序。
 *
 * 返回这两个区间列表的交集。
 *
 * （形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <=
 * b。两个闭区间的交集是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。）
 *
 *
 *
 * 示例：
 *
 *
 *
 * 输入：A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
 * 输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= A.length < 1000
 * 0 <= B.length < 1000
 * 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
 *
 *
 */

/**
 * @File    :   986.区间列表的交集.go
 * @Time    :   2020/10/16 14:12:01
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func intervalIntersection(a [][]int, b [][]int) [][]int {
	ans := [][]int{}
	i, j, na, nb := 0, 0, len(a), len(b)

	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	for i < na && j < nb {
		lo, hi := max(a[i][0], b[j][0]), min(a[i][1], b[j][1])
		if lo <= hi {
			ans = append(ans, []int{lo, hi})
		}

		if a[i][1] < b[j][1] {
			i++
		} else {
			j++
		}
	}

	return ans
}

// @lc code=end
