package p1to99

import "sort"

/*
 * @lc app=leetcode.cn id=90 lang=golang
 *
 * [90] 子集 II
 *
 * https://leetcode-cn.com/problems/subsets-ii/description/
 *
 * algorithms
 * Medium (62.93%)
 * Likes:    484
 * Dislikes: 0
 * Total Accepted:    86.2K
 * Total Submissions: 136.9K
 * Testcase Example:  '[1,2,2]'
 *
 * 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
 *
 * 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,2]
 * 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0]
 * 输出：[[],[0]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10
 * -10 <= nums[i] <= 10
 *
 *
 *
 *
 */

/**
 * @File    :   90.子集-ii.go
 * @Time    :   2021/04/09 11:26:40
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func subsetsWithDup(nums []int) [][]int {
	sort.Ints(nums)
	ans, stk, n := [][]int{}, []int{}, len(nums)

	var dfs func(cur int, choosePre bool)
	dfs = func(cur int, choosePre bool) {
		if cur == n {
			subSet := make([]int, len(stk))
			copy(subSet, stk)
			ans = append(ans, subSet)
			return
		}

		dfs(cur+1, false)
		if !choosePre && cur > 0 && nums[cur-1] == nums[cur] {
			return
		}
		stk = append(stk, nums[cur])
		dfs(cur+1, true)
		stk = stk[:len(stk)-1]
	}

	dfs(0, false)
	return ans
}

// @lc code=end
