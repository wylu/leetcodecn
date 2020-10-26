package p1300to1399

import "sort"

/*
 * @lc app=leetcode.cn id=1365 lang=golang
 *
 * [1365] 有多少小于当前数字的数字
 *
 * https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
 *
 * algorithms
 * Easy (82.74%)
 * Likes:    88
 * Dislikes: 0
 * Total Accepted:    37.9K
 * Total Submissions: 45.8K
 * Testcase Example:  '[8,1,2,2,3]'
 *
 * 给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
 *
 * 换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
 *
 * 以数组形式返回答案。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [8,1,2,2,3]
 * 输出：[4,0,1,1,3]
 * 解释：
 * 对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。
 * 对于 nums[1]=1 不存在比它小的数字。
 * 对于 nums[2]=2 存在一个比它小的数字：（1）。
 * 对于 nums[3]=2 存在一个比它小的数字：（1）。
 * 对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。
 *
 *
 * 示例 2：
 *
 * 输入：nums = [6,5,4,8]
 * 输出：[2,1,0,3]
 *
 *
 * 示例 3：
 *
 * 输入：nums = [7,7,7,7]
 * 输出：[0,0,0,0]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= nums.length <= 500
 * 0 <= nums[i] <= 100
 *
 *
 */

/**
 * @File    :   1365.有多少小于当前数字的数字.go
 * @Time    :   2020/10/26 11:01:19
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func smallerNumbersThanCurrent(nums []int) []int {
	data := [][2]int{}
	for i, num := range nums {
		data = append(data, [2]int{num, i})
	}
	sort.Slice(data, func(i, j int) bool {
		if data[i][0] == data[j][0] {
			return data[i][1] < data[j][1]
		}
		return data[i][0] < data[j][0]
	})

	ans := make([]int, len(data))
	for i, pre := 0, -1; i < len(data); i++ {
		if pre == -1 || data[i][0] != data[i-1][0] {
			pre = i
		}
		ans[data[i][1]] = pre
	}

	return ans
}

// @lc code=end
