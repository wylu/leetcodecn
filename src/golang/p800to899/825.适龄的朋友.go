package p800to899

/*
 * @lc app=leetcode.cn id=825 lang=golang
 *
 * [825] 适龄的朋友
 *
 * https://leetcode-cn.com/problems/friends-of-appropriate-ages/description/
 *
 * algorithms
 * Medium (44.41%)
 * Likes:    149
 * Dislikes: 0
 * Total Accepted:    25.3K
 * Total Submissions: 57.1K
 * Testcase Example:  '[16,16]'
 *
 * 在社交媒体网站上有 n 个用户。给你一个整数数组 ages ，其中 ages[i] 是第 i 个用户的年龄。
 *
 * 如果下述任意一个条件为真，那么用户 x 将不会向用户 y（x != y）发送好友请求：
 *
 *
 * age[y] <= 0.5 * age[x] + 7
 * age[y] > age[x]
 * age[y] > 100 && age[x] < 100
 *
 *
 * 否则，x 将会向 y 发送一条好友请求。
 *
 * 注意，如果 x 向 y 发送一条好友请求，y 不必也向 x 发送一条好友请求。另外，用户不会向自己发送好友请求。
 *
 * 返回在该社交媒体网站上产生的好友请求总数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：ages = [16,16]
 * 输出：2
 * 解释：2 人互发好友请求。
 *
 *
 * 示例 2：
 *
 *
 * 输入：ages = [16,17,18]
 * 输出：2
 * 解释：产生的好友请求为 17 -> 16 ，18 -> 17 。
 *
 *
 * 示例 3：
 *
 *
 * 输入：ages = [20,30,100,110,120]
 * 输出：3
 * 解释：产生的好友请求为 110 -> 100 ，120 -> 110 ，120 -> 100 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == ages.length
 * 1 <= n <= 2 * 10^4
 * 1 <= ages[i] <= 120
 *
 *
 */

/**
 * @File    :   825.适龄的朋友.go
 * @Time    :   2021/12/27 21:20:46
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func numFriendRequests(ages []int) int {
	ps, cnt := [121]int{}, [121]int{}
	for _, age := range ages {
		cnt[age]++
	}
	for i := 1; i < 121; i++ {
		ps[i] = ps[i-1] + cnt[i]
	}

	ans := 0
	for x := 15; x <= 120; x++ {
		if cnt[x] > 0 {
			bound := x/2 + 8
			ans += cnt[x] * (ps[x] - ps[bound-1] - 1)
		}
	}

	return ans
}

// @lc code=end

// func numFriendRequests(ages []int) int {
// 	counters := [125]int{}
// 	for _, age := range ages {
// 		counters[age]++
// 	}

// 	ans := 0
// 	for x := 15; x <= 120; x++ {
// 		if counters[x] == 0 {
// 			continue
// 		}

// 		ans += (counters[x] - 1) * counters[x]
// 		for y := x/2 + 8; y <= x; y++ {
// 			if y > 100 && x < 100 {
// 				break
// 			}
// 			if x != y {
// 				ans += counters[x] * counters[y]
// 			}
// 		}
// 	}

// 	return ans
// }
