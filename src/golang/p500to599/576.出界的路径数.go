package p500to599

/*
 * @lc app=leetcode.cn id=576 lang=golang
 *
 * [576] 出界的路径数
 *
 * https://leetcode-cn.com/problems/out-of-boundary-paths/description/
 *
 * algorithms
 * Medium (43.12%)
 * Likes:    163
 * Dislikes: 0
 * Total Accepted:    13.6K
 * Total Submissions: 31.6K
 * Testcase Example:  '2\n2\n2\n0\n0'
 *
 * 给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn]
 * 。你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。
 *
 * 给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对
 * 10^9 + 7 取余 后的结果。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
 * 输出：6
 *
 *
 * 示例 2：
 *
 *
 * 输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
 * 输出：12
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= m, n <= 50
 * 0 <= maxMove <= 50
 * 0 <= startRow < m
 * 0 <= startColumn < n
 *
 *
 */

/**
 * @File    :   576.出界的路径数.go
 * @Time    :   2021/08/15 12:23:54
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 *
 * 方法一：动态规划
 * 可以使用动态规划计算出界的路径数。
 *
 * 动态规划的状态由移动次数、行和列决定，定义 dp[i][j][k] 表示球移动 i 次之后
 * 位于坐标 (j, k) 的路径数量。当 i=0 时，球一定位于起始坐标 (startRow, startColumn)，
 * 因此动态规划的边界情况是：dp[0][startRow][startColumn]=1，
 * 当 (j, k) != (startRow, startColumn) 时有 dp[0][j][k]=0。
 *
 * 如果球移动了 i 次之后位于坐标 (j, k)，且 i < maxMove，0 <= j < m，0 <= k < n，
 * 则移动第 i+1 次之后，球一定位于和坐标 (j, k) 相邻的一个坐标，记为 (j', k')。
 *
 * 当 0 <= j' < m 且 0 <= k' < n 时，球在移动 i+1 次之后没有出界，将 dp[i][j][k]
 * 的值加到 dp[i+1][j'][k']；
 *
 * 否则，球在第 i+1 次移动之后出界，将 dp[i][j][k] 的值加到出界的路径数。
 *
 * 由于最多可以移动的次数是 maxMove，因此遍历 0 <= i < maxMove，根据 dp[i][][]
 * 计算 dp[i+1][][] 的值以及出界的路径数，即可得到最多移动 maxMove 次的情况下的
 * 出界的路径数。
 *
 * 根据上述思路，可以得到时间复杂度和空间复杂度都是 O(maxMove * m * n) 的实现。
 */

// @lc code=start
func findPaths(m int, n int, maxMove int, startRow int, startColumn int) int {
	MOD := 1000000007
	d := [5]int{0, 1, 0, -1, 0}
	ans := 0
	f := make([][][]int, maxMove+1)
	for i := 0; i <= maxMove; i++ {
		f[i] = make([][]int, m)
		for j := 0; j < m; j++ {
			f[i][j] = make([]int, n)
		}
	}

	f[0][startRow][startColumn] = 1
	for i := 0; i < maxMove; i++ {
		for j := 0; j < m; j++ {
			for k := 0; k < n; k++ {
				if f[i][j][k] > 0 {
					for v := 0; v < 4; v++ {
						vj, vk := j+d[v], k+d[v+1]
						if vj >= 0 && vj < m && vk >= 0 && vk < n {
							f[i+1][vj][vk] = (f[i+1][vj][vk] + f[i][j][k]) % MOD
						} else {
							ans = (ans + f[i][j][k]) % MOD
						}
					}
				}
			}
		}
	}

	return ans
}

// @lc code=end
