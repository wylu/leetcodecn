package week198

/**
 * @File    :   5465.子树中标签相同的节点数.go
 * @Time    :   2020/07/19 10:46:51
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :   https://leetcode-cn.com/contest/weekly-contest-198/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
 */
func countSubTrees(n int, edges [][]int, labels string) []int {
	v := make([][]int, n)
	for _, e := range edges {
		if v[e[0]] == nil {
			v[e[0]] = []int{}
		}
		v[e[0]] = append(v[e[0]], e[1])
		v[e[1]] = append(v[e[1]], e[0])
	}

	c := make([][26]int, n)
	res := make([]int, n)
	dfs(0, -1, v, labels, &c, &res)
	return res
}

func dfs(x int, pre int, v [][]int, labels string, c *[][26]int, res *[]int) {
	(*c)[x][labels[x]-'a']++
	for _, y := range v[x] {
		if y == pre {
			continue
		}
		dfs(y, x, v, labels, c, res)
		for i := 0; i < 26; i++ {
			(*c)[x][i] += (*c)[y][i]
		}
	}
	(*res)[x] = (*c)[x][labels[x]-'a']
}
