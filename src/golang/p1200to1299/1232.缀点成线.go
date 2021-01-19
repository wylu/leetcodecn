package p1200to1299

/*
 * @lc app=leetcode.cn id=1232 lang=golang
 *
 * [1232] 缀点成线
 *
 * https://leetcode-cn.com/problems/check-if-it-is-a-straight-line/description/
 *
 * algorithms
 * Easy (47.04%)
 * Likes:    78
 * Dislikes: 0
 * Total Accepted:    29.6K
 * Total Submissions: 63K
 * Testcase Example:  '[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]'
 *
 * 在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y]
 * 表示横坐标为 x、纵坐标为 y 的点。
 *
 * 请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 *
 * 输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= coordinates.length <= 1000
 * coordinates[i].length == 2
 * -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
 * coordinates 中不含重复的点
 *
 *
 */

/**
 * @File    :   1232.缀点成线.go
 * @Time    :   2021/01/19 18:54:36
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func checkStraightLine(coordinates [][]int) bool {
	dx, dy := coordinates[0][0], coordinates[0][1]
	A, B := coordinates[1][1]-dy, -(coordinates[1][0] - dx)
	n := len(coordinates)
	for i := 2; i < n; i++ {
		x, y := coordinates[i][0]-dx, coordinates[i][1]-dy
		if A*x+B*y != 0 {
			return false
		}
	}
	return true
}

// @lc code=end
