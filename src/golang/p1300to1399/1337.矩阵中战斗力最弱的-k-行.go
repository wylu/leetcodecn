package p1300to1399

import (
	"sort"
)

/*
 * @lc app=leetcode.cn id=1337 lang=golang
 *
 * [1337] 矩阵中战斗力最弱的 K 行
 *
 * https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix/description/
 *
 * algorithms
 * Easy (70.09%)
 * Likes:    84
 * Dislikes: 0
 * Total Accepted:    27.1K
 * Total Submissions: 38.7K
 * Testcase Example:  '[[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]\n3'
 *
 * 给你一个大小为 m * n 的矩阵 mat，矩阵由若干军人和平民组成，分别用 1 和 0 表示。
 *
 * 请你返回矩阵中战斗力最弱的 k 行的索引，按从最弱到最强排序。
 *
 * 如果第 i 行的军人数量少于第 j 行，或者两行军人数量相同但 i 小于 j，那么我们认为第 i 行的战斗力比第 j 行弱。
 *
 * 军人 总是 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：mat =
 * [[1,1,0,0,0],
 * ⁠[1,1,1,1,0],
 * ⁠[1,0,0,0,0],
 * ⁠[1,1,0,0,0],
 * ⁠[1,1,1,1,1]],
 * k = 3
 * 输出：[2,0,3]
 * 解释：
 * 每行中的军人数目：
 * 行 0 -> 2
 * 行 1 -> 4
 * 行 2 -> 1
 * 行 3 -> 2
 * 行 4 -> 5
 * 从最弱到最强对这些行排序后得到 [2,0,3,1,4]
 *
 *
 * 示例 2：
 *
 *
 * 输入：mat =
 * [[1,0,0,0],
 * [1,1,1,1],
 * [1,0,0,0],
 * [1,0,0,0]],
 * k = 2
 * 输出：[0,2]
 * 解释：
 * 每行中的军人数目：
 * 行 0 -> 1
 * 行 1 -> 4
 * 行 2 -> 1
 * 行 3 -> 1
 * 从最弱到最强对这些行排序后得到 [0,2,3,1]
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == mat.length
 * n == mat[i].length
 * 2 <= n, m <= 100
 * 1 <= k <= m
 * matrix[i][j] 不是 0 就是 1
 *
 *
 */

// @lc code=start
func kWeakestRows(mat [][]int, k int) []int {
	m, n := len(mat), len(mat[0])
	cnts := make([][2]int, 0, m)

	for i := 0; i < m; i++ {
		c := 0
		for j := 0; j < n; j++ {
			if mat[i][j] == 0 {
				break
			}
			c++
		}
		cnts = append(cnts, [2]int{c, i})
	}

	sort.Slice(cnts, func(i, j int) bool {
		if cnts[i][0] == cnts[j][0] {
			return cnts[i][1] <= cnts[j][1]
		}
		return cnts[i][0] <= cnts[j][0]
	})

	ans := make([]int, k)
	for i := 0; i < k; i++ {
		ans[i] = cnts[i][1]
	}
	return ans
}

// @lc code=end
