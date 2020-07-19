package week198

/**
 * @File    :   5464.换酒问题.go
 * @Time    :   2020/07/19 10:32:59
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :   https://leetcode-cn.com/contest/weekly-contest-198/problems/water-bottles/
 */
func numWaterBottles(bottles int, exchange int) int {
	res := bottles
	for bottles >= exchange {
		ex := bottles / exchange
		res += bottles / exchange
		bottles = ex + bottles%exchange
	}
	return res
}
