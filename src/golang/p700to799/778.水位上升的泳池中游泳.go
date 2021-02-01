package p700to799

/*
 * @lc app=leetcode.cn id=778 lang=golang
 *
 * [778] 水位上升的泳池中游泳
 *
 * https://leetcode-cn.com/problems/swim-in-rising-water/description/
 *
 * algorithms
 * Hard (60.75%)
 * Likes:    150
 * Dislikes: 0
 * Total Accepted:    18.7K
 * Total Submissions: 30.7K
 * Testcase Example:  '[[0,2],[1,3]]'
 *
 * 在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。
 *
 * 现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t
 * 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。
 *
 * 你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: [[0,2],[1,3]]
 * 输出: 3
 * 解释:
 * 时间为0时，你位于坐标方格的位置为 (0, 0)。
 * 此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。
 *
 * 等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3
 * 更高的，所以你可以游向坐标方格中的任意位置
 *
 *
 * 示例2:
 *
 *
 * 输入:
 * [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
 * 输出: 16
 * 解释:
 * ⁠0  1  2  3  4
 * 24 23 22 21  5
 * 12 13 14 15 16
 * 11 17 18 19 20
 * 10  9  8  7  6
 *
 * 最终的路线用加粗进行了标记。
 * 我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的
 *
 *
 *
 *
 * 提示:
 *
 *
 * 2 <= N <= 50.
 * grid[i][j] 是 [0, ..., N*N - 1] 的排列。
 *
 *
 */

/**
 * @File    :   778.水位上升的泳池中游泳.go
 * @Time    :   2021/02/01 09:08:58
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 参考 1631. 最小体力消耗路径
 */

// @lc code=start

// UnionFind ...
type UnionFind struct {
	par []int
}

// NewUnionFind ...
func NewUnionFind(n int) *UnionFind {
	uf := UnionFind{par: make([]int, n)}
	for i := 0; i < n; i++ {
		uf.par[i] = i
	}
	return &uf
}

// Find ...
func (uf *UnionFind) Find(x int) int {
	if uf.par[x] != x {
		uf.par[x] = uf.Find(uf.par[x])
	}
	return uf.par[x]
}

// Union ..
func (uf *UnionFind) Union(x, y int) {
	uf.par[uf.Find(x)] = uf.Find(y)
}

// Connected ...
func (uf *UnionFind) Connected(x, y int) bool {
	return uf.Find(x) == uf.Find(y)
}

func swimInWater(grid [][]int) int {
	n := len(grid)
	m := n * n
	pos := map[int][2]int{}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			pos[grid[i][j]] = [2]int{i, j}
		}
	}

	d := [5]int{0, 1, 0, -1, 0}
	uf := NewUnionFind(m)
	for t := 0; t < m; t++ {
		x, y := pos[t][0], pos[t][1]
		for i := 0; i < 4; i++ {
			u, v := x+d[i], y+d[i+1]
			if u >= 0 && u < n && v >= 0 && v < n && grid[u][v] <= t {
				uf.Union(x*n+y, u*n+v)
				if uf.Connected(0, m-1) {
					return t
				}
			}
		}
	}

	return -1
}

// @lc code=end
