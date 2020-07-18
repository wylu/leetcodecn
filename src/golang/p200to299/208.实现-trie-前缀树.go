package p200to299

/*
 * @lc app=leetcode.cn id=208 lang=golang
 *
 * [208] 实现 Trie (前缀树)
 *
 * https://leetcode-cn.com/problems/implement-trie-prefix-tree/description/
 *
 * algorithms
 * Medium (67.63%)
 * Likes:    349
 * Dislikes: 0
 * Total Accepted:    44.9K
 * Total Submissions: 66.1K
 * Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
 *
 * 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
 *
 * 示例:
 *
 * Trie trie = new Trie();
 *
 * trie.insert("apple");
 * trie.search("apple");   // 返回 true
 * trie.search("app");     // 返回 false
 * trie.startsWith("app"); // 返回 true
 * trie.insert("app");
 * trie.search("app");     // 返回 true
 *
 * 说明:
 *
 *
 * 你可以假设所有的输入都是由小写字母 a-z 构成的。
 * 保证所有输入均为非空字符串。
 *
 *
*/

/**
 * @File    :   208.实现-trie-前缀树.go
 * @Time    :   2020/07/18 18:44:03
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start

// Trie - Prefix Tree
type Trie struct {
	links [26]*Trie
	isEnd bool
}

// Constructor - Initialize your data structure here.
func Constructor() Trie {
	return Trie{}
}

// Insert - Inserts a word into the trie.
func (tr *Trie) Insert(word string) {
	for i := 0; i < len(word); i++ {
		ch := word[i] - 'a'
		if tr.links[ch] == nil {
			tr.links[ch] = &Trie{}
		}
		tr = tr.links[ch]
	}
	tr.isEnd = true
}

// Search - Returns if the word is in the trie.
func (tr *Trie) Search(word string) bool {
	for i := 0; i < len(word); i++ {
		ch := word[i] - 'a'
		if tr.links[ch] == nil {
			return false
		}
		tr = tr.links[ch]
	}
	return tr.isEnd
}

// StartsWith - Returns if there is any word in the trie that starts with the given prefix.
func (tr *Trie) StartsWith(prefix string) bool {
	for i := 0; i < len(prefix); i++ {
		ch := prefix[i] - 'a'
		if tr.links[ch] == nil {
			return false
		}
		tr = tr.links[ch]
	}
	return true
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
// @lc code=end
