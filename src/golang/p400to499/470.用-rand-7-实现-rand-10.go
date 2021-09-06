package p400to499

import "math/rand"

/*
 * @lc app=leetcode.cn id=470 lang=golang
 *
 * [470] 用 Rand7() 实现 Rand10()
 *
 * https://leetcode-cn.com/problems/implement-rand10-using-rand7/description/
 *
 * algorithms
 * Medium (54.51%)
 * Likes:    287
 * Dislikes: 0
 * Total Accepted:    51.5K
 * Total Submissions: 94.4K
 * Testcase Example:  '1'
 *
 * 已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。
 *
 * 不要使用系统的 Math.random() 方法。
 *
 *
 *
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: 1
 * 输出: [7]
 *
 *
 * 示例 2:
 *
 *
 * 输入: 2
 * 输出: [8,4]
 *
 *
 * 示例 3:
 *
 *
 * 输入: 3
 * 输出: [8,1,10]
 *
 *
 *
 *
 * 提示:
 *
 *
 * rand7 已定义。
 * 传入参数: n 表示 rand10 的调用次数。
 *
 *
 *
 *
 * 进阶:
 *
 *
 * rand7()调用次数的 期望值 是多少 ?
 * 你能否尽量少调用 rand7() ?
 *
 *
 */

/**
 * @File    :   470.用-rand-7-实现-rand-10.go
 * @Time    :   2021/09/05 19:45:17
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

func rand7() int {
	return rand.Intn(7) + 1
}

// @lc code=start
func rand10() int {
	for {
		row := rand7()
		col := rand7()
		idx := (row-1)*7 + col
		if idx <= 40 {
			return 1 + (idx-1)%10
		}
	}
}

// @lc code=end
