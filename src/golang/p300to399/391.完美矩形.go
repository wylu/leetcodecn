package p300to399

import (
	"sort"
)

/*
 * @lc app=leetcode.cn id=391 lang=golang
 *
 * [391] 完美矩形
 *
 * https://leetcode-cn.com/problems/perfect-rectangle/description/
 *
 * algorithms
 * Hard (46.39%)
 * Likes:    194
 * Dislikes: 0
 * Total Accepted:    18.2K
 * Total Submissions: 39.2K
 * Testcase Example:  '[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]'
 *
 * 给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi]
 * 表示一个坐标轴平行的矩形。这个矩形的左下顶点是 (xi, yi) ，右上顶点是 (ai, bi) 。
 *
 * 如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 。
 *
 *
 * 示例 1：
 *
 *
 * 输入：rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
 * 输出：true
 * 解释：5 个矩形一起可以精确地覆盖一个矩形区域。
 *
 *
 * 示例 2：
 *
 *
 * 输入：rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
 * 输出：false
 * 解释：两个矩形之间有间隔，无法覆盖成一个矩形。
 *
 * 示例 3：
 *
 *
 * 输入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[3,2,4,4]]
 * 输出：false
 * 解释：图形顶端留有空缺，无法覆盖成一个矩形。
 *
 * 示例 4：
 *
 *
 * 输入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
 * 输出：false
 * 解释：因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= rectangles.length <= 2 * 10^4
 * rectangles[i].length == 4
 * -10^5 <= xi, yi, ai, bi <= 10^5
 *
 *
 */

/**
 * @File    :   391.完美矩形.go
 * @Time    :   2021/11/16 22:46:53
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 扫描线
 * 将每个矩形 rectangles[i] 看做两条竖直方向的边，使用 (x, y1, y2) 的形式
 * 进行存储（其中 y1 代表该竖边的下端点，y2 代表竖边的上端点），同时为了区分
 * 是矩形的左边还是右边，再引入一个标识位，即以四元组 (x, y1, y2, flag)
 * 的形式进行存储。
 *
 * 一个完美矩形的充要条件为：对于完美矩形的每一条非边缘的竖边，都「成对」出现
 * （存在两条完全相同的左边和右边重叠在一起）；对于完美矩形的两条边缘竖边，
 * 均独立为一条连续的（不重叠）的竖边。
 *
 * 如图（红色框的为「完美矩形的边缘竖边」，绿框的为「完美矩形的非边缘竖边」）：
 *
 * https://pic.leetcode-cn.com/1637019249-QYzZTM-image.png
 *
 * - 绿色：非边缘竖边必然有成对的左右两条完全相同的竖边重叠在一起；
 * - 红色：边缘竖边由于只有单边，必然不重叠，且连接成一条完成的竖边。
 *
 *
 *                ^
 *                |
 *              6 +
 *                |
 *              5 +   +---+---------------+
 *                |   |   |               |
 *              4 +   +---+               |
 *                |   |   |               |
 *              3 +   +---+-----------+---+
 *                |   |               |   |
 *              2 +   +---+-----------+---+
 *                |   |   |               |
 *              1 +   +---+---------------+
 *                |
 *         ---+---+---+---+---+---+---+---+---+---+---->
 *                |   1   2   3   4   5   6
 *                +
 *                |
 */

// @lc code=start
func isRectangleCover(rectangles [][]int) bool {
	n := len(rectangles)
	// 扫描线数组，四元组：[横坐标，纵坐标起点，纵坐标终点，左线段还是右线段]
	rs := make([][4]int, n*2)
	for i, k := 0, 0; i < n; i++ {
		rect := rectangles[i]
		// 加入四元组，1 表示左线段，-1 表示右线段
		rs[k] = [4]int{rect[0], rect[1], rect[3], 1}
		k++
		rs[k] = [4]int{rect[2], rect[1], rect[3], -1}
		k++
	}

	sort.Slice(rs, func(i, j int) bool {
		if rs[i][0] == rs[j][0] {
			return rs[i][1] < rs[j][1]
		}
		return rs[i][0] < rs[j][0]
	})

	// fmt.Println(rs)

	n *= 2
	// 分别存储相同的横坐标下「左边的线段」和「右边的线段」
	le, re := [][2]int{}, [][2]int{}
	for lt := 0; lt < n; {
		rt := lt
		le, re = le[0:0], re[0:0]

		// 找到横坐标相同部分
		for rt < n && rs[rt][0] == rs[lt][0] {
			rt++
		}

		for i := lt; i < rt; i++ {
			// 得到当前横坐标上的线段，二元组 [纵坐标起始位置，纵坐标终止位置]
			cur := [2]int{rs[i][1], rs[i][2]}
			// es 指向左线段或者右线段集合
			var es *[][2]int
			if rs[i][3] == 1 {
				es = &le
			} else {
				es = &re
			}

			if len(*es) == 0 {
				*es = append(*es, cur)
			} else {
				// 如果能进来这个 else，说明在当前横坐标上有多条“左边”或“右边”，
				// 将当前边和上一次的边取出对比。
				pre := &(*es)[len(*es)-1]
				if cur[0] < (*pre)[1] { // 存在重叠
					return false
				} else if cur[0] == (*pre)[1] { // 首尾相连
					(*pre)[1] = cur[1]
				} else {
					*es = append(*es, cur)
				}
			}
		}

		if lt > 0 && rt < n {
			// 若不是完美矩形的边缘竖边，检查是否成对出现
			if len(le) != len(re) {
				return false
			}
			for i := 0; i < len(le); i++ {
				if le[i][0] != re[i][0] || le[i][1] != re[i][1] {
					return false
				}
			}
		} else {
			// 若是完美矩形的边缘竖边，检查是否形成完整一段
			if len(le)+len(re) != 1 {
				return false
			}
		}

		lt = rt
	}

	return true
}

// @lc code=end
