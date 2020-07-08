package offer

import "math"

/**
 * @File    :   17.打印从1到最大的n位数.go
 * @Time    :   2020/07/08 23:22:30
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
func printNumbers(n int) []int {
	res := make([]int, int(math.Pow10(n))-1)
	for i := 0; i < len(res); i++ {
		res[i] = i + 1
	}
	return res
}
