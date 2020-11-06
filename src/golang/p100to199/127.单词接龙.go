package p100to199

/*
 * @lc app=leetcode.cn id=127 lang=golang
 *
 * [127] 单词接龙
 *
 * https://leetcode-cn.com/problems/word-ladder/description/
 *
 * algorithms
 * Medium (44.01%)
 * Likes:    559
 * Dislikes: 0
 * Total Accepted:    72.2K
 * Total Submissions: 162K
 * Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
 *
 * 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
 * 的最短转换序列的长度。转换需遵循如下规则：
 *
 *
 * 每次转换只能改变一个字母。
 * 转换过程中的中间单词必须是字典中的单词。
 *
 *
 * 说明:
 *
 *
 * 如果不存在这样的转换序列，返回 0。
 * 所有单词具有相同的长度。
 * 所有单词只由小写字母组成。
 * 字典中不存在重复的单词。
 * 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
 *
 *
 * 示例 1:
 *
 * 输入:
 * beginWord = "hit",
 * endWord = "cog",
 * wordList = ["hot","dot","dog","lot","log","cog"]
 *
 * 输出: 5
 *
 * 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
 * ⁠    返回它的长度 5。
 *
 *
 * 示例 2:
 *
 * 输入:
 * beginWord = "hit"
 * endWord = "cog"
 * wordList = ["hot","dot","dog","lot","log"]
 *
 * 输出: 0
 *
 * 解释: endWord "cog" 不在字典中，所以无法进行转换。
 *
 */

/**
 * @File    :   127.单词接龙.go
 * @Time    :   2020/11/06 13:41:14
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func ladderLength(beginWord string, endWord string, wordList []string) int {
	word2id := map[string]int{}
	graph := map[int][]int{}
	nodeNum := 0

	addWord := func(word string) int {
		if _, ok := word2id[word]; !ok {
			word2id[word] = nodeNum
			graph[nodeNum] = []int{}
			nodeNum++
		}
		return word2id[word]
	}

	addEdge := func(word string) {
		u := addWord(word)
		s := []byte(word)
		for i := 0; i < len(s); i++ {
			tmp := s[i]
			s[i] = '*'
			v := addWord(string(s))
			graph[u] = append(graph[u], v)
			graph[v] = append(graph[v], u)
			s[i] = tmp
		}
	}

	for _, word := range wordList {
		addEdge(word)
	}

	addEdge(beginWord)
	if _, ok := word2id[endWord]; !ok {
		return 0
	}

	dist := 0
	visit := map[int]bool{}
	begin, end := word2id[beginWord], word2id[endWord]
	que := []int{begin}

	for len(que) > 0 {
		size := len(que)
		for i := 0; i < size; i++ {
			u := que[0]
			que = que[1:]
			visit[u] = true
			if u == end {
				return dist/2 + 1
			}

			for _, v := range graph[u] {
				if !visit[v] {
					que = append(que, v)
				}
			}
		}
		dist++
	}

	return 0
}

// @lc code=end
