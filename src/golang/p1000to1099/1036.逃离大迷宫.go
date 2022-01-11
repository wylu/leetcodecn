package p1000to1099

import "sort"

/*
 * @lc app=leetcode.cn id=1036 lang=golang
 *
 * [1036] 逃离大迷宫
 *
 * https://leetcode-cn.com/problems/escape-a-large-maze/description/
 *
 * algorithms
 * Hard (44.76%)
 * Likes:    142
 * Dislikes: 0
 * Total Accepted:    13.9K
 * Total Submissions: 31.2K
 * Testcase Example:  '[[0,1],[1,0]]\n[0,0]\n[0,2]'
 *
 * 在一个 10^6 x 10^6 的网格中，每个网格上方格的坐标为 (x, y) 。
 *
 * 现在从源方格 source = [sx, sy] 开始出发，意图赶往目标方格 target = [tx, ty] 。数组 blocked
 * 是封锁的方格列表，其中每个 blocked[i] = [xi, yi] 表示坐标为 (xi, yi) 的方格是禁止通行的。
 *
 * 每次移动，都可以走到网格中在四个方向上相邻的方格，只要该方格 不 在给出的封锁列表 blocked 上。同时，不允许走出网格。
 *
 * 只有在可以通过一系列的移动从源方格 source 到达目标方格 target 时才返回 true。否则，返回 false。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
 * 输出：false
 * 解释：
 * 从源方格无法到达目标方格，因为我们无法在网格中移动。
 * 无法向北或者向东移动是因为方格禁止通行。
 * 无法向南或者向西移动是因为不能走出网格。
 *
 * 示例 2：
 *
 *
 * 输入：blocked = [], source = [0,0], target = [999999,999999]
 * 输出：true
 * 解释：
 * 因为没有方格被封锁，所以一定可以到达目标方格。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= blocked.length <= 200
 * blocked[i].length == 2
 * 0 <= xi, yi < 10^6
 * source.length == target.length == 2
 * 0 <= sx, sy, tx, ty < 10^6
 * source != target
 * 题目数据保证 source 和 target 不在封锁列表内
 *
 *
 */

/**
 * @File    :   1036.逃离大迷宫.go
 * @Time    :   2022/01/11 21:28:37
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法二：离散化 + 广度优先搜索
 * 思路与算法
 *
 * 我们也可以借助离散化技巧将网格「压缩」成一个规模较小的但等价的新网格，并在
 * 新网格上进行常规的广度优先搜索。
 *
 * 以网格的每一行为例，可以发现，不同的行坐标只有：
 *   - 障碍所在的行，最多有 n 个；
 *   - source 和 target 所在的行，最多有 2 个。
 *   - 网格的上下边界（即 -1 和 10^6），有 2 个。
 *
 * 因此不同的行坐标最多只有 n+4 个，我们可以对行坐标进行离散化，具体的规则如下：
 *   - 我们将行坐标进行升序排序；
 *   - 将上边界离散化为 -1。上边界是排序后的第 0 个行坐标；
 *   - 如果排序后的第 i 个行坐标与第 i-1 个行坐标相同，那么它们离散化之后的值也相同；
 *   - 如果排序后的第 i 个行坐标与第 i-1 个行坐标相差 1，那么它们离散化之后的值也相差 1；
 *   - 如果排序后的第 i 个行坐标与第 i-1 个行坐标相差超过 1，那么它们离散化之后的值相差 2。
 *
 * 这样的正确性在于：在离散化前，如果两个行坐标本身相邻，那么在离散化之后它们
 * 也必须相邻。如果它们不相邻，可以把它们之间间隔的若干行直接「压缩」成一行，
 * 即行坐标相差 2。
 *
 * 对于列坐标的离散化方法也是如此。在离散化完成之后，新的网格的规模不会超过
 * 2(n+4) * 2(n+4)，进行广度优先搜索需要的时间是可接受的。
 */

// @lc code=start
func isEscapePossible(blocked [][]int, source []int, target []int) bool {
	// 离散化 a，返回的哈希表中的键值对分别为 a 中的原始值及其离散化后的对应值
	discrete := func(a []int) (map[int]int, int) {
		sort.Ints(a)

		id := 0
		if a[0] > 0 {
			id = 1
		}

		mapping := map[int]int{a[0]: id}
		pre := a[0]
		for _, v := range a[1:] {
			if v != pre {
				if v == pre+1 {
					id++
				} else {
					id += 2
				}
				mapping[v] = id
				pre = v
			}
		}

		const boundary int = 1e6
		if a[len(a)-1] != boundary-1 {
			id++
		}

		return mapping, id
	}

	n := len(blocked)
	if n < 2 {
		return true
	}

	d := []int{0, 1, 0, -1, 0}
	rows := []int{source[0], target[0]}
	cols := []int{source[1], target[1]}
	for _, b := range blocked {
		rows = append(rows, b[0])
		cols = append(cols, b[1])
	}

	// 离散化行列坐标
	rMapping, rBound := discrete(rows)
	cMapping, cBound := discrete(cols)

	grid := make([][]bool, rBound+1)
	for i := range grid {
		grid[i] = make([]bool, cBound+1)
	}
	for _, b := range blocked {
		grid[rMapping[b[0]]][cMapping[b[1]]] = true
	}

	type pair struct{ x, y int }
	sx, sy := rMapping[source[0]], cMapping[source[1]]
	tx, ty := rMapping[target[0]], cMapping[target[1]]
	grid[sx][sy] = true
	q := []pair{{sx, sy}}
	for len(q) > 0 {
		p := q[0]
		q = q[1:]
		for i := 0; i < 4; i++ {
			x, y := p.x+d[i], p.y+d[i+1]
			if x < 0 || x > rBound || y < 0 || y > cBound || grid[x][y] {
				continue
			}

			if x == tx && y == ty {
				return true
			}
			grid[x][y] = true
			q = append(q, pair{x, y})
		}
	}

	return false
}

// @lc code=end
