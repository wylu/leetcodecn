package p800to899

import "sort"

/*
 * @lc app=leetcode.cn id=802 lang=golang
 *
 * [802] 找到最终的安全状态
 *
 * https://leetcode-cn.com/problems/find-eventual-safe-states/description/
 *
 * algorithms
 * Medium (54.66%)
 * Likes:    202
 * Dislikes: 0
 * Total Accepted:    18.3K
 * Total Submissions: 33.5K
 * Testcase Example:  '[[1,2],[2,3],[5],[0],[5],[],[]]'
 *
 * 在有向图中，以某个节点为起始节点，从该点出发，每一步沿着图中的一条有向边行走。如果到达的节点是终点（即它没有连出的有向边），则停止。
 *
 * 对于一个起始节点，如果从该节点出发，无论每一步选择沿哪条有向边行走，最后必然在有限步内到达终点，则将该起始节点称作是 安全 的。
 *
 * 返回一个由图中所有安全的起始节点组成的数组作为答案。答案数组中的元素应当按 升序 排列。
 *
 * 该有向图有 n 个节点，按 0 到 n - 1 编号，其中 n 是 graph 的节点数。图以下述形式给出：graph[i] 是编号 j
 * 节点的一个列表，满足 (i, j) 是图的一条有向边。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：graph = [[1,2],[2,3],[5],[0],[5],[],[]]
 * 输出：[2,4,5,6]
 * 解释：示意图如上。
 *
 *
 * 示例 2：
 *
 *
 * 输入：graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
 * 输出：[4]
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == graph.length
 * 1 <= n <= 10^4
 * 0 <= graph[i].length <= n
 * graph[i] 按严格递增顺序排列。
 * 图中可能包含自环。
 * 图中边的数目在范围 [1, 4 * 10^4] 内。
 *
 *
 *
 *
 */

/**
 * @File    :   802.找到最终的安全状态.go
 * @Time    :   2021/08/05 14:43:46
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func eventualSafeNodes(graph [][]int) []int {
	n := len(graph)
	que := []int{}
	outdegree := make([]int, n)
	rgraph := make([][]int, n)
	for i := 0; i < n; i++ {
		rgraph[i] = []int{}
	}

	for u := 0; u < n; u++ {
		outdegree[u] = len(graph[u])
		// 出度为 0 的节点入队列
		if outdegree[u] == 0 {
			que = append(que, u)
			continue
		}

		for _, v := range graph[u] {
			rgraph[v] = append(rgraph[v], u)
		}
	}

	ans := []int{}
	for len(que) > 0 {
		v := que[0]
		que = que[1:]
		ans = append(ans, v)

		for _, u := range rgraph[v] {
			outdegree[u]--
			if outdegree[u] == 0 {
				que = append(que, u)
			}
		}
	}

	sort.Ints(ans)
	return ans
}

// @lc code=end
