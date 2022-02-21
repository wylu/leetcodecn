package p800to899

/*
 * @lc app=leetcode.cn id=838 lang=golang
 *
 * [838] 推多米诺
 *
 * https://leetcode-cn.com/problems/push-dominoes/description/
 *
 * algorithms
 * Medium (54.98%)
 * Likes:    210
 * Dislikes: 0
 * Total Accepted:    21.9K
 * Total Submissions: 39.9K
 * Testcase Example:  '"RR.L"'
 *
 * n 张多米诺骨牌排成一行，将每张多米诺骨牌垂直竖立。在开始时，同时把一些多米诺骨牌向左或向右推。
 *
 * 每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。
 *
 * 如果一张垂直竖立的多米诺骨牌的两侧同时有多米诺骨牌倒下时，由于受力平衡， 该骨牌仍然保持不变。
 *
 * 就这个问题而言，我们会认为一张正在倒下的多米诺骨牌不会对其它正在倒下或已经倒下的多米诺骨牌施加额外的力。
 *
 * 给你一个字符串 dominoes 表示这一行多米诺骨牌的初始状态，其中：
 *
 *
 * dominoes[i] = 'L'，表示第 i 张多米诺骨牌被推向左侧，
 * dominoes[i] = 'R'，表示第 i 张多米诺骨牌被推向右侧，
 * dominoes[i] = '.'，表示没有推动第 i 张多米诺骨牌。
 *
 *
 * 返回表示最终状态的字符串。
 *
 *
 * 示例 1：
 *
 *
 * 输入：dominoes = "RR.L"
 * 输出："RR.L"
 * 解释：第一张多米诺骨牌没有给第二张施加额外的力。
 *
 *
 * 示例 2：
 *
 *
 * 输入：dominoes = ".L.R...LR..L.."
 * 输出："LL.RR.LLRRLL.."
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == dominoes.length
 * 1 <= n <= 10^5
 * dominoes[i] 为 'L'、'R' 或 '.'
 *
 *
 */

/**
 * @File    :   838.推多米诺.go
 * @Time    :   2022/02/21 16:46:34
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func pushDominoes(dominoes string) string {
	s := []byte(dominoes)

	i, n, left := 0, len(s), byte('L')
	for i < n {
		j := i
		for j < n && s[j] == '.' { // 找到一段连续的没有被推动的骨牌
			j++
		}
		right := byte('R')
		if j < n {
			right = s[j]
		}

		if left == right { // 方向相同，那么这些竖立骨牌也会倒向同一方向
			for i < j {
				s[i] = right
				i++
			}
		} else if left == 'R' && right == 'L' { // 方向相对，那么就从两侧向中间倒
			for k := j - 1; i < k; i, k = i+1, k-1 {
				s[i], s[k] = 'R', 'L'
			}
		}
		left = right
		i = j + 1
	}

	return string(s)
}

// @lc code=end

// func pushDominoes(dominoes string) string {
// 	chs := []byte(dominoes)
// 	p1, p2, n := 0, 0, len(chs)
// 	for p2 < n {
// 		for ; p2 < n && chs[p2] != 'L'; p2++ {
// 			if chs[p2] == 'R' {
// 				p1 = p2
// 			}
// 		}

// 		if chs[p1] == 'R' && p2 < n {
// 			i, j := p1, p2
// 			for ; i < j; i, j = i+1, j-1 {
// 				chs[i], chs[j] = 'R', 'L'
// 			}
// 			if i == j {
// 				chs[i] = '#'
// 			}
// 			p1 = p2
// 		}

// 		p2++
// 	}

// 	for i := 0; i < n; i++ {
// 		if chs[i] == 'L' {
// 			for j := i - 1; j >= 0 && chs[j] == '.'; j-- {
// 				chs[j] = 'L'
// 			}
// 		} else if chs[i] == 'R' {
// 			for j := i + 1; j < n && chs[j] == '.'; j++ {
// 				chs[j] = 'R'
// 			}
// 		}
// 	}

// 	for i := 0; i < n; i++ {
// 		if chs[i] == '#' {
// 			chs[i] = '.'
// 		}
// 	}

// 	return string(chs)
// }
