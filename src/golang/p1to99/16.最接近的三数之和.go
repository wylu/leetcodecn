package p1to99

import "sort"

/*
 * @lc app=leetcode.cn id=16 lang=golang
 *
 * [16] 最接近的三数之和
 *
 * https://leetcode-cn.com/problems/3sum-closest/description/
 *
 * algorithms
 * Medium (45.83%)
 * Likes:    580
 * Dislikes: 0
 * Total Accepted:    155.8K
 * Total Submissions: 340.1K
 * Testcase Example:  '[-1,2,1,-4]\n1'
 *
 * 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
 * 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
 *
 *
 *
 * 示例：
 *
 * 输入：nums = [-1,2,1,-4], target = 1
 * 输出：2
 * 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 3 <= nums.length <= 10^3
 * -10^3 <= nums[i] <= 10^3
 * -10^4 <= target <= 10^4
 *
 *
 */

/**
 * @File    :   16.最接近的三数之和.go
 * @Time    :   2020/09/25 13:51:08
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 双指针
 *
 * 详见 [15] 三数之和 https://leetcode-cn.com/problems/3sum/
 */

// @lc code=start
func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	ans, n := nums[0]+nums[1]+nums[2], len(nums)

	abs := func(x int) int {
		if x >= 0 {
			return x
		}
		return -x
	}

	for a := 0; a < n-2; a++ {
		if a > 0 && nums[a] == nums[a-1] {
			continue
		}

		c := n - 1

		for b := a + 1; b < n-1; b++ {
			if b > a+1 && nums[b] == nums[b-1] {
				continue
			}

			for b < c && nums[a]+nums[b]+nums[c] > target {
				if nums[a]+nums[b]+nums[c]-target < abs(ans-target) {
					ans = nums[a] + nums[b] + nums[c]
				}
				c--
			}

			if b == c {
				break
			}

			if abs(nums[a]+nums[b]+nums[c]-target) < abs(ans-target) {
				ans = nums[a] + nums[b] + nums[c]
			}

			if ans == target {
				return ans
			}
		}
	}

	return ans
}

// @lc code=end
