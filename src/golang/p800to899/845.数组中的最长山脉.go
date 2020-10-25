package p800to899

/*
 * @lc app=leetcode.cn id=845 lang=golang
 *
 * [845] 数组中的最长山脉
 *
 * https://leetcode-cn.com/problems/longest-mountain-in-array/description/
 *
 * algorithms
 * Medium (36.53%)
 * Likes:    129
 * Dislikes: 0
 * Total Accepted:    21.5K
 * Total Submissions: 53.1K
 * Testcase Example:  '[2,1,4,7,3,2,5]'
 *
 * 我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
 *
 *
 * B.length >= 3
 * 存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... >
 * B[B.length - 1]
 *
 *
 * （注意：B 可以是 A 的任意子数组，包括整个数组 A。）
 *
 * 给出一个整数数组 A，返回最长 “山脉” 的长度。
 *
 * 如果不含有 “山脉” 则返回 0。
 *
 *
 *
 * 示例 1：
 *
 * 输入：[2,1,4,7,3,2,5]
 * 输出：5
 * 解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
 *
 *
 * 示例 2：
 *
 * 输入：[2,2,2]
 * 输出：0
 * 解释：不含 “山脉”。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= A.length <= 10000
 * 0 <= A[i] <= 10000
 *
 *
 */

/**
 * @File    :   845.数组中的最长山脉.go
 * @Time    :   2020/10/25 21:45:14
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func longestMountain(a []int) int {
	n := len(a)
	lts, rts := make([]int, n), make([]int, n)

	for i := 1; i < n; i++ {
		if a[i] > a[i-1] {
			lts[i] = lts[i-1] + 1
		}
	}
	for i := n - 2; i >= 0; i-- {
		if a[i] > a[i+1] {
			rts[i] = rts[i+1] + 1
		}
	}

	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	ans := 0
	for i := 1; i < n-1; i++ {
		if lts[i] > 0 && rts[i] > 0 {
			ans = max(ans, lts[i]+rts[i]+1)
		}
	}

	return ans
}

// @lc code=end
