package p1to99

/*
 * @lc app=leetcode.cn id=31 lang=golang
 *
 * [31] 下一个排列
 *
 * https://leetcode-cn.com/problems/next-permutation/description/
 *
 * algorithms
 * Medium (34.63%)
 * Likes:    749
 * Dislikes: 0
 * Total Accepted:    101.5K
 * Total Submissions: 289.7K
 * Testcase Example:  '[1,2,3]'
 *
 * 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
 *
 * 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
 *
 * 必须原地修改，只允许使用额外常数空间。
 *
 * 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
 * 1,2,3 → 1,3,2
 * 3,2,1 → 1,2,3
 * 1,1,5 → 1,5,1
 *
 */

/**
 * @File    :   31.下一个排列.go
 * @Time    :   2020/11/10 09:58:01
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func nextPermutation(nums []int) {
	n := len(nums)
	if n <= 1 {
		return
	}

	reverse := func(left, right int) {
		for left < right {
			nums[left], nums[right] = nums[right], nums[left]
			left++
			right--
		}
	}

	i := n - 1
	for i > 0 && nums[i] <= nums[i-1] {
		i--
	}

	if i == 0 {
		reverse(0, n-1)
		return
	}

	j := i - 1
	for ; j < n-1 && nums[j+1] > nums[i-1]; j++ {
	}
	nums[i-1], nums[j] = nums[j], nums[i-1]
	reverse(i, n-1)
}

// @lc code=end
