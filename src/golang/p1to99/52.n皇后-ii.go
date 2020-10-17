package p1to99

/*
 * @lc app=leetcode.cn id=52 lang=golang
 *
 * [52] N皇后 II
 *
 * https://leetcode-cn.com/problems/n-queens-ii/description/
 *
 * algorithms
 * Hard (80.57%)
 * Likes:    158
 * Dislikes: 0
 * Total Accepted:    36.2K
 * Total Submissions: 45K
 * Testcase Example:  '4'
 *
 * n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
 *
 *
 *
 * 上图为 8 皇后问题的一种解法。
 *
 * 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
 *
 * 示例:
 *
 * 输入: 4
 * 输出: 2
 * 解释: 4 皇后问题存在如下两个不同的解法。
 * [
 * [".Q..",  // 解法 1
 * "...Q",
 * "Q...",
 * "..Q."],
 *
 * ["..Q.",  // 解法 2
 * "Q...",
 * "...Q",
 * ".Q.."]
 * ]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或
 * N-1 步，可进可退。（引用自 百度百科 - 皇后 ）
 *
 *
 */

/**
 * @File    :   52.n皇后-ii.go
 * @Time    :   2020/10/17 10:21:46
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func totalNQueens(n int) int {
	ans, m := 0, 2*n-1
	cols, dales, hills := make([]bool, n), make([]bool, m), make([]bool, m)

	ok := func(x, y int) bool {
		sub, add := (x-y+m)%m, x+y
		return !(cols[y] || dales[sub] || hills[add])
	}

	var dfs func(x int)
	dfs = func(x int) {
		if x == n {
			ans++
			return
		}
		for y := 0; y < n; y++ {
			if ok(x, y) {
				sub, add := (x-y+m)%m, x+y
				cols[y], dales[sub], hills[add] = true, true, true
				dfs(x + 1)
				cols[y], dales[sub], hills[add] = false, false, false
			}
		}
	}

	dfs(0)
	return ans
}

// @lc code=end
