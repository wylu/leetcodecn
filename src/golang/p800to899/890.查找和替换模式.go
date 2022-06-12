package p800to899

/*
 * @lc app=leetcode.cn id=890 lang=golang
 *
 * [890] 查找和替换模式
 *
 * https://leetcode.cn/problems/find-and-replace-pattern/description/
 *
 * algorithms
 * Medium (76.11%)
 * Likes:    145
 * Dislikes: 0
 * Total Accepted:    14.3K
 * Total Submissions: 18.8K
 * Testcase Example:  '["abc","deq","mee","aqq","dkd","ccc"]\n"abb"'
 *
 * 你有一个单词列表 words 和一个模式  pattern，你想知道 words 中的哪些单词与模式匹配。
 *
 * 如果存在字母的排列 p ，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。
 *
 * （回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）
 *
 * 返回 words 中与给定模式匹配的单词列表。
 *
 * 你可以按任何顺序返回答案。
 *
 *
 *
 * 示例：
 *
 * 输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
 * 输出：["mee","aqq"]
 * 解释：
 * "mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
 * "ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
 * 因为 a 和 b 映射到同一个字母。
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= words.length <= 50
 * 1 <= pattern.length = words[i].length <= 20
 *
 *
 */

/**
 * @File    :   890.查找和替换模式.go
 * @Time    :   2022/06/12 10:12:18
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findAndReplacePattern(words []string, pattern string) []string {
	n := len(pattern)
	ans := []string{}
	for _, word := range words {
		flag := true
		mapping := map[byte]byte{}
		used := [26]bool{}
		for i := 0; i < n; i++ {
			if _, ok := mapping[word[i]]; !ok {
				if used[pattern[i]-'a'] {
					flag = false
					break
				}

				mapping[word[i]] = pattern[i]
				used[pattern[i]-'a'] = true
				continue
			}

			if mapping[word[i]] != pattern[i] {
				flag = false
				break
			}
		}

		if flag {
			ans = append(ans, word)
		}
	}
	return ans
}

// @lc code=end
