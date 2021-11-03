package p400to499

import "container/heap"

/*
 * @lc app=leetcode.cn id=407 lang=golang
 *
 * [407] 接雨水 II
 *
 * https://leetcode-cn.com/problems/trapping-rain-water-ii/description/
 *
 * algorithms
 * Hard (55.25%)
 * Likes:    496
 * Dislikes: 0
 * Total Accepted:    19K
 * Total Submissions: 34.3K
 * Testcase Example:  '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]'
 *
 * 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。
 *
 *
 *
 * 示例 1:
 *
 *
 *
 *
 * 输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
 * 输出: 4
 * 解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。
 *
 *
 * 示例 2:
 *
 *
 *
 *
 * 输入: heightMap =
 * [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
 * 输出: 10
 *
 *
 *
 *
 * 提示:
 *
 *
 * m == heightMap.length
 * n == heightMap[i].length
 * 1 <= m, n <= 200
 * 0 <= heightMap[i][j] <= 2 * 10^4
 *
 *
 *
 *
 */

/**
 * @File    :   407.接雨水-ii.go
 * @Time    :   2021/11/03 20:33:30
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：最小堆
 * 思路与算法
 *
 * 本题为经典题目，解题的原理和方法都可以参考「42.接雨水」，本题主要从一维数组
 * 变成了二维数组。首先我们思考一下什么样的方块一定可以接住水：
 *
 * - 该方块不为最外层的方块；
 * - 该方块自身的高度比其上下左右四个相邻的方块接水后的高度都要低；
 *
 * 我们假设方块的索引为 (i,j)，方块的高度为 heightMap[i][j]，方块接水后的高度
 * 为 water[i][j]。则我们知道方块 (i,j) 的接水后的高度为：
 *
 * water[i][j] = max(
 * 	heightMap[i][j],
 * 	min(water[i−1][j], water[i+1][j], water[i][j−1], water[i][j+1])
 * )
 *
 * 我们知道方块 (i,j) 实际接水的容量计算公式为 water[i][j] - heightMap[i][j]。
 * 首先我们可以确定的是，矩阵的最外层的方块接水后的高度就是方块的自身高度，因为
 * 最外层的方块无法接水，因此最外层的方块 water[i][j] = heightMap[i][j]。
 *
 * 根据木桶原理，接到的雨水的高度由这个容器周围最短的木板来确定的。我们可以知道
 * 容器内水的高度取决于最外层高度最低的方块，如图 1 所示：
 *
 * https://assets.leetcode-cn.com/solution-static/407/407_1.PNG
 *
 * 我们假设已经知道最外层的方块接水后的高度的最小值，则此时我们根据木桶原理，
 * 肯定可以确定最小高度方块的相邻方块的接水高度。我们同时更新最外层的方块标记，
 * 我们在新的最外层的方块再次找到接水后的高度的最小值，同时确定与其相邻的方块
 * 的接水高度，如图 2 所示:
 *
 * https://assets.leetcode-cn.com/solution-static/407/407_2.PNG
 *
 * 然后再次更新最外层，依次迭代直到求出所有的方块的接水高度，即可知道矩阵中
 * 的接水容量。
 */

// @lc code=start

type cell struct{ h, x, y int }
type hp []cell

func (h hp) Len() int            { return len(h) }
func (h hp) Less(i, j int) bool  { return h[i].h < h[j].h }
func (h hp) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v interface{}) { *h = append(*h, v.(cell)) }
func (h *hp) Pop() interface{}   { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }

func trapRainWater(heightMap [][]int) int {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	m, n := len(heightMap), len(heightMap[0])
	if m <= 2 || n <= 2 {
		return 0
	}

	seen := make([][]bool, m)
	for i := 0; i < m; i++ {
		seen[i] = make([]bool, n)
	}

	h := &hp{}
	for i, row := range heightMap {
		for j, v := range row {
			if i == 0 || i == m-1 || j == 0 || j == n-1 {
				heap.Push(h, cell{v, i, j})
				seen[i][j] = true
			}
		}
	}

	ans := 0
	d := []int{-1, 0, 1, 0, -1}
	for h.Len() > 0 {
		cur := heap.Pop(h).(cell)
		for k := 0; k < 4; k++ {
			nx, ny := cur.x+d[k], cur.y+d[k+1]
			if 0 <= nx && nx < m && 0 <= ny && ny < n && !seen[nx][ny] {
				if heightMap[nx][ny] < cur.h {
					ans += cur.h - heightMap[nx][ny]
				}
				seen[nx][ny] = true
				heap.Push(h, cell{max(heightMap[nx][ny], cur.h), nx, ny})
			}
		}
	}

	return ans
}

// @lc code=end
