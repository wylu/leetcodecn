package p400to499

/*
 * @lc app=leetcode.cn id=423 lang=golang
 *
 * [423] 从英文中重建数字
 *
 * https://leetcode-cn.com/problems/reconstruct-original-digits-from-english/description/
 *
 * algorithms
 * Medium (59.07%)
 * Likes:    86
 * Dislikes: 0
 * Total Accepted:    11.6K
 * Total Submissions: 19.7K
 * Testcase Example:  '"owoztneoer"'
 *
 * 给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "owoztneoer"
 * 输出："012"
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "fviefuro"
 * 输出："45"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 10^5
 * s[i] 为 ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]
 * 这些字符之一
 * s 保证是一个符合题目要求的字符串
 *
 *
 */

/**
 * @File    :   423.从英文中重建数字.go
 * @Time    :   2021/11/24 09:15:21
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：依次确定每一个数字的次数
 * 思路与算法
 *
 * 首先我们可以统计每个字母分别在哪些数字中出现：
 *
 * 	字母	数字
 * 	e	    0 1 3 5 7 8 9
 * 	f	    4 5
 * 	g	    8
 * 	h	    3 8
 * 	i	    5 6 8 9
 * 	n	    1 7 9
 * 	o	    0 1 2 4
 * 	r	    0 3 4
 * 	s	    6 7
 * 	t	    2 3 8
 * 	u	    4
 * 	v	    5 7
 * 	w	    2
 * 	x	    6
 * 	z	    0
 *
 * 可以发现，z, w, u, x, g 都只在一个数字中，即 0, 2, 4, 6, 8 中出现。
 * 因此我们可以使用一个哈希表统计每个字母出现的次数，那么 z, w, u, x, g
 * 出现的次数，即分别为 0, 2, 4, 6, 8 出现的次数。
 *
 * 随后我们可以注意那些只在两个数字中出现的字符：
 *
 * h 只在 3, 8 中出现。由于我们已经知道了 8 出现的次数，因此可以计算出
 * 3 出现的次数。
 *
 * f 只在 4, 5 中出现。由于我们已经知道了 4 出现的次数，因此可以计算出
 * 5 出现的次数。
 *
 * s 只在 6, 7 中出现。由于我们已经知道了 6 出现的次数，因此可以计算出
 * 7 出现的次数。
 *
 * 此时，我们还剩下 1 和 9 的出现次数没有求出：
 *
 * o 只在 0, 1, 2, 4 中出现，由于我们已经知道了 0, 2, 4 出现的次数，
 * 因此可以计算出 1 出现的次数。
 * 最后的 9 就可以通过 n, i, e 中的任一字符计算得到了。这里推荐使用
 * i 进行计算，因为 n 在 9 中出现了 2 次，e 在 3 中出现了 2 次，
 * 容易在计算中遗漏。
 *
 * 当我们统计完每个数字出现的次数后，我们按照升序将它们进行拼接即可。
 */

// @lc code=start
func originalDigits(s string) string {
	cnts := [26]int{}
	for _, ch := range s {
		cnts[ch-'a']++
	}

	nums := [10]int{}
	nums[0] = cnts['z'-'a']
	nums[2] = cnts['w'-'a']
	nums[4] = cnts['u'-'a']
	nums[6] = cnts['x'-'a']
	nums[8] = cnts['g'-'a']

	nums[3] = cnts['h'-'a'] - nums[8]
	nums[5] = cnts['f'-'a'] - nums[4]
	nums[7] = cnts['s'-'a'] - nums[6]

	nums[1] = cnts['o'-'a'] - nums[0] - nums[2] - nums[4]
	nums[9] = cnts['i'-'a'] - nums[5] - nums[6] - nums[8]

	ans := []byte{}
	for i := 0; i < 10; i++ {
		ch := byte(i) + '0'
		for j := 0; j < nums[i]; j++ {
			ans = append(ans, ch)
		}
	}

	return string(ans)
}

// @lc code=end

// func originalDigits(s string) string {
// 	cs, ns := "zwxsvfgito", "0267548931"
// 	words := []string{
// 		"zero", "two", "six", "seven", "five",
// 		"four", "eight", "nine", "three", "one",
// 	}

// 	cnts := [26]int{}
// 	for _, ch := range s {
// 		cnts[ch-'a']++
// 	}

// 	sub := func(word string, c int) {
// 		for _, ch := range word {
// 			cnts[ch-'a'] -= c
// 		}
// 	}

// 	ans := []byte{}
// 	for i, ch := range cs {
// 		c := cnts[ch-'a']
// 		if c > 0 {
// 			sub(words[i], c)
// 		}
// 		for j := 0; j < c; j++ {
// 			ans = append(ans, ns[i])
// 		}
// 	}

// 	sort.Slice(ans, func(i, j int) bool { return ans[i] < ans[j] })
// 	return string(ans)
// }
