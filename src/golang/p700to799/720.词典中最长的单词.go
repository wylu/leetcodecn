package p700to799

import "sort"

/*
 * @lc app=leetcode.cn id=720 lang=golang
 *
 * [720] 词典中最长的单词
 *
 * https://leetcode-cn.com/problems/longest-word-in-dictionary/description/
 *
 * algorithms
 * Easy (49.54%)
 * Likes:    209
 * Dislikes: 0
 * Total Accepted:    29.1K
 * Total Submissions: 58.8K
 * Testcase Example:  '["w","wo","wor","worl","world"]'
 *
 * 给出一个字符串数组 words 组成的一本英语词典。返回 words 中最长的一个单词，该单词是由 words 词典中其他单词逐步添加一个字母组成。
 *
 * 若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：words = ["w","wo","wor","worl", "world"]
 * 输出："world"
 * 解释： 单词"world"可由"w", "wo", "wor", 和 "worl"逐步添加一个字母组成。
 *
 *
 * 示例 2：
 *
 *
 * 输入：words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
 * 输出："apple"
 * 解释："apply" 和 "apple" 都能由词典中的单词组成。但是 "apple" 的字典序小于 "apply"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= words.length <= 1000
 * 1 <= words[i].length <= 30
 * 所有输入的字符串 words[i] 都只包含小写字母。
 *
 *
 */

/**
 * @File    :   720.词典中最长的单词.go
 * @Time    :   2022/03/17 09:20:20
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：哈希集合
 * 思路和算法
 *
 * 定义「符合要求的单词」如下：
 *
 * 空字符串是符合要求的单词；
 *
 * 在符合要求的单词的末尾添加一个字母，得到的新单词是符合要求的单词。
 *
 * 这道题要求返回数组 words 中的最长的符合要求的单词，如果有多个最长的
 * 符合要求的单词则返回其中字典序最小的单词。以下将返回值称为「答案」。
 *
 * 为了方便处理，需要将数组 words 排序，排序的规则是首先按照单词的长度
 * 升序排序，如果单词的长度相同则按照字典序降序排序。排序之后，可以确保
 * 当遍历到每个单词时，比该单词短的全部单词都已经遍历过，且每次遇到符合
 * 要求的单词一定是最长且字典序最小的单词，可以直接更新答案。
 *
 * 将答案初始化为空字符串。使用哈希集合存储所有符合要求的单词，初始时
 * 将空字符串加入哈希集合。遍历数组 words，对于每个单词，判断当前单词
 * 去掉最后一个字母之后的前缀是否在哈希集合中，如果该前缀在哈希集合中
 * 则当前单词是符合要求的单词，将当前单词加入哈希集合，并将答案更新为
 * 当前单词。
 *
 * 遍历结束之后，返回答案。
 */

// @lc code=start
func longestWord(words []string) string {
	sort.Slice(words, func(i, j int) bool {
		return len(words[i]) < len(words[j]) || (len(words[i]) == len(words[j]) && words[i] > words[j])
	})

	ans := ""
	seen := map[string]bool{"": true}
	for _, word := range words {
		if seen[word[:len(word)-1]] {
			ans = word
			seen[word] = true
		}
	}

	return ans
}

// @lc code=end

// func longestWord(words []string) string {
// 	set := map[string]bool{}
// 	for _, word := range words {
// 		set[word] = true
// 	}

// 	sort.Strings(words)
// 	ans := ""
// 	for _, word := range words {
// 		if len(word) <= len(ans) {
// 			continue
// 		}

// 		flag := true
// 		for i, n := 1, len(word); i < n && flag; i++ {
// 			if !set[string(word[:i])] {
// 				flag = false
// 			}
// 		}

// 		if flag {
// 			ans = word
// 		}
// 	}

// 	return ans
// }
