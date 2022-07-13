package p700to799

/*
 * @lc app=leetcode.cn id=735 lang=golang
 *
 * [735] 行星碰撞
 *
 * https://leetcode.cn/problems/asteroid-collision/description/
 *
 * algorithms
 * Medium (42.73%)
 * Likes:    291
 * Dislikes: 0
 * Total Accepted:    43.4K
 * Total Submissions: 101.5K
 * Testcase Example:  '[5,10,-5]'
 *
 * 给定一个整数数组 asteroids，表示在同一行的行星。
 *
 * 对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。
 *
 *
 * 找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：asteroids = [5,10,-5]
 * 输出：[5,10]
 * 解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。
 *
 * 示例 2：
 *
 *
 * 输入：asteroids = [8,-8]
 * 输出：[]
 * 解释：8 和 -8 碰撞后，两者都发生爆炸。
 *
 * 示例 3：
 *
 *
 * 输入：asteroids = [10,2,-5]
 * 输出：[10]
 * 解释：2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= asteroids.length <= 10^4
 * -1000 <= asteroids[i] <= 1000
 * asteroids[i] != 0
 *
 *
 */

/**
 * @File    :   735.行星碰撞.go
 * @Time    :   2022/07/13 12:58:34
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func asteroidCollision(asteroids []int) []int {
	stk := []int{}
	for _, aster := range asteroids {
		alive := true
		for alive && aster < 0 && len(stk) > 0 && stk[len(stk)-1] > 0 {
			alive = stk[len(stk)-1] < -aster
			if stk[len(stk)-1] <= -aster {
				stk = stk[:len(stk)-1]
			}
		}
		if alive {
			stk = append(stk, aster)
		}
	}
	return stk
}

// @lc code=end

// func asteroidCollision(asteroids []int) []int {
// 	stk := []int{}
// 	for _, v := range asteroids {
// 		n := len(stk)
// 		if n == 0 || !(stk[n-1] > 0 && v < 0) {
// 			stk = append(stk, v)
// 			continue
// 		}

// 		for n > 0 && stk[n-1]*v < 0 && stk[n-1] < -v {
// 			stk = stk[:n-1]
// 			n--
// 		}

// 		if n == 0 || stk[n-1] < 0 {
// 			stk = append(stk, v)
// 		} else if stk[n-1] == -v {
// 			stk = stk[:n-1]
// 		}
// 	}
// 	return stk
// }
