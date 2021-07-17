package offer

/**
 * @File    :   42.连续子数组的最大和.go
 * @Time    :   2021/07/17 09:28:42
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

func maxSubArray(nums []int) int {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	ans, cur, n := nums[0], nums[0], len(nums)
	for i := 1; i < n; i++ {
		if cur > 0 {
			cur += nums[i]
		} else {
			cur = nums[i]
		}
		ans = max(ans, cur)
	}

	return ans
}
