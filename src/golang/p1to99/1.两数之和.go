package p1to99

/*
 * @lc app=leetcode.cn id=1 lang=golang
 *
 * [1] 两数之和
 *
 * https://leetcode-cn.com/problems/two-sum/description/
 *
 * algorithms
 * Easy (48.87%)
 * Likes:    8629
 * Dislikes: 0
 * Total Accepted:    1.2M
 * Total Submissions: 2.5M
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
 *
 * 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
 *
 *
 *
 * 示例:
 *
 * 给定 nums = [2, 7, 11, 15], target = 9
 *
 * 因为 nums[0] + nums[1] = 2 + 7 = 9
 * 所以返回 [0, 1]
 *
 *
 */

/**
 * @File    :   1.两数之和.go
 * @Time    :   2020/07/13 22:35:53
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
// @lc code=start
func twoSum(nums []int, target int) []int {
	if nums == nil || len(nums) < 2 {
		return nil
	}

	num2idx := map[int]int{}
	for i := 0; i < len(nums); i++ {
		if idx, ok := num2idx[target-nums[i]]; ok {
			return []int{idx, i}
		}
		num2idx[nums[i]] = i
	}
	return nil
}

// @lc code=end
