package p1200to1299

import (
	"math"
	"sort"
)

/*
 * @lc app=leetcode.cn id=1200 lang=golang
 *
 * [1200] 最小绝对差
 *
 * https://leetcode.cn/problems/minimum-absolute-difference/description/
 *
 * algorithms
 * Easy (72.50%)
 * Likes:    102
 * Dislikes: 0
 * Total Accepted:    38.9K
 * Total Submissions: 53.7K
 * Testcase Example:  '[4,2,1,3]'
 *
 * 给你个整数数组 arr，其中每个元素都 不相同。
 *
 * 请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
 *
 *
 *
 * 示例 1：
 *
 * 输入：arr = [4,2,1,3]
 * 输出：[[1,2],[2,3],[3,4]]
 *
 *
 * 示例 2：
 *
 * 输入：arr = [1,3,6,10,15]
 * 输出：[[1,3]]
 *
 *
 * 示例 3：
 *
 * 输入：arr = [3,8,-10,23,19,-4,-14,27]
 * 输出：[[-14,-10],[19,23],[23,27]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= arr.length <= 10^5
 * -10^6 <= arr[i] <= 10^6
 *
 *
 */

/**
 * @File    :   1200.最小绝对差.go
 * @Time    :   2022/07/04 15:44:33
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func minimumAbsDifference(arr []int) [][]int {
	sort.Ints(arr)
	ans := [][]int{}
	best, n := math.MaxInt32, len(arr)
	for i := 0; i < n-1; i++ {
		delta := arr[i+1] - arr[i]
		if delta < best {
			best = delta
			ans = [][]int{{arr[i], arr[i+1]}}
		} else if delta == best {
			ans = append(ans, []int{arr[i], arr[i+1]})
		}
	}
	return ans
}

// @lc code=end
