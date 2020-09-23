package p900to999

/*
 * @lc app=leetcode.cn id=930 lang=golang
 *
 * [930] 和相同的二元子数组
 *
 * https://leetcode-cn.com/problems/binary-subarrays-with-sum/description/
 *
 * algorithms
 * Medium (37.74%)
 * Likes:    60
 * Dislikes: 0
 * Total Accepted:    4.3K
 * Total Submissions: 11.4K
 * Testcase Example:  '[1,0,1,0,1]\n2'
 *
 * 在由若干 0 和 1  组成的数组 A 中，有多少个和为 S 的非空子数组。
 *
 *
 *
 * 示例：
 *
 * 输入：A = [1,0,1,0,1], S = 2
 * 输出：4
 * 解释：
 * 如下面黑体所示，有 4 个满足题目要求的子数组：
 * [1,0,1,0,1]
 * [1,0,1,0,1]
 * [1,0,1,0,1]
 * [1,0,1,0,1]
 *
 *
 *
 *
 * 提示：
 *
 *
 * A.length <= 30000
 * 0 <= S <= A.length
 * A[i] 为 0 或 1
 *
 *
 */

/**
 * @File    :   930.和相同的二元子数组.go
 * @Time    :   2020/09/23 09:39:00
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :   前缀和 + 哈希表
 */

// @lc code=start
func numSubarraysWithSum(A []int, S int) int {
	n := len(A)
	ps := make([]int, n+1)
	for i := 0; i < n; i++ {
		ps[i+1] = ps[i] + A[i]
	}

	ans := 0
	mp := map[int]int{}
	mp[0] = 1
	for i := 1; i <= n; i++ {
		ans += mp[ps[i]-S]
		mp[ps[i]]++
	}

	return ans
}

// @lc code=end
