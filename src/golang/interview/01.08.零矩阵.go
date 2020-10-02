package interview

/**
 * @File    :   01.08.零矩阵.go
 * @Time    :   2020/10/02 11:34:23
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

func setZeroes(matrix [][]int) {
	m, n := len(matrix), len(matrix[0])
	rows, cols := make([]bool, m), make([]bool, n)

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 0 {
				rows[i], cols[j] = true, true
			}
		}
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if rows[i] || cols[j] {
				matrix[i][j] = 0
			}
		}
	}
}
