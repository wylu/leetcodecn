package p1000to1099

import (
	"math"
	"math/rand"
	"time"
)

/*
 * @lc app=leetcode.cn id=1044 lang=golang
 *
 * [1044] 最长重复子串
 *
 * https://leetcode-cn.com/problems/longest-duplicate-substring/description/
 *
 * algorithms
 * Hard (24.43%)
 * Likes:    178
 * Dislikes: 0
 * Total Accepted:    7.8K
 * Total Submissions: 32.4K
 * Testcase Example:  '"banana"'
 *
 * 给你一个字符串 s ，考虑其所有 重复子串 ：即，s 的连续子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。
 *
 * 返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "banana"
 * 输出："ana"
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "abcd"
 * 输出：""
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= s.length <= 3 * 10^4
 * s 由小写英文字母组成
 *
 *
 */

/**
 * @File    :   1044.最长重复子串.go
 * @Time    :   2021/12/23 09:27:26
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：二分查找 + Rabin-Karp 字符串编码
 * 思路及解法
 *
 * 记 s 的长度为 n。这个问题可以分为两步：从 n - 1 到 1 由大至小遍历选取长度 L，
 * 判断 s 中是否有长度为 L 的重复子串。从大至小遍历的时候，第一次遇到的符合条件
 * 的 L，即为最大的符合条件的 L，记为 L1，重复的子串为 s1。并且对于任意满足
 * L0 <= L1 的 L0 也均符合条件，因为 s1 的所有子串也是 s 的重复子串。而对于任意
 * 满足 L2 > L1 的 L2，则均不符合条件。因此，我们可以用二分查找的方法，来查找 L1。
 *
 * 剩下的任务便是如何高效判断 s 中是否有长度为 L 的重复子串。我们可以使用
 * Rabin-Karp 算法对固定长度的字符串进行编码。当两个字符串的编码相同时，
 * 则这两个字符串也相同。在 s 中 {n-L+1} 个长度为 L 的子串中，有两个子串的
 * 编码相同时，则说明存在长度为 L 的重复子串。具体步骤如下：
 *
 * 1.首先，我们需要对 s 的每个字符进行编码，得到一个数组 arr。因为本题中 s 仅包含
 * 小写字母，我们可按照 arr[i] = (int)s.charAt(i) - (int)'a'，将所有字母编码为
 * 0-25 之间的数字。比如字符串 "abcde" 可以编码为数组 [0, 1, 2, 3, 4]。
 *
 * 2.我们将子串看成一个 26 进制的数，它对应的 10 进制数就是它的编码。假设此时我们
 * 需要求长度为 3 的子串的编码。那么第一个子串 "abc" 的编码就是
 * h0 = 0 * 26^2 + 1 * 26^1 + 2 * 26^0 = 28。更一般地，设 ci 为 s 的第 i 个字符
 * 编码后的数字，a (a >= 26) 为编码的进制，那么有
 * h0 = c0 * a^{L-1} + c1 * a^{L-2} + ... + c{L-1} * a^1 = sum{0,L-1} ci * a^{L-1-i}。
 *
 * 3.上一步我们只求了第一个子串 "abc" 的编码。当我们要求第二个子串 "bcd" 的编码时，
 * 也可以按照上一步的方法求：h1 = 1 * 26^2 + 2 * 26^1 + 3 * 26^0 = 731，但是这样
 * 时间复杂度是 O(L)。我们可以在 h0 的基础上，更快地求出它的编码：
 * h1 = (h0 - 0 * 26^2) * 26 + 3 * 26^0 = 731。更一般的表达式是：
 * h1 = (h0 * a - c0 * a^L) + c{L+1}。这样，我们只需要在常数时间内就可以根据
 * 上一个子串的编码求出下一个子串的编码。我们用一个哈希表 seen 来存储子串的编码。
 * 在求子串的编码时，如果某个子串的编码出现过，则表示存在长度为 L 的重复子串，
 * 否则，我们将当前的编码放入 seen 中。如果所有编码都不重复，则说明不存在长度为
 * L 的重复子串。
 *
 * 4.还有一点需要考虑的是，本题中 a^L 会非常大。一般的做法是需要对编码进行取模来
 * 防止溢出，模一般选取编码的信息量的平方的数量级。而取模则会带来哈希碰撞。
 * 本题中为了避免碰撞，我们使用双哈希，即用两套进制和模的组合，来对字符串进行
 * 编码。只有两种编码都相同时，我们才认为字符串相同。
 *
 * 5.本题要求返回最长重复子串而不是最长重复子串长度。因此，当存在长度为 L 的子串时，
 * 我们的判断函数可以返回重复子串的起点。而当不存在时，可以返回 -1 用做区分。
 */

// @lc code=start
func longestDupSubstring(s string) string {
	rand.Seed(time.Now().UnixNano())
	randint := func(begin, end int) int {
		return begin + rand.Intn(end-begin)
	}

	pow := func(a, b, mod int) int {
		res := 1
		for b > 0 {
			if b&1 > 0 {
				res = res * a % mod
			}
			a = a * a % mod
			b >>= 1
		}
		return res
	}

	// 生成两个进制
	a1, a2 := randint(26, 100), randint(26, 100)
	// 生成两个模
	mod1, mod2 := randint(1e9+7, math.MaxInt32), randint(1e9+7, math.MaxInt32)

	n := len(s)
	// 先对所有字符进行编码
	arr := []int{}
	for _, ch := range s {
		arr = append(arr, int(byte(ch)-'a'))
	}

	check := func(m int) int {
		al1, al2 := pow(a1, m, mod1), pow(a2, m, mod2)
		h1, h2 := 0, 0
		for i := 0; i < m; i++ {
			h1 = (h1*a1 + arr[i]) % mod1
			h2 = (h2*a2 + arr[i]) % mod2
		}

		// 存储一个编码组合是否出现过
		seen := map[[2]int]bool{{h1, h2}: true}
		for i := 1; i <= n-m; i++ {
			h1 = (h1*a1 - arr[i-1]*al1 + arr[i+m-1]) % mod1
			if h1 < 0 {
				h1 += mod1
			}
			h2 = (h2*a2 - arr[i-1]*al2 + arr[i+m-1]) % mod2
			if h2 < 0 {
				h2 += mod2
			}
			code := [2]int{h1, h2}
			// 如果重复，则返回重复串的起点
			if seen[code] {
				return i
			}
			seen[code] = true
		}

		// 没有重复，则返回 -1
		return -1
	}

	// 二分查找的范围 [1, n-1]
	left, right := 1, n-1
	size, start := 0, -1
	for left <= right {
		m := left + (right-left+1)/2
		idx := check(m)
		if idx != -1 {
			// 有重复子串，移动左边界
			left = m + 1
			size, start = m, idx
		} else {
			// 无重复子串，移动右边界
			right = m - 1
		}
	}

	if start == -1 {
		return ""
	}
	return s[start : start+size]
}

// @lc code=end
