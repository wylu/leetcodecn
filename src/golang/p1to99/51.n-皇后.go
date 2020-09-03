package p1to99

/*
 * @lc app=leetcode.cn id=51 lang=golang
 *
 * [51] N 皇后
 *
 * https://leetcode-cn.com/problems/n-queens/description/
 *
 * algorithms
 * Hard (71.71%)
 * Likes:    550
 * Dislikes: 0
 * Total Accepted:    63.3K
 * Total Submissions: 88.3K
 * Testcase Example:  '4'
 *
 * n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
 *
 *
 *
 * 上图为 8 皇后问题的一种解法。
 *
 * 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
 *
 * 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
 *
 *
 *
 * 示例：
 *
 * 输入：4
 * 输出：[
 * ⁠[".Q..",  // 解法 1
 * ⁠ "...Q",
 * ⁠ "Q...",
 * ⁠ "..Q."],
 *
 * ⁠["..Q.",  // 解法 2
 * ⁠ "Q...",
 * ⁠ "...Q",
 * ⁠ ".Q.."]
 * ]
 * 解释: 4 皇后问题存在两个不同的解法。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
 *
 *
 */

/**
 * @File    :   51.n-皇后.go
 * @Time    :   2020/09/03 10:44:34
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 两个有用的细节。
 *
 * （1）一行只可能有一个皇后且一列也只可能有一个皇后。这意味着没有必要
 * 在棋盘上考虑所有的方格。只需要按列循环即可。
 * （2）对于所有的主对角线有 行号 - 列号 = 常数，对于所有的次对角线有
 * 行号 + 列号 = 常数。
 *
 * 这可以让我们标记已经在攻击范围下的对角线并且检查一个方格 (行号, 列号)
 * 是否处在攻击位置。
 */

// @lc code=start
func solveNQueens(n int) [][]string {
	ans := [][]string{}
	if n <= 0 {
		return ans
	}

	cur := make([][]byte, n)
	for i := 0; i < n; i++ {
		cur[i] = make([]byte, n)
		for j := 0; j < n; j++ {
			cur[i][j] = '.'
		}
	}

	cols, dales, hills := make([]int, n), make([]int, 2*n-1), make([]int, 2*n-1)
	dfs51(0, n, &cur, &ans, &cols, &dales, &hills)
	return ans
}

func dfs51(r, n int, cur *[][]byte, ans *[][]string, cols *[]int, dales *[]int, hills *[]int) {
	if r == n {
		addSolution(n, cur, ans)
		return
	}

	for c := 0; c < n; c++ {
		if ok(r, c, n, (*cols), (*dales), (*hills)) {
			rmc, rpc := (r-c+(2*n-1))%(2*n-1), r+c
			(*cols)[c], (*dales)[rmc], (*hills)[rpc] = 1, 1, 1
			(*cur)[r][c] = 'Q'
			dfs51(r+1, n, cur, ans, cols, dales, hills)
			(*cur)[r][c] = '.'
			(*cols)[c], (*dales)[rmc], (*hills)[rpc] = 0, 0, 0
		}
	}
}

func addSolution(n int, cur *[][]byte, ans *[][]string) {
	solu := make([]string, n)
	for i := 0; i < n; i++ {
		solu[i] = string((*cur)[i])
	}
	(*ans) = append((*ans), solu)
}

func ok(r, c, n int, cols []int, dales []int, hills []int) bool {
	rmc, rpc := (r-c+(2*n-1))%(2*n-1), r+c
	return cols[c]+dales[rmc]+hills[rpc] == 0
}

// @lc code=end
