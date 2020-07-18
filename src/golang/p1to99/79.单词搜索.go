package p1to99

/*
 * @lc app=leetcode.cn id=79 lang=golang
 *
 * [79] 单词搜索
 *
 * https://leetcode-cn.com/problems/word-search/description/
 *
 * algorithms
 * Medium (41.89%)
 * Likes:    481
 * Dislikes: 0
 * Total Accepted:    70.3K
 * Total Submissions: 167.2K
 * Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
 *
 * 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
 *
 * 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
 *
 *
 *
 * 示例:
 *
 * board =
 * [
 * ⁠ ['A','B','C','E'],
 * ⁠ ['S','F','C','S'],
 * ⁠ ['A','D','E','E']
 * ]
 *
 * 给定 word = "ABCCED", 返回 true
 * 给定 word = "SEE", 返回 true
 * 给定 word = "ABCB", 返回 false
 *
 *
 *
 * 提示：
 *
 *
 * board 和 word 中只包含大写和小写英文字母。
 * 1 <= board.length <= 200
 * 1 <= board[i].length <= 200
 * 1 <= word.length <= 10^3
 *
 *
 */

/**
 * @File    :   79.单词搜索.go
 * @Time    :   2020/07/18 18:16:50
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * DFS + 剪枝
 *
 * - 递归参数：
 *   当前元素在矩阵 board 中的行列索引 i 和 j ，当前目标字符在 word 中的索引 k
 *
 * - 终止条件：
 *   1.返回 false ：
 *     (1)行或列索引越界
 *     或 (2)当前矩阵元素与目标字符不同
 *     或 (3)当前矩阵元素已访问过
 *
 *   2.返回 true ：
 *     字符串 word 已全部匹配，即 k = len(word) - 1
 *
 * - 递推工作：
 *   1.标记当前矩阵元素：
 *     将 board[i][j] 值暂存于变量 tmp ，并修改为字符 '#' ，代表此元素已访问过，
 *     防止之后搜索时重复访问。
 *   2.搜索下一单元格：
 *     朝当前元素的 上、下、左、右 四个方向开启下层递归，使用 或 连接（代表只需一条
 *     可行路径） ，并记录结果至 res 。
 *   3.还原当前矩阵元素：
 *     将 tmp 暂存值还原至 board[i][j] 元素。
 *
 * - 回溯返回值：
 *   返回 res ，代表是否搜索到目标字符串
 */
// @lc code=start
func exist(board [][]byte, word string) bool {
	n, m := len(board), len(board[0])
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if dfs(&board, i, j, word, 0) {
				return true
			}
		}
	}
	return false
}

func dfs(board *[][]byte, i, j int, word string, k int) bool {
	if i < 0 || i >= len(*board) || j < 0 || j >= len((*board)[0]) ||
		(*board)[i][j] != word[k] {
		return false
	}
	if k == len(word)-1 {
		return true
	}

	tmp := (*board)[i][j]
	(*board)[i][j] = '#' // 标记已访问
	res := dfs(board, i+1, j, word, k+1) || dfs(board, i-1, j, word, k+1) ||
		dfs(board, i, j+1, word, k+1) || dfs(board, i, j-1, word, k+1)
	(*board)[i][j] = tmp

	return res
}

// @lc code=end
