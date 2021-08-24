package p700to799

/*
 * @lc app=leetcode.cn id=787 lang=golang
 *
 * [787] K 站中转内最便宜的航班
 *
 * https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/description/
 *
 * algorithms
 * Medium (38.33%)
 * Likes:    370
 * Dislikes: 0
 * Total Accepted:    33.5K
 * Total Submissions: 87.5K
 * Testcase Example:  '3\n[[0,1,100],[1,2,100],[0,2,500]]\n0\n2\n1'
 *
 * 有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei]
 * ，表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。
 *
 * 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的
 * 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入:
 * n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
 * src = 0, dst = 2, k = 1
 * 输出: 200
 * 解释:
 * 城市航班图如下
 *
 *
 * 从城市 0 到城市 2 在 1 站中转以内的最便宜价格是 200，如图中红色所示。
 *
 * 示例 2：
 *
 *
 * 输入:
 * n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
 * src = 0, dst = 2, k = 0
 * 输出: 500
 * 解释:
 * 城市航班图如下
 *
 *
 * 从城市 0 到城市 2 在 0 站中转以内的最便宜价格是 500，如图中蓝色所示。
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 100
 * 0 <= flights.length <= (n * (n - 1) / 2)
 * flights[i].length == 3
 * 0 <= fromi, toi < n
 * fromi != toi
 * 1 <= pricei <= 10^4
 * 航班没有重复，且不存在自环
 * 0 <= src, dst, k < n
 * src != dst
 *
 *
 */

/**
 * @File    :   787.k-站中转内最便宜的航班.go
 * @Time    :   2021/08/24 21:11:29
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findCheapestPrice(n int, flights [][]int, src int, dst int, k int) int {
	INF := 1000007
	cache := make([][]int, n)
	graph := make([][][]int, n)
	for i := 0; i < n; i++ {
		cache[i] = make([]int, k+2)
		graph[i] = [][]int{}
	}

	for _, flight := range flights {
		u := flight[0]
		graph[u] = append(graph[u], flight)
	}

	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	var dfs func(u, k int) int
	dfs = func(u, k int) int {
		if k < 0 {
			return INF
		}

		if u == dst {
			return 0
		}

		if cache[u][k] != 0 {
			return cache[u][k]
		}

		res := INF
		for _, flight := range graph[u] {
			res = min(res, dfs(flight[1], k-1)+flight[2])
		}
		cache[u][k] = res
		return res
	}

	ans := dfs(src, k+1)

	if ans == INF {
		return -1
	}
	return ans
}

// @lc code=end
