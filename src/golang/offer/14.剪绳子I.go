package offer

import "math"

/**
 * @File    :   14.I剪绳子.go
 * @Time    :   2020/07/08 22:10:16
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
func cuttingRope(n int) int {
	if n <= 3 {
		return n - 1
	}

	cnt3 := n / 3
	n %= 3
	switch n {
	case 1:
		return int(math.Pow(3, float64(cnt3-1))) * 4
	case 2:
		return int(math.Pow(3, float64(cnt3))) * 2
	default:
		return int(math.Pow(3, float64(cnt3)))
	}
}
