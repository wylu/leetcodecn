package p1to99

/*
 * @lc app=leetcode.cn id=47 lang=golang
 *
 * [47] 全排列 II
 *
 * https://leetcode-cn.com/problems/permutations-ii/description/
 *
 * algorithms
 * Medium (59.81%)
 * Likes:    393
 * Dislikes: 0
 * Total Accepted:    87.4K
 * Total Submissions: 146.1K
 * Testcase Example:  '[1,1,2]'
 *
 * 给定一个可包含重复数字的序列，返回所有不重复的全排列。
 *
 * 示例:
 *
 * 输入: [1,1,2]
 * 输出:
 * [
 * ⁠ [1,1,2],
 * ⁠ [1,2,1],
 * ⁠ [2,1,1]
 * ]
 *
 */

/**
 * @File    :   47.全排列-ii.go
 * @Time    :   2020/09/18 00:17:32
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func permuteUnique(nums []int) [][]int {
	cnts := make(map[int]int)
	for _, num := range nums {
		cnts[num]++
	}

	stack := []int{}
	ans := [][]int{}
	dfs47(nums, &stack, 0, &ans, &cnts)
	return ans
}

func dfs47(nums []int, stack *[]int, c int, ans *[][]int, cnts *map[int]int) {
	if c == len(nums) {
		res := make([]int, len(nums))
		copy(res, *stack)
		*ans = append(*ans, res)
		return
	}

	for num, cnt := range *cnts {
		if cnt > 0 {
			(*cnts)[num]--
			*stack = append(*stack, num)
			dfs47(nums, stack, c+1, ans, cnts)
			*stack = (*stack)[:len(*stack)-1]
			(*cnts)[num]++
		}
	}
}

// @lc code=end
