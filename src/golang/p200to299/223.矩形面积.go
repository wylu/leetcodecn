package p200to299

/*
 * @lc app=leetcode.cn id=223 lang=golang
 *
 * [223] 矩形面积
 *
 * https://leetcode-cn.com/problems/rectangle-area/description/
 *
 * algorithms
 * Medium (46.40%)
 * Likes:    136
 * Dislikes: 0
 * Total Accepted:    26.7K
 * Total Submissions: 54K
 * Testcase Example:  '-3\n0\n3\n4\n0\n-1\n9\n2'
 *
 * 给你 二维 平面上两个 由直线构成的 矩形，请你计算并返回两个矩形覆盖的总面积。
 *
 * 每个矩形由其 左下 顶点和 右上 顶点坐标表示：
 *
 *
 *
 * 第一个矩形由其左下顶点 (ax1, ay1) 和右上顶点 (ax2, ay2) 定义。
 * 第二个矩形由其左下顶点 (bx1, by1) 和右上顶点 (bx2, by2) 定义。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
 * 输出：45
 *
 *
 * 示例 2：
 *
 *
 * 输入：ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 =
 * 2
 * 输出：16
 *
 *
 *
 *
 * 提示：
 *
 *
 * -10^4 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 10^4
 *
 *
 */

/**
 * @File    :   223.矩形面积.go
 * @Time    :   2021/09/30 10:25:01
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：计算重叠面积
 * 两个矩形覆盖的总面积等于两个矩形的面积之和减去两个矩形的重叠部分的面积。
 * 由于两个矩形的左下顶点和右上顶点已知，因此两个矩形的面积可以直接计算。
 * 如果两个矩形重叠，则两个矩形的重叠部分也是矩形，重叠部分的面积可以根据
 * 重叠部分的边界计算。
 *
 * 两个矩形的水平边投影到 x 轴上的线段分别为 [ax1, ax2] 和 [bx1, bx2]，
 * 竖直边投影到 y 轴上的线段分别为 [ay1, ay2] 和 [by1, by2]。如果两个矩形
 * 重叠，则重叠部分的水平边投影到 x 轴上的线段为 [max(ax1, bx1), min(ax2, bx2)]，
 * 竖直边投影到 y 轴上的线段为 [max(ay1, by1), min(ay2, by2)]，根据重叠部分
 * 的水平边投影到 x 轴上的线段长度和竖直边投影到 y 轴上的线段长度即可计算
 * 重叠部分的面积。只有当两条线段的长度都大于 0 时，重叠部分的面积才大于 0，
 * 否则重叠部分的面积为 0。
 */

// @lc code=start
func computeArea(ax1 int, ay1 int, ax2 int, ay2 int, bx1 int, by1 int, bx2 int, by2 int) int {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	ans := (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)
	ex, ey := min(ax2, bx2)-max(ax1, bx1), min(ay2, by2)-max(ay1, by1)
	if ex > 0 && ey > 0 {
		ans -= ex * ey
	}

	return ans
}

// @lc code=end

// func computeArea(ax1 int, ay1 int, ax2 int, ay2 int, bx1 int, by1 int, bx2 int, by2 int) int {
// 	checkUp := func() bool { return by1 < ay2 && by2 >= ay2 && bx1 < ax2 && bx2 > ax1 }
// 	checkDown := func() bool { return by1 <= ay1 && by2 > ay1 && bx1 < ax2 && bx2 > ax1 }
// 	checkLeft := func() bool { return bx1 <= ax1 && bx2 > ax1 && by1 < ay2 && by2 > ay1 }
// 	checkRight := func() bool { return bx1 < ax2 && bx2 >= ax2 && by1 < ay2 && by2 > ay1 }
// 	max := func(x, y int) int {
// 		if x > y {
// 			return x
// 		}
// 		return y
// 	}
// 	min := func(x, y int) int {
// 		if x < y {
// 			return x
// 		}
// 		return y
// 	}

// 	ans := (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)

// 	if checkUp() {
// 		lt, rt := max(ax1, bx1), min(ax2, bx2)
// 		ans -= (rt - lt) * (ay2 - max(by1, ay1))
// 	} else if checkDown() {
// 		lt, rt := max(ax1, bx1), min(ax2, bx2)
// 		ans -= (rt - lt) * (by2 - ay1)
// 	} else if checkLeft() {
// 		ans -= (min(bx2, ax2) - ax1) * (by2 - by1)
// 	} else if checkRight() {
// 		ans -= (ax2 - bx1) * (by2 - by1)
// 	} else if !(by1 >= ay2 || by2 <= ay1 || bx2 <= ax1 || bx1 >= ax2) {
// 		ans -= min((ax2-ax1)*(ay2-ay1), (bx2-bx1)*(by2-by1))
// 	}

// 	return ans
// }
