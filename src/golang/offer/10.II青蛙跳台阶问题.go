package offer

/**
 * @File    :   10.II青蛙跳台阶问题.go
 * @Time    :   2020/07/06 23:13:17
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
func numWays(n int) int {
	MOD := 1000000007
	f := []int{1, 1}
	if n < 2 {
		return f[n]
	}
	for i := 2; i <= n; i++ {
		f[0], f[1] = f[1], (f[0]+f[1])%MOD
	}
	return f[1]
}
