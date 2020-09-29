package p1500to1599

import "math"

/*
 * @lc app=leetcode.cn id=1521 lang=golang
 *
 * [1521] 找到最接近目标值的函数值
 *
 * https://leetcode-cn.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/description/
 *
 * algorithms
 * Hard (37.79%)
 * Likes:    24
 * Dislikes: 0
 * Total Accepted:    1.9K
 * Total Submissions: 5.1K
 * Testcase Example:  '[9,12,3,7,15]\n5'
 *
 *
 *
 * Winston 构造了一个如上所示的函数 func 。他有一个整数数组 arr 和一个整数 target ，他想找到让 |func(arr, l, r)
 * - target| 最小的 l 和 r 。
 *
 * 请你返回 |func(arr, l, r) - target| 的最小值。
 *
 * 请注意， func 的输入参数 l 和 r 需要满足 0 <= l, r < arr.length 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：arr = [9,12,3,7,15], target = 5
 * 输出：2
 * 解释：所有可能的 [l,r] 数对包括
 * [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]]，
 * Winston 得到的相应结果为 [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0] 。最接近 5 的值是 7 和 3，所以最小差值为
 * 2 。
 *
 *
 * 示例 2：
 *
 * 输入：arr = [1000000,1000000,1000000], target = 1
 * 输出：999999
 * 解释：Winston 输入函数的所有可能 [l,r] 数对得到的函数值都为 1000000 ，所以最小差值为 999999 。
 *
 *
 * 示例 3：
 *
 * 输入：arr = [1,2,4,8,16], target = 0
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= arr.length <= 10^5
 * 1 <= arr[i] <= 10^6
 * 0 <= target <= 10^7
 *
 *
 */

/**
 * @File    :   1521.找到最接近目标值的函数值.go
 * @Time    :   2020/09/29 17:56:06
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func closestToTarget(arr []int, target int) int {
	ans := math.MaxInt32
	opts := map[int]bool{-1: true}

	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}

	for _, num := range arr {
		ans = min(ans, abs(num-target))
		tmp := map[int]bool{num: true}
		for k := range opts {
			ans = min(ans, abs((k&num)-target))
			tmp[k&num] = true
		}
		opts = tmp
	}

	return ans
}

// @lc code=end
