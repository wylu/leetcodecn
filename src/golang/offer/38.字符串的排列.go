package offer

/**
 * @File    :   38.字符串的排列.go
 * @Time    :   2021/06/22 08:53:20
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

func permutation(s string) []string {
	n := len(s)
	ans := []string{}
	seq := []byte(s)

	var dfs func(cur int)
	dfs = func(cur int) {
		if cur == n {
			ans = append(ans, string(seq))
			return
		}
		seen := map[byte]bool{}
		for i := cur; i < n; i++ {
			if seen[seq[i]] {
				continue
			}
			seen[seq[i]] = true
			seq[cur], seq[i] = seq[i], seq[cur]
			dfs(cur + 1)
			seq[cur], seq[i] = seq[i], seq[cur]
		}
	}

	dfs(0)
	return ans
}
