package p100to199

/*
 * @lc app=leetcode.cn id=118 lang=golang
 *
 * [118] 杨辉三角
 *
 * https://leetcode-cn.com/problems/pascals-triangle/description/
 *
 * algorithms
 * Easy (67.50%)
 * Likes:    354
 * Dislikes: 0
 * Total Accepted:    108.4K
 * Total Submissions: 160.6K
 * Testcase Example:  '5'
 *
 * 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
 *
 *
 *
 * 在杨辉三角中，每个数是它左上方和右上方的数的和。
 *
 * 示例:
 *
 * 输入: 5
 * 输出:
 * [
 * ⁠    [1],
 * ⁠   [1,1],
 * ⁠  [1,2,1],
 * ⁠ [1,3,3,1],
 * ⁠[1,4,6,4,1]
 * ]
 *
 */

/**
 * @File    :   118.杨辉三角.go
 * @Time    :   2020/10/02 18:03:35
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func generate(numRows int) [][]int {
	if numRows <= 0 {
		return [][]int{}
	}

	ans := make([][]int, numRows)
	ans[0] = []int{1}

	for i := 1; i < numRows; i++ {
		row := make([]int, i+1)
		row[0] = 1
		for j := 1; j < i; j++ {
			row[j] = ans[i-1][j-1] + ans[i-1][j]
		}
		row[i] = 1
		ans[i] = row
	}

	return ans
}

// @lc code=end
