package p900to999

/*
 * @lc app=leetcode.cn id=997 lang=golang
 *
 * [997] 找到小镇的法官
 *
 * https://leetcode-cn.com/problems/find-the-town-judge/description/
 *
 * algorithms
 * Easy (53.41%)
 * Likes:    217
 * Dislikes: 0
 * Total Accepted:    57.9K
 * Total Submissions: 108.5K
 * Testcase Example:  '2\n[[1,2]]'
 *
 * 在一个小镇里，按从 1 到 n 为 n 个人进行编号。传言称，这些人中有一个是小镇上的秘密法官。
 *
 * 如果小镇的法官真的存在，那么：
 *
 *
 * 小镇的法官不相信任何人。
 * 每个人（除了小镇法官外）都信任小镇的法官。
 * 只有一个人同时满足条件 1 和条件 2 。
 *
 *
 * 给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示编号为 a 的人信任编号为 b 的人。
 *
 * 如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的编号。否则，返回 -1。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 2, trust = [[1,2]]
 * 输出：2
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 3, trust = [[1,3],[2,3]]
 * 输出：3
 *
 *
 * 示例 3：
 *
 *
 * 输入：n = 3, trust = [[1,3],[2,3],[3,1]]
 * 输出：-1
 *
 *
 * 示例 4：
 *
 *
 * 输入：n = 3, trust = [[1,2],[2,3]]
 * 输出：-1
 *
 *
 * 示例 5：
 *
 *
 * 输入：n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
 * 输出：3
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 1000
 * 0 <= trust.length <= 10^4
 * trust[i].length == 2
 * trust[i] 互不相同
 * trust[i][0] != trust[i][1]
 * 1 <= trust[i][0], trust[i][1] <= n
 *
 *
 */

/**
 * @File    :   997.找到小镇的法官.go
 * @Time    :   2021/12/19 21:09:56
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findJudge(n int, trust [][]int) int {
	indegrees := make([]int, n)
	outdegrees := make([]int, n)
	for _, t := range trust {
		outdegrees[t[0]-1]++
		indegrees[t[1]-1]++
	}

	for i := 0; i < n; i++ {
		if indegrees[i] == n-1 && outdegrees[i] == 0 {
			return i + 1
		}
	}

	return -1
}

// @lc code=end

// func findJudge(n int, trust [][]int) int {
// 	cnt := make([]int, n)
// 	for _, t := range trust {
// 		cnt[t[0]-1]--
// 		cnt[t[1]-1]++
// 	}

// 	ans := []int{}
// 	for i, v := range cnt {
// 		if v == n-1 {
// 			ans = append(ans, i+1)
// 		}
// 	}

// 	if len(ans) == 1 {
// 		return ans[0]
// 	}

// 	return -1
// }
