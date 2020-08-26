package p600to699

import "math"

/*
 * @lc app=leetcode.cn id=679 lang=golang
 *
 * [679] 24 点游戏
 *
 * https://leetcode-cn.com/problems/24-game/description/
 *
 * algorithms
 * Hard (44.76%)
 * Likes:    199
 * Dislikes: 0
 * Total Accepted:    14.8K
 * Total Submissions: 27.8K
 * Testcase Example:  '[4,1,8,7]'
 *
 * 你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。
 *
 * 示例 1:
 *
 * 输入: [4, 1, 8, 7]
 * 输出: True
 * 解释: (8-4) * (7-1) = 24
 *
 *
 * 示例 2:
 *
 * 输入: [1, 2, 1, 2]
 * 输出: False
 *
 *
 * 注意:
 *
 *
 * 除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
 * 每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1
 * 是不允许的。
 * 你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。
 *
 *
 */

/**
 * @File    :   679.24-点游戏.go
 * @Time    :   2020/08/26 22:52:21
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func judgePoint24(nums []int) bool {
	if len(nums) == 0 {
		return false
	}

	newNums := make([]float64, len(nums))
	for i := 0; i < len(nums); i++ {
		newNums[i] = float64(nums[i])
	}
	return dfs679(newNums)
}

func dfs679(nums []float64) bool {
	EPSILON := 1e-6
	if len(nums) == 1 {
		return math.Abs(nums[0]-24) < EPSILON
	}

	for i, x := range nums {
		for j, y := range nums {
			if i == j {
				continue
			}

			newNums := []float64{}
			for k, z := range nums {
				if k != i && k != j {
					newNums = append(newNums, z)
				}
			}

			for op := 0; op < 4; op++ {
				if op < 2 && i > j {
					continue
				}

				if op == 0 {
					newNums = append(newNums, x+y)
				} else if op == 1 {
					newNums = append(newNums, x*y)
				} else if op == 2 {
					newNums = append(newNums, x-y)
				} else if op == 3 {
					if math.Abs(y) < EPSILON {
						continue
					}
					newNums = append(newNums, x/y)
				}

				if dfs679(newNums) {
					return true
				}
				newNums = newNums[:len(newNums)-1]
			}
		}
	}

	return false
}

// @lc code=end
