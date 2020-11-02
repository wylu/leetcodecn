package p100to199

import "strings"

/*
 * @lc app=leetcode.cn id=140 lang=golang
 *
 * [140] 单词拆分 II
 *
 * https://leetcode-cn.com/problems/word-break-ii/description/
 *
 * algorithms
 * Hard (42.44%)
 * Likes:    331
 * Dislikes: 0
 * Total Accepted:    31.6K
 * Total Submissions: 74.6K
 * Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
 *
 * 给定一个非空字符串 s 和一个包含非空单词列表的字典
 * wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
 *
 * 说明：
 *
 *
 * 分隔时可以重复使用字典中的单词。
 * 你可以假设字典中没有重复的单词。
 *
 *
 * 示例 1：
 *
 * 输入:
 * s = "catsanddog"
 * wordDict = ["cat", "cats", "and", "sand", "dog"]
 * 输出:
 * [
 * "cats and dog",
 * "cat sand dog"
 * ]
 *
 *
 * 示例 2：
 *
 * 输入:
 * s = "pineapplepenapple"
 * wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
 * 输出:
 * [
 * "pine apple pen apple",
 * "pineapple pen apple",
 * "pine applepen apple"
 * ]
 * 解释: 注意你可以重复使用字典中的单词。
 *
 *
 * 示例 3：
 *
 * 输入:
 * s = "catsandog"
 * wordDict = ["cats", "dog", "sand", "and", "cat"]
 * 输出:
 * []
 *
 *
 */

/**
 * @File    :   140.单词拆分-ii.go
 * @Time    :   2020/11/02 21:55:50
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func wordBreak(s string, wordDict []string) []string {
	wordSet := map[string]bool{}
	for _, word := range wordDict {
		wordSet[word] = true
	}

	n := len(s)
	cache := map[int][][]string{}

	var traceback func(cur int) [][]string
	traceback = func(cur int) [][]string {
		if _, ok := cache[cur]; ok {
			return cache[cur]
		}
		if cur == n {
			return [][]string{{}}
		}

		sts := [][]string{}
		for i := cur + 1; i <= n; i++ {
			word := s[cur:i]
			if _, ok := wordSet[word]; ok {
				for _, sentence := range traceback(i) {
					// reversed sentence
					rst := make([]string, len(sentence))
					copy(rst, sentence)
					rst = append(rst, word)
					sts = append(sts, rst)
				}
			}
		}

		cache[cur] = sts
		return sts
	}

	reverse := func(sentence *[]string) {
		for i, j := 0, len(*sentence)-1; i < j; i, j = i+1, j-1 {
			(*sentence)[i], (*sentence)[j] = (*sentence)[j], (*sentence)[i]
		}
	}

	ans := []string{}
	for _, sentence := range traceback(0) {
		reverse(&sentence)
		ans = append(ans, strings.Join(sentence, " "))
	}
	return ans
}

// @lc code=end
