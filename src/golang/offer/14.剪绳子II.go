package offer

/**
 * @File    :   14.剪绳子II.go
 * @Time    :   2020/07/08 22:29:45
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
func cuttingRope2(n int) int {
	if n <= 3 {
		return n - 1
	}

	res, p := int64(1), int64(1000000007)
	for n > 4 {
		res = res * 3 % p
		n -= 3
	}
	return int(res * int64(n) % p)
}
