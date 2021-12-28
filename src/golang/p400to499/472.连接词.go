package p400to499

import "sort"

/*
 * @lc app=leetcode.cn id=472 lang=golang
 *
 * [472] 连接词
 *
 * https://leetcode-cn.com/problems/concatenated-words/description/
 *
 * algorithms
 * Hard (38.92%)
 * Likes:    172
 * Dislikes: 0
 * Total Accepted:    12.8K
 * Total Submissions: 28.2K
 * Testcase Example:  '["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]'
 *
 * 给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。
 *
 * 连接词 定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：words =
 * ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
 * 输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
 * 解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成;
 * ⁠    "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成;
 * ⁠    "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。
 *
 *
 * 示例 2：
 *
 *
 * 输入：words = ["cat","dog","catdog"]
 * 输出：["catdog"]
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= words.length <= 10^4
 * 0 <= words[i].length <= 1000
 * words[i] 仅由小写字母组成
 * 0 <= sum(words[i].length) <= 10^5
 *
 *
 */

/**
 * @File    :   472.连接词.go
 * @Time    :   2021/12/28 14:20:35
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：字典树 + 深度优先搜索
 *
 * 判断一个单词是不是连接词，需要判断这个单词是否完全由至少两个给定数组
 * 中的更短的非空单词（可以重复）组成。判断更短的单词是否在给定数组中，
 * 可以使用字典树实现。
 *
 * 为了方便处理，首先将数组 words 按照字符串的长度递增的顺序排序，排序后
 * 可以确保当遍历到任意单词时，比该单词短的单词一定都已经遍历过，因此可以
 * 根据已经遍历过的全部单词判断当前单词是不是连接词。
 *
 * 在将数组 words 排序之后，遍历数组，跳过空字符串，对于每个非空单词，
 * 判断该单词是不是连接词，如果是连接词则将该单词加入结果数组，如果不是
 * 连接词则将该单词加入字典树。
 *
 * 判断一个单词是不是连接词的做法是在字典树中深度优先搜索。从该单词的
 * 第一个字符（即下标 0 处的字符）开始，在字典树中依次搜索每个字符对应的
 * 结点，可能有以下几种情况：
 *
 *   - 如果一个字符对应的结点是单词的结尾，则找到了一个更短的单词，从该
 *     字符的后一个字符开始搜索下一个更短的单词；
 *
 *   - 如果一个字符对应的结点在字典树中不存在，则当前的搜索结果失败，
 *     回到上一个单词的结尾继续搜索。
 *
 * 如果找到一个更短的单词且这个更短的单词的最后一个字符是当前单词的最后
 * 一个字符，则当前单词是连接词。由于数组 words 中没有重复的单词，因此
 * 在判断一个单词是不是连接词时，该单词一定没有加入字典树，由此可以确保
 * 判断连接词的条件成立。
 *
 * 由于一个连接词由多个更短的非空单词组成，如果存在一个较长的连接词的
 * 组成部分之一是一个较短的连接词，则一定可以将这个较短的连接词换成多个
 * 更短的非空单词，因此不需要将连接词加入字典树。
 */

// @lc code=start
type tire472 struct {
	children [26]*tire472
	end      bool
}

func (t *tire472) insert(word string) {
	node := t
	for _, ch := range word {
		idx := ch - 'a'
		if node.children[idx] == nil {
			node.children[idx] = &tire472{}
		}
		node = node.children[idx]
	}
	node.end = true
}

func (t *tire472) search(word string) bool {
	if word == "" {
		return true
	}

	node := t
	for i, ch := range word {
		node = node.children[ch-'a']
		if node == nil {
			return false
		}
		if node.end && t.search(word[i+1:]) {
			return true
		}
	}

	return false
}

func findAllConcatenatedWordsInADict(words []string) []string {
	sort.Slice(words, func(i, j int) bool { return len(words[i]) < len(words[j]) })

	tire := &tire472{}
	ans := []string{}
	for _, word := range words {
		if word == "" {
			continue
		}

		if tire.search(word) {
			ans = append(ans, word)
		} else {
			tire.insert(word)
		}
	}

	return ans
}

// @lc code=end
