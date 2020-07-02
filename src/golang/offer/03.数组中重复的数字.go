package offer

/**
 * @File    :   03.数组中重复的数字.go
 * @Time    :   2020/07/02 22:36:24
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :   https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
 */
func findRepeatNumber(nums []int) int {
	i := 0
	for i < len(nums) {
		if nums[i] == i {
			i++
		} else {
			j := nums[i]
			if nums[i] == nums[j] {
				return nums[i]
			}
			nums[i], nums[j] = nums[j], nums[i]
		}
	}
	return -1
}
