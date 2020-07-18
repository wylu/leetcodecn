package p200to299

/*
 * @lc app=leetcode.cn id=211 lang=golang
 *
 * [211] 添加与搜索单词 - 数据结构设计
 *
 * https://leetcode-cn.com/problems/add-and-search-word-data-structure-design/description/
 *
 * algorithms
 * Medium (45.15%)
 * Likes:    137
 * Dislikes: 0
 * Total Accepted:    13K
 * Total Submissions: 28.6K
 * Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
  '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
 *
 * 设计一个支持以下两种操作的数据结构：
 *
 * void addWord(word)
 * bool search(word)
 *
 *
 * search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。
 *
 * 示例:
 *
 * addWord("bad")
 * addWord("dad")
 * addWord("mad")
 * search("pad") -> false
 * search("bad") -> true
 * search(".ad") -> true
 * search("b..") -> true
 *
 *
 * 说明:
 *
 * 你可以假设所有单词都是由小写字母 a-z 组成的。
 *
*/

/**
 * @File    :   211.添加与搜索单词-数据结构设计.go
 * @Time    :   2020/07/18 19:14:19
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
// @lc code=start

// Trie211 - Prifix Tree
type Trie211 struct {
	links [26]*Trie211
	isEnd bool
}

// WordDictionary - word dictionary
type WordDictionary struct {
	trie *Trie211
}

// Constructor211 - Initialize your data structure here.
func Constructor211() WordDictionary {
	return WordDictionary{
		trie: &Trie211{},
	}
}

// AddWord - Adds a word into the data structure.
func (wd *WordDictionary) AddWord(word string) {
	tr := wd.trie
	for i := 0; i < len(word); i++ {
		ch := word[i] - 'a'
		if tr.links[ch] == nil {
			tr.links[ch] = &Trie211{}
		}
		tr = tr.links[ch]
	}
	tr.isEnd = true
}

// Search - Returns if the word is in the data structure.
// A word could contain the dot character '.' to represent any one letter.
func (wd *WordDictionary) Search(word string) bool {
	return wd.trie.Search211(word, 0)
}

// Search211 - search a word
func (tr *Trie211) Search211(word string, k int) bool {
	for i := k; i < len(word); i++ {
		if word[i] == '.' {
			for j := 0; j < len(tr.links); j++ {
				if tr.links[j] != nil && tr.links[j].Search211(word, i+1) {
					return true
				}
			}
			return false
		}

		ch := word[i] - 'a'
		if tr.links[ch] == nil {
			return false
		}
		tr = tr.links[ch]
	}
	return tr.isEnd
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */
// @lc code=end

// // WordDictionary - word dictionary
// type WordDictionary struct {
// 	trie *Trie211
// }

// // Constructor211 - Initialize your data structure here.
// func Constructor211() WordDictionary {
// 	return WordDictionary{
// 		trie: &Trie211{},
// 	}
// }

// // AddWord - Adds a word into the data structure.
// func (wd *WordDictionary) AddWord(word string) {
// 	wd.trie.Insert211(word)
// }

// // Search - Returns if the word is in the data structure.
// // A word could contain the dot character '.' to represent any one letter.
// func (wd *WordDictionary) Search(word string) bool {
// 	return wd.trie.Search211(word)
// }

// // Trie211 - Prifix Tree
// type Trie211 struct {
// 	links [26]*Trie211
// 	isEnd bool
// }

// // Insert211 - insert a word
// func (tr *Trie211) Insert211(word string) {
// 	for i := 0; i < len(word); i++ {
// 		ch := word[i] - 'a'
// 		if tr.links[ch] == nil {
// 			tr.links[ch] = &Trie211{}
// 		}
// 		tr = tr.links[ch]
// 	}
// 	tr.isEnd = true
// }

// // Search211 - search a word
// func (tr *Trie211) Search211(word string) bool {
// 	for i := 0; i < len(word); i++ {
// 		if word[i] == '.' {
// 			flag := false
// 			for j := 0; j < len(tr.links) && !flag; j++ {
// 				if tr.links[j] == nil {
// 					continue
// 				}
// 				flag = tr.links[j].Search211(string(word[i+1:]))
// 			}
// 			return flag
// 		}

// 		ch := word[i] - 'a'
// 		if tr.links[ch] == nil {
// 			return false
// 		}
// 		tr = tr.links[ch]
// 	}
// 	return tr.isEnd
// }
