package offer

/**
 * @File    :   114.外星文字典.go
 * @Time    :   2022/05/31 15:53:19
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

func alienOrder(words []string) string {
	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	graph := map[byte][]byte{}
	for _, word := range words {
		for _, ch := range word {
			if _, ok := graph[byte(ch)]; !ok {
				graph[byte(ch)] = []byte{}
			}
		}
	}

	n := len(words)
	indegrees := map[byte]int{}
	for i := 1; i < n; i++ {
		w1, w2 := words[i-1], words[i]
		s1, s2 := len(w1), len(w2)
		sz := min(s1, s2)

		j := 0
		for ; j < sz; j++ {
			if w1[j] != w2[j] {
				graph[byte(w1[j])] = append(graph[byte(w1[j])], byte(w2[j]))
				indegrees[byte(w2[j])]++
				break
			}
		}

		if j == sz && s1 > s2 {
			return ""
		}
	}

	que := []byte{}
	for k := range graph {
		if indegrees[k] == 0 {
			que = append(que, k)
		}
	}

	ts := []byte{}
	for len(que) > 0 {
		sz := len(que)
		for i := 0; i < sz; i++ {
			u := que[0]
			que = que[1:]
			ts = append(ts, u)

			for _, v := range graph[u] {
				indegrees[v]--
				if indegrees[v] == 0 {
					que = append(que, v)
				}
			}
		}
	}

	if len(ts) != len(graph) {
		return ""
	}
	return string(ts)
}
