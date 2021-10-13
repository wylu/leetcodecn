package p400to499

import "strconv"

/*
 * @lc app=leetcode.cn id=412 lang=golang
 *
 * [412] Fizz Buzz
 *
 * https://leetcode-cn.com/problems/fizz-buzz/description/
 *
 * algorithms
 * Easy (68.77%)
 * Likes:    121
 * Dislikes: 0
 * Total Accepted:    82.5K
 * Total Submissions: 120K
 * Testcase Example:  '3'
 *
 * 写一个程序，输出从 1 到 n 数字的字符串表示。
 *
 * 1. 如果 n 是3的倍数，输出“Fizz”；
 *
 * 2. 如果 n 是5的倍数，输出“Buzz”；
 *
 * 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
 *
 * 示例：
 *
 * n = 15,
 *
 * 返回:
 * [
 * ⁠   "1",
 * ⁠   "2",
 * ⁠   "Fizz",
 * ⁠   "4",
 * ⁠   "Buzz",
 * ⁠   "Fizz",
 * ⁠   "7",
 * ⁠   "8",
 * ⁠   "Fizz",
 * ⁠   "Buzz",
 * ⁠   "11",
 * ⁠   "Fizz",
 * ⁠   "13",
 * ⁠   "14",
 * ⁠   "FizzBuzz"
 * ]
 *
 *
 */

/**
 * @File    :   412.fizz-buzz.go
 * @Time    :   2021/10/13 13:03:42
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func fizzBuzz(n int) []string {
	ans := make([]string, 0, n)
	for i := 1; i <= n; i++ {
		cur := strconv.Itoa(i)
		if i%3 == 0 && i%5 == 0 {
			cur = "FizzBuzz"
		} else if i%3 == 0 {
			cur = "Fizz"
		} else if i%5 == 0 {
			cur = "Buzz"
		}
		ans = append(ans, cur)
	}
	return ans
}

// @lc code=end
