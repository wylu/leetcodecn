package offer

/**
 * @File    :   12.矩阵中的路径.go
 * @Time    :   2020/07/07 22:49:06
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
 *     将 board[i][j] 值暂存于变量 tmp ，并修改为字符 '/' ，代表此元素已访问过，
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
func exist(board [][]byte, word string) bool {
	m, n := len(board), len(board[0])
	ws := []byte(word)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if dfs(&board, i, j, ws, 0) {
				return true
			}
		}
	}
	return false
}

func dfs(board *([][]byte), x, y int, ws []byte, k int) bool {
	if x < 0 || x >= len(*board) || y < 0 || y >= len((*board)[0]) || (*board)[x][y] != ws[k] {
		return false
	}
	if k == len(ws)-1 {
		return true
	}
	tmp := (*board)[x][y]
	(*board)[x][y] = '#' // 标记已访问
	res := dfs(board, x+1, y, ws, k+1) || dfs(board, x-1, y, ws, k+1) ||
		dfs(board, x, y-1, ws, k+1) || dfs(board, x, y+1, ws, k+1)
	(*board)[x][y] = tmp
	return res
}
