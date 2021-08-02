package p700to799

import "math"

/*
 * @lc app=leetcode.cn id=743 lang=golang
 *
 * [743] 网络延迟时间
 *
 * https://leetcode-cn.com/problems/network-delay-time/description/
 *
 * algorithms
 * Medium (50.34%)
 * Likes:    378
 * Dislikes: 0
 * Total Accepted:    44.3K
 * Total Submissions: 87.9K
 * Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
 *
 * 有 n 个网络节点，标记为 1 到 n。
 *
 * 给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点，
 * wi 是一个信号从源节点传递到目标节点的时间。
 *
 * 现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
 * 输出：2
 *
 *
 * 示例 2：
 *
 *
 * 输入：times = [[1,2,1]], n = 2, k = 1
 * 输出：1
 *
 *
 * 示例 3：
 *
 *
 * 输入：times = [[1,2,1]], n = 2, k = 2
 * 输出：-1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= k <= n <= 100
 * 1 <= times.length <= 6000
 * times[i].length == 3
 * 1 <= ui, vi <= n
 * ui != vi
 * 0 <= wi <= 100
 * 所有 (ui, vi) 对都 互不相同（即，不含重复边）
 *
 *
 */

// @lc code=start
func networkDelayTime(times [][]int, n int, k int) int {
	inf := math.MaxInt32 / 2

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

	// 邻接矩阵存储边信息
	graph := make([][]int, n)
	for i := 0; i < n; i++ {
		graph[i] = make([]int, n)
		for j := 0; j < n; j++ {
			graph[i][j] = inf
		}
	}

	for _, edge := range times {
		// 顶点序号从 0 开始
		u, v, t := edge[0]-1, edge[1]-1, edge[2]
		graph[u][v] = t
	}

	// 从源点到某个点的最短距离数组
	dist := make([]int, n)
	for i := 0; i < n; i++ {
		dist[i] = inf
	}
	// 由于从 k 开始，所以该点距离设为 0，也即源点
	dist[k-1] = 0

	// 顶点是否已确定了到源点的最短路
	used := make([]bool, n)

	for i := 0; i < n; i++ {
		// 在还未确定最短路的点中，寻找距离源点最近的点
		u := -1
		for v := 0; v < n; v++ {
			if !used[v] && (u == -1 || dist[v] < dist[u]) {
				u = v
			}
		}

		// 用该点更新所有其它点的距离
		used[u] = true
		for v := 0; v < n; v++ {
			dist[v] = min(dist[v], dist[u]+graph[u][v])
		}
	}

	// 找到距离最远的点
	ans := 0
	for _, d := range dist {
		if d == inf {
			return -1
		}
		ans = max(ans, d)
	}

	return ans
}

// @lc code=end
