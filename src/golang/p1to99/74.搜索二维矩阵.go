package p1to99

/*
 * @lc app=leetcode.cn id=74 lang=golang
 *
 * [74] 搜索二维矩阵
 *
 * https://leetcode-cn.com/problems/search-a-2d-matrix/description/
 *
 * algorithms
 * Medium (38.24%)
 * Likes:    209
 * Dislikes: 0
 * Total Accepted:    51.8K
 * Total Submissions: 134.7K
 * Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
 *
 * 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
 *
 *
 * 每行中的整数从左到右按升序排列。
 * 每行的第一个整数大于前一行的最后一个整数。
 *
 *
 * 示例 1:
 *
 * 输入:
 * matrix = [
 * ⁠ [1,   3,  5,  7],
 * ⁠ [10, 11, 16, 20],
 * ⁠ [23, 30, 34, 50]
 * ]
 * target = 3
 * 输出: true
 *
 *
 * 示例 2:
 *
 * 输入:
 * matrix = [
 * ⁠ [1,   3,  5,  7],
 * ⁠ [10, 11, 16, 20],
 * ⁠ [23, 30, 34, 50]
 * ]
 * target = 13
 * 输出: false
 *
 */

/**
 * @File    :   74.搜索二维矩阵.go
 * @Time    :   2020/07/18 12:43:59
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 输入的 n x m 矩阵可以视为长度为 n x m 的有序数组。
 *
 * [
 *   [ 1,  3,  5,  7],
 *   [10, 11, 16, 20],   =>  [1,3,5,7, 10,11,16,20, 23,30,34,50]
 *   [23, 30, 34, 50],
 * ]
 *
 * 由于该 虚数组 的序号可以由下式方便地转化为原矩阵中的行和列，所以该有序数组
 * 非常适合二分查找。
 *
 *   row = idx // m
 *   col = idx % m
 *
 */
// @lc code=start
func searchMatrix(matrix [][]int, target int) bool {
	if matrix == nil || len(matrix) == 0 {
		return false
	}

	n, m := len(matrix), len(matrix[0])
	lo, hi := 0, n*m-1
	for lo <= hi {
		mid := lo + (hi-lo)/2
		row, col := mid/m, mid%m
		if matrix[row][col] == target {
			return true
		} else if matrix[row][col] < target {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return false
}

// @lc code=end
