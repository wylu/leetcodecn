package offer

/**
 * @File    :   10.I斐波那契数列.go
 * @Time    :   2020/07/06 23:07:34
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
func fib(n int) int {
	mod := 1000000007
	f := [2]int{0, 1}
	if n < 2 {
		return f[n]
	}
	for i := 2; i <= n; i++ {
		f[0], f[1] = f[1], (f[0]+f[1])%mod
	}
	return f[1]
}
