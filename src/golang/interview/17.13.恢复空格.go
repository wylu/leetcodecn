package interview

/**
 * @File    :   17.13.恢复空格.go
 * @Time    :   2020/07/09 21:48:28
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Trie + Dynamic Programming
 *
 * State:
 *   dp[i]: 表示s[0:i]（不包含s[i]）的最少的未识别的字符数量
 *
 * Initial State:
 *   dp[0] = 0
 *   dp[i] = dp[i-1] + 1, 1 <= i <= n
 *
 * State Transition:
 *   如果 s[j:i] 在词典中（可以选择将其视为一个单词或视为未识别字符序列）:
 *     dp[i] = min(dp[i], dp[j])
 *   否则，可以复用 dp[i−1] 的状态再加上当前未被识别的 s[i-1] (第 i 个字符):
 *     dp[i] = dp[i-1] + 1
 *
 * Optimization:
 *   计算 dp[i] 时，需要用 j 来遍历前 i 个字符，逐个判断以 s[j] 为开头，
 *   以第 i 个字符（也即 s[i-1]）为结尾的字符串是否在字典中。这一步可以利用
 *   字典树来加速，通过字典树我们可以查询以第 i 个字符为结尾的单词有哪些
 *  （构建字典树时将单词逆序插入即可）。
 */
func respace(dictionary []string, sentence string) int {
	// 构建字典树
	trie := &Trie{}
	for _, word := range dictionary {
		trie.insert(word)
	}

	n := len(sentence)
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = dp[i-1] + 1
		for cur, j := trie, i-1; j >= 0; j-- {
			c := sentence[j] - 'a'
			if cur.children[c] == nil {
				break
			}
			cur = cur.children[c]
			if cur.isWord {
				dp[i] = min1713(dp[i], dp[j])
			}
		}
	}
	return dp[n]
}

func min1713(x, y int) int {
	if x < y {
		return x
	}
	return y
}

// Trie - Prefix Tree
type Trie struct {
	children [26]*Trie
	isWord   bool
}

// 将单词倒序插入字典树
func (root *Trie) insert(s string) {
	cur := root
	for i := len(s) - 1; i >= 0; i-- {
		c := s[i] - 'a'
		if cur.children[c] == nil {
			cur.children[c] = &Trie{}
		}
		cur = cur.children[c]
	}
	cur.isWord = true
}

/*
 * Dynamic Programming
 *
 * State:
 *   dp[i]: 表示前i个字符(即s[0:i])最少的未识别的字符数量
 *
 * Initial State:
 *   dp[0] = 0
 *   dp[i] = dp[i-1] + 1, 1 <= i <= n
 *
 * State Transition:
 *   每次转移时，考虑 s[j] 到 s[i-1] 组成的子串（即 sentence[j:i]）是否能在词典
 *   中找到，如果能找到:
 *     dp[i] = min(dp[i], dp[j])
 *   否则，可以复用 dp[i−1] 的状态再加上当前未被识别的 s[i-1] (第 i 个字符)，
 *   此时有:
 *     dp[i] = dp[i-1] + 1
 */
// func respace(dictionary []string, sentence string) int {
// 	dict := make(map[string]bool, len(dictionary))
// 	for _, word := range dictionary {
// 		dict[word] = true
// 	}

// 	st, n := []byte(sentence), len(sentence)
// 	dp := make([]int, n+1)
// 	for i := 1; i <= n; i++ {
// 		dp[i] = dp[i-1] + 1
// 		for j := 0; j < i; j++ {
// 			key := string(st[j:i])
// 			if _, ok := dict[key]; ok {
// 				dp[i] = min1713(dp[i], dp[j])
// 			}
// 		}
// 	}
// 	return dp[n]
// }

// func min1713(x, y int) int {
// 	if x < y {
// 		return x
// 	}
// 	return y
// }
