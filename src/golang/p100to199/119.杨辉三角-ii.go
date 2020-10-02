package p100to199

/*
 * @lc app=leetcode.cn id=119 lang=golang
 *
 * [119] 杨辉三角 II
 *
 * https://leetcode-cn.com/problems/pascals-triangle-ii/description/
 *
 * algorithms
 * Easy (61.91%)
 * Likes:    183
 * Dislikes: 0
 * Total Accepted:    71.8K
 * Total Submissions: 115.9K
 * Testcase Example:  '3'
 *
 * 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
 *
 *
 *
 * 在杨辉三角中，每个数是它左上方和右上方的数的和。
 *
 * 示例:
 *
 * 输入: 3
 * 输出: [1,3,3,1]
 *
 *
 * 进阶：
 *
 * 你可以优化你的算法到 O(k) 空间复杂度吗？
 *
 */

/**
 * @File    :   119.杨辉三角-ii.go
 * @Time    :   2020/10/02 22:00:15
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func getRow(rowIndex int) []int {
	pre := []int{1}
	for i := 1; i < rowIndex+1; i++ {
		cur := []int{1}
		for j := 1; j < i; j++ {
			cur = append(cur, pre[j-1]+pre[j])
		}
		cur = append(cur, 1)
		pre = cur
	}
	return pre
}

// @lc code=end
