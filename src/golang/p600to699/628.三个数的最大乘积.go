package p600to699

/*
 * @lc app=leetcode.cn id=628 lang=golang
 *
 * [628] 三个数的最大乘积
 *
 * https://leetcode-cn.com/problems/maximum-product-of-three-numbers/description/
 *
 * algorithms
 * Easy (50.36%)
 * Likes:    174
 * Dislikes: 0
 * Total Accepted:    27.8K
 * Total Submissions: 55.2K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
 *
 * 示例 1:
 *
 *
 * 输入: [1,2,3]
 * 输出: 6
 *
 *
 * 示例 2:
 *
 *
 * 输入: [1,2,3,4]
 * 输出: 24
 *
 *
 * 注意:
 *
 *
 * 给定的整型数组长度范围是[3,10^4]，数组中所有的元素范围是[-1000, 1000]。
 * 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
 *
 *
 */

/**
 * @File    :   628.三个数的最大乘积.go
 * @Time    :   2020/09/23 21:57:54
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法二：线性扫描
 *
 * 实际上只要求出数组中最大的三个数以及最小的两个数，因此我们可以不用排序，
 * 用线性扫描直接得出这五个数。
 */

// @lc code=start
func maximumProduct(nums []int) int {
	max1, max2, max3 := -1001, -1001, -1001
	min1, min2 := 1001, 1001
	for _, num := range nums {
		tmp := num
		if num > max1 {
			num, max1 = max1, num
		}
		if num > max2 {
			num, max2 = max2, num
		}
		if num > max3 {
			num, max3 = max3, num
		}

		num = tmp
		if num < min1 {
			num, min1 = min1, num
		}
		if num < min2 {
			num, min2 = min2, num
		}
	}

	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	return max(min1*min2*max1, max1*max2*max3)
}

// @lc code=end
