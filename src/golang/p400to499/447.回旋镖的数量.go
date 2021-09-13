package p400to499

/*
 * @lc app=leetcode.cn id=447 lang=golang
 *
 * [447] 回旋镖的数量
 *
 * https://leetcode-cn.com/problems/number-of-boomerangs/description/
 *
 * algorithms
 * Medium (64.77%)
 * Likes:    190
 * Dislikes: 0
 * Total Accepted:    37.2K
 * Total Submissions: 57.4K
 * Testcase Example:  '[[0,0],[1,0],[2,0]]'
 *
 * 给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组
 * ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。
 *
 * 返回平面上所有回旋镖的数量。
 *
 *
 * 示例 1：
 *
 *
 * 输入：points = [[0,0],[1,0],[2,0]]
 * 输出：2
 * 解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：points = [[1,1],[2,2],[3,3]]
 * 输出：2
 *
 *
 * 示例 3：
 *
 *
 * 输入：points = [[1,1]]
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == points.length
 * 1 <= n <= 500
 * points[i].length == 2
 * -10^4 <= xi, yi <= 10^4
 * 所有点都 互不相同
 *
 *
 */

/**
 * @File    :   447.回旋镖的数量.go
 * @Time    :   2021/09/13 16:49:33
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func numberOfBoomerangs(points [][]int) int {
	getDistance := func(a, b int) int {
		x1, y1 := points[a][0], points[a][1]
		x2, y2 := points[b][0], points[b][1]
		return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
	}

	ans := 0
	n := len(points)
	for i := 0; i < n; i++ {
		dist := map[int]int{}
		for j := 0; j < n; j++ {
			dist[getDistance(i, j)]++
		}

		for _, cnt := range dist {
			ans += cnt * (cnt - 1)
		}
	}

	return ans
}

// @lc code=end

// func numberOfBoomerangs(points [][]int) int {
// 	getDistance := func(a, b int) int {
// 		x1, y1 := points[a][0], points[a][1]
// 		x2, y2 := points[b][0], points[b][1]
// 		return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
// 	}

// 	ans := 0
// 	n := len(points)
// 	dists := make([]int, n+1)
// 	dists[n] = math.MaxInt32

// 	for i := 0; i < n; i++ {
// 		for j := 0; j < n; j++ {
// 			dists[j] = getDistance(i, j)
// 		}

// 		sort.Ints(dists)
// 		for pre, cur := 0, 0; cur <= n; cur++ {
// 			if dists[cur] != dists[pre] {
// 				// 与点 i 距离相同的点的个数
// 				cnt := (cur - pre)
// 				if cnt >= 2 {
// 					// 组合 + 排列
// 					ans += cnt * (cnt - 1)
// 				}
// 				pre = cur
// 			}
// 		}
// 	}

// 	return ans
// }
