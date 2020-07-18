package p200to299

/*
 * @lc app=leetcode.cn id=212 lang=golang
 *
 * [212] 单词搜索 II
 *
 * https://leetcode-cn.com/problems/word-search-ii/description/
 *
 * algorithms
 * Hard (41.25%)
 * Likes:    196
 * Dislikes: 0
 * Total Accepted:    17K
 * Total Submissions: 41K
 * Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
  '["oath","pea","eat","rain"]'
 *
 * 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
 *
 *
 * 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
 *
 * 示例:
 *
 * 输入:
 * words = ["oath","pea","eat","rain"] and board =
 * [
 * ⁠ ['o','a','a','n'],
 * ⁠ ['e','t','a','e'],
 * ⁠ ['i','h','k','r'],
 * ⁠ ['i','f','l','v']
 * ]
 *
 * 输出: ["eat","oath"]
 *
 * 说明:
 * 你可以假设所有输入都由小写字母 a-z 组成。
 *
 * 提示:
 *
 *
 * 你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
 * 如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？
 * 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
 *
 *
*/

/**
 * @File    :   212.单词搜索-ii.go
 * @Time    :   2020/07/18 21:43:59
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
// @lc code=start
func findWords(board [][]byte, words []string) []string {
	trie := Trie212{}
	for _, word := range words {
		trie.Insert212(word)
	}

	res := []string{}

	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			trie.Search212(&board, i, j, &res)
		}
	}

	return res
}

// Trie212 - Prefix Tree
type Trie212 struct {
	links [26]*Trie212
	word  string
}

// IsLeafNode - check if it is a leaf node
func (tr *Trie212) IsLeafNode() bool {
	for _, link := range tr.links {
		if link != nil {
			return false
		}
	}
	return true
}

// Insert212 - insert a word
func (tr *Trie212) Insert212(word string) {
	for i := 0; i < len(word); i++ {
		ch := word[i] - 'a'
		if tr.links[ch] == nil {
			tr.links[ch] = &Trie212{}
		}
		tr = tr.links[ch]
	}
	tr.word = word
}

// Search212 - search words
func (tr *Trie212) Search212(board *[][]byte, x, y int, res *[]string) {
	if x < 0 || x >= len(*board) || y < 0 || y >= len((*board)[0]) ||
		(*board)[x][y] == '#' || tr.links[(*board)[x][y]-'a'] == nil {
		return
	}

	letter := (*board)[x][y]
	cur := tr.links[letter-'a']

	// check if there is any match
	if cur.word != "" {
		(*res) = append(*res, cur.word)
		cur.word = ""
	}

	(*board)[x][y] = '#' // 标记已访问
	dx, dy := [4]int{1, 0, -1, 0}, [4]int{0, 1, 0, -1}
	for i := 0; i < 4; i++ {
		cur.Search212(board, x+dx[i], y+dy[i], res)
	}
	(*board)[x][y] = letter // restore the original letter

	// 使用剪枝进行优化
	// 对于 Trie 中的叶节点，一旦遍历它（即找到匹配的单词），就不需要再遍历它了。
	if cur.IsLeafNode() {
		tr.links[letter-'a'] = nil
	}
}

// @lc code=end
