package p800to899

import "sort"

/*
 * @lc app=leetcode.cn id=850 lang=golang
 *
 * [850] 矩形面积 II
 *
 * https://leetcode.cn/problems/rectangle-area-ii/description/
 *
 * algorithms
 * Hard (48.58%)
 * Likes:    206
 * Dislikes: 0
 * Total Accepted:    12.5K
 * Total Submissions: 20.6K
 * Testcase Example:  '[[0,0,2,2],[1,0,2,3],[1,0,3,1]]'
 *
 * 我们给出了一个（轴对齐的）二维矩形列表 rectangles 。 对于 rectangle[i] = [x1, y1, x2,
 * y2]，其中（x1，y1）是矩形 i 左下角的坐标， (xi1, yi1) 是该矩形 左下角 的坐标， (xi2, yi2) 是该矩形 右上角
 * 的坐标。
 *
 * 计算平面中所有 rectangles 所覆盖的 总面积 。任何被两个或多个矩形覆盖的区域应只计算 一次 。
 *
 * 返回 总面积 。因为答案可能太大，返回 10^9 + 7 的 模 。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
 * 输出：6
 * 解释：如图所示，三个矩形覆盖了总面积为6的区域。
 * 从(1,1)到(2,2)，绿色矩形和红色矩形重叠。
 * 从(1,0)到(2,3)，三个矩形都重叠。
 *
 *
 * 示例 2：
 *
 *
 * 输入：rectangles = [[0,0,1000000000,1000000000]]
 * 输出：49
 * 解释：答案是 10^18 对 (10^9 + 7) 取模的结果， 即 49 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= rectangles.length <= 200
 * rectanges[i].length = 4
 * 0 <= xi1, yi1, xi2, yi2 <= 10^9
 * 矩形叠加覆盖后的总面积不会超越 2^63 - 1 ，这意味着可以用一个 64 位有符号整数来保存面积结果。
 *
 *
 */

/**
 * @File    :   850.矩形面积-ii.go
 * @Time    :   2022/09/16 20:51:09
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func rectangleArea(rectangles [][]int) int {
	n := len(rectangles) * 2
	hBound := make([]int, 0, n)
	for _, r := range rectangles {
		hBound = append(hBound, r[1], r[3])
	}
	// 排序，方便下面去重
	sort.Ints(hBound)
	m := 0
	for _, b := range hBound[1:] {
		if hBound[m] != b {
			m++
			hBound[m] = b
		}
	}
	hBound = hBound[:m+1]

	type tuple struct{ x, i, d int }
	sweep := make([]tuple, 0, n)
	for i, r := range rectangles {
		sweep = append(sweep, tuple{r[0], i, 1}, tuple{r[2], i, -1})
	}
	sort.Slice(sweep, func(i, j int) bool { return sweep[i].x < sweep[j].x })

	ans := 0
	seg := make([]int, m)
	for i := 0; i < n; i++ {
		j := i
		for j+1 < n && sweep[j+1].x == sweep[i].x {
			j++
		}
		if j+1 == n {
			break
		}
		// 一次性地处理掉一批横坐标相同的左右边界
		for k := i; k <= j; k++ {
			idx, diff := sweep[k].i, sweep[k].d
			left, right := rectangles[idx][1], rectangles[idx][3]
			for x := 0; x < m; x++ {
				if left <= hBound[x] && hBound[x+1] <= right {
					seg[x] += diff
				}
			}
		}
		cover := 0
		for k := 0; k < m; k++ {
			if seg[k] > 0 {
				cover += hBound[k+1] - hBound[k]
			}
		}
		ans += cover * (sweep[j+1].x - sweep[j].x)
		i = j
	}

	return ans % (1e9 + 7)
}

// @lc code=end
