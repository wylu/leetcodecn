package p1700to1799

/*
 * @lc app=leetcode.cn id=1791 lang=golang
 *
 * [1791] 找出星型图的中心节点
 *
 * https://leetcode-cn.com/problems/find-center-of-star-graph/description/
 *
 * algorithms
 * Easy (82.97%)
 * Likes:    22
 * Dislikes: 0
 * Total Accepted:    17.1K
 * Total Submissions: 20.7K
 * Testcase Example:  '[[1,2],[2,3],[4,2]]'
 *
 * 有一个无向的 星型 图，由 n 个编号从 1 到 n 的节点组成。星型图有一个 中心 节点，并且恰有 n - 1
 * 条边将中心节点与其他每个节点连接起来。
 *
 * 给你一个二维整数数组 edges ，其中 edges[i] = [ui, vi] 表示在节点 ui 和 vi 之间存在一条边。请你找出并返回 edges
 * 所表示星型图的中心节点。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：edges = [[1,2],[2,3],[4,2]]
 * 输出：2
 * 解释：如上图所示，节点 2 与其他每个节点都相连，所以节点 2 是中心节点。
 *
 *
 * 示例 2：
 *
 *
 * 输入：edges = [[1,2],[5,1],[1,3],[1,4]]
 * 输出：1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 3 <= n <= 10^5
 * edges.length == n - 1
 * edges[i].length == 2
 * 1 <= ui, vi <= n
 * ui != vi
 * 题目数据给出的 edges 表示一个有效的星型图
 *
 *
 */

/**
 * @File    :   1791.找出星型图的中心节点.go
 * @Time    :   2022/02/18 09:10:25
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findCenter(edges [][]int) int {
	a, b := edges[0][0], edges[0][1]
	c, d := edges[1][0], edges[1][1]
	if a == c || a == d {
		return a
	}
	return b
}

// @lc code=end
