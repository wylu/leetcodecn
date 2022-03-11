package p2000to2099

/*
 * @lc app=leetcode.cn id=2049 lang=golang
 *
 * [2049] 统计最高分的节点数目
 *
 * https://leetcode-cn.com/problems/count-nodes-with-the-highest-score/description/
 *
 * algorithms
 * Medium (50.11%)
 * Likes:    74
 * Dislikes: 0
 * Total Accepted:    12.4K
 * Total Submissions: 24.6K
 * Testcase Example:  '[-1,2,0,2,0]'
 *
 * 给你一棵根节点为 0 的 二叉树 ，它总共有 n 个节点，节点编号为 0 到 n - 1 。同时给你一个下标从 0 开始的整数数组 parents
 * 表示这棵树，其中 parents[i] 是节点 i 的父节点。由于节点 0 是根，所以 parents[0] == -1 。
 *
 * 一个子树的 大小 为这个子树内节点的数目。每个节点都有一个与之关联的 分数 。求出某个节点分数的方法是，将这个节点和与它相连的边全部 删除
 * ，剩余部分是若干个 非空 子树，这个节点的 分数 为所有这些子树 大小的乘积 。
 *
 * 请你返回有 最高得分 节点的 数目 。
 *
 *
 *
 * 示例 1:
 *
 *
 *
 * 输入：parents = [-1,2,0,2,0]
 * 输出：3
 * 解释：
 * - 节点 0 的分数为：3 * 1 = 3
 * - 节点 1 的分数为：4 = 4
 * - 节点 2 的分数为：1 * 1 * 2 = 2
 * - 节点 3 的分数为：4 = 4
 * - 节点 4 的分数为：4 = 4
 * 最高得分为 4 ，有三个节点得分为 4 （分别是节点 1，3 和 4 ）。
 *
 *
 * 示例 2：
 *
 *
 *
 * 输入：parents = [-1,2,0]
 * 输出：2
 * 解释：
 * - 节点 0 的分数为：2 = 2
 * - 节点 1 的分数为：2 = 2
 * - 节点 2 的分数为：1 * 1 = 1
 * 最高分数为 2 ，有两个节点分数为 2 （分别为节点 0 和 1 ）。
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == parents.length
 * 2 <= n <= 10^5
 * parents[0] == -1
 * 对于 i != 0 ，有 0 <= parents[i] <= n - 1
 * parents 表示一棵二叉树。
 *
 *
 */

/**
 * @File    :   2049.统计最高分的节点数目.go
 * @Time    :   2022/03/11 14:06:58
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func countHighestScoreNodes(parents []int) int {
	n := len(parents)
	graph := make([][]int, n)
	for i, p := range parents[1:] {
		graph[p] = append(graph[p], i+1)
	}

	score, ans := 0, 0
	var dfs func(int) int
	dfs = func(root int) int {
		cur, cnt := 1, n-1
		for _, child := range graph[root] {
			sz := dfs(child)
			cur *= sz
			cnt -= sz
		}

		if root > 0 {
			cur *= cnt
		}

		if cur == score {
			ans++
		} else if cur > score {
			score, ans = cur, 1
		}

		return n - cnt
	}

	dfs(0)
	return ans
}

// @lc code=end

// func countHighestScoreNodes(parents []int) int {
// 	n := len(parents)
// 	graph := make([][]int, n)
// 	cache := make([]int, n)
// 	for i, p := range parents {
// 		if p != -1 {
// 			graph[p] = append(graph[p], i)
// 		}
// 	}

// 	var dfs func(int) int
// 	dfs = func(root int) int {
// 		if cache[root] != 0 {
// 			return cache[root]
// 		}

// 		tot := 1
// 		for _, child := range graph[root] {
// 			tot += dfs(child)
// 		}

// 		cache[root] = tot
// 		return tot
// 	}

// 	score, count := 0, 0
// 	for i := 0; i < n; i++ {
// 		parts := [3]int{}
// 		if len(graph[i]) > 0 {
// 			parts[1] = dfs(graph[i][0])
// 		}
// 		if len(graph[i]) > 1 {
// 			parts[2] = dfs(graph[i][1])
// 		}
// 		if parents[i] != -1 {
// 			parts[0] = n - parts[1] - parts[2] - 1
// 		}

// 		// fmt.Printf("i: %v, P: %v, L: %v, R: %v\n", i, parts[0], parts[1], parts[2])
// 		if parts[0]+parts[1]+parts[2] == 0 {
// 			continue
// 		}

// 		cur := 1
// 		for i := 0; i < 3; i++ {
// 			if parts[i] > 0 {
// 				cur *= parts[i]
// 			}
// 		}

// 		if cur > score {
// 			score, count = cur, 1
// 		} else if cur == score {
// 			count++
// 		}
// 	}

// 	return count
// }
