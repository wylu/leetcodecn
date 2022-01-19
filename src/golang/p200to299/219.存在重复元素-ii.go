package p200to299

/*
 * @lc app=leetcode.cn id=219 lang=golang
 *
 * [219] 存在重复元素 II
 *
 * https://leetcode-cn.com/problems/contains-duplicate-ii/description/
 *
 * algorithms
 * Easy (42.76%)
 * Likes:    370
 * Dislikes: 0
 * Total Accepted:    129.1K
 * Total Submissions: 302K
 * Testcase Example:  '[1,2,3,1]\n3'
 *
 * 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且
 * abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3,1], k = 3
 * 输出：true
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,0,1,1], k = 1
 * 输出：true
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1,2,3,1,2,3], k = 2
 * 输出：false
 *
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 * 0 <= k <= 10^5
 *
 *
 */

/**
 * @File    :   219.存在重复元素-ii.go
 * @Time    :   2022/01/19 09:08:51
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func containsNearbyDuplicate(nums []int, k int) bool {
	pos := map[int]int{}
	for i, num := range nums {
		j, ok := pos[num]
		if ok && i-j <= k{
			return true
		}
		pos[num] = i
	}
	return false
}

// @lc code=end
