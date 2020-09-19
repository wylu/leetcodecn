package lcp

/**
 * @File    :   19.秋叶收藏集.go
 * @Time    :   2020/09/19 10:52:39
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Dynamic Programming
 *
 * State:
 *   f[i][0]: 表示将前 i 个字符变成形如 'r...' 的形式需要的最小调整次数
 *   f[i][1]: 表示将前 i 个字符变成形如 'r...y...' 的形式需要的最小调整次数
 *   f[i][2]: 表示将前 i 个字符变成形如 'r...y...r...' 的形式需要的最小调整次数
 */

func minimumOperations(leaves string) int {
	n := len(leaves)
	f := make([][3]int, n)
	if leaves[0] == 'y' {
		f[0][0] = 1
	}

	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	for i := 1; i < n; i++ {
		r, y := 0, 0
		if leaves[i] == 'r' {
			y = 1
		} else {
			r = 1
		}

		f[i][0] = f[i-1][0] + r
		f[i][1] = f[i-1][0] + y

		if i > 1 {
			f[i][1] = min(f[i][1], f[i-1][1]+y)
			f[i][2] = f[i-1][1] + r
		}

		if i > 2 {
			f[i][2] = min(f[i][2], f[i-1][2]+r)
		}
	}

	return f[n-1][2]
}
