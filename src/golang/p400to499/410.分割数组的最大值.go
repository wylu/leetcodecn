package p400to499

/*
 * @lc app=leetcode.cn id=410 lang=golang
 *
 * [410] 分割数组的最大值
 *
 * https://leetcode-cn.com/problems/split-array-largest-sum/description/
 *
 * algorithms
 * Hard (44.03%)
 * Likes:    266
 * Dislikes: 0
 * Total Accepted:    17.4K
 * Total Submissions: 34.2K
 * Testcase Example:  '[7,2,5,10,8]\n2'
 *
 * 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
 *
 * 注意:
 * 数组长度 n 满足以下条件:
 *
 *
 * 1 ≤ n ≤ 1000
 * 1 ≤ m ≤ min(50, n)
 *
 *
 * 示例:
 *
 *
 * 输入:
 * nums = [7,2,5,10,8]
 * m = 2
 *
 * 输出:
 * 18
 *
 * 解释:
 * 一共有四种方法将nums分割为2个子数组。
 * 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
 * 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
 *
 *
 */

/**
 * @File    :   410.分割数组的最大值.go
 * @Time    :   2020/07/25 22:09:32
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
// @lc code=start
func splitArray(nums []int, m int) int {
	left, right := 0, 0
	for _, num := range nums {
		right += num
		if num > left {
			left = num
		}
	}

	for left < right {
		mid := left + (right-left)/2
		if checkSplit(nums, m, mid) {
			left = mid + 1
		} else {
			right = mid
		}
	}

	return left
}

func checkSplit(nums []int, m int, limit int) bool {
	total, cnt := 0, 1
	for _, num := range nums {
		if total+num > limit {
			total = num
			cnt++
		} else {
			total += num
		}
	}
	return cnt > m
}

// @lc code=end
