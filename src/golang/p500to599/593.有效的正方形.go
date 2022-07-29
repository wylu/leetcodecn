package p500to599

import "sort"

/*
 * @lc app=leetcode.cn id=593 lang=golang
 *
 * [593] 有效的正方形
 *
 * https://leetcode.cn/problems/valid-square/description/
 *
 * algorithms
 * Medium (46.22%)
 * Likes:    115
 * Dislikes: 0
 * Total Accepted:    15.4K
 * Total Submissions: 33.4K
 * Testcase Example:  '[0,0]\n[1,1]\n[1,0]\n[0,1]'
 *
 * 给定2D空间中四个点的坐标 p1, p2, p3 和 p4，如果这四个点构成一个正方形，则返回 true 。
 *
 * 点的坐标 pi 表示为 [xi, yi] 。输入 不是 按任何顺序给出的。
 *
 * 一个 有效的正方形 有四条等边和四个等角(90度角)。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
 * 输出: True
 *
 *
 * 示例 2:
 *
 *
 * 输入：p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
 * 输出：false
 *
 *
 * 示例 3:
 *
 *
 * 输入：p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
 * 输出：true
 *
 *
 *
 *
 * 提示:
 *
 *
 * p1.length == p2.length == p3.length == p4.length == 2
 * -10^4 <= xi, yi <= 10^4
 *
 *
 */

/**
 * @File    :   593.有效的正方形.go
 * @Time    :   2022/07/29 09:42:16
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func validSquare(p1 []int, p2 []int, p3 []int, p4 []int) bool {
	dist := func(x, y []int) int {
		return (x[0]-y[0])*(x[0]-y[0]) + (x[1]-y[1])*(x[1]-y[1])
	}

	if p1[0] == p2[0] && p1[1] == p2[1] {
		return false
	}
	edges := []int{
		dist(p1, p2), dist(p1, p3), dist(p1, p4),
		dist(p2, p3), dist(p2, p4), dist(p3, p4),
	}
	sort.Ints(edges)
	return edges[0] == edges[1] && edges[0] == edges[2] &&
		edges[0] == edges[3] && edges[4] == edges[5]
}

// @lc code=end
