package p400to499

import "strings"

/*
 * @lc app=leetcode.cn id=482 lang=golang
 *
 * [482] 密钥格式化
 *
 * https://leetcode-cn.com/problems/license-key-formatting/description/
 *
 * algorithms
 * Easy (44.93%)
 * Likes:    94
 * Dislikes: 0
 * Total Accepted:    26.3K
 * Total Submissions: 58.6K
 * Testcase Example:  '"5F3Z-2e-9-w"\n4'
 *
 * 有一个密钥字符串 S ，只包含字母，数字以及 '-'（破折号）。其中， N 个 '-' 将字符串分成了 N+1 组。
 *
 * 给你一个数字 K，请你重新格式化字符串，使每个分组恰好包含 K 个字符。特别地，第一个分组包含的字符个数必须小于等于 K，但至少要包含 1
 * 个字符。两个分组之间需要用 '-'（破折号）隔开，并且将所有的小写字母转换为大写字母。
 *
 * 给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。
 *
 *
 *
 * 示例 1：
 *
 * 输入：S = "5F3Z-2e-9-w", K = 4
 * 输出："5F3Z-2E9W"
 * 解释：字符串 S 被分成了两个部分，每部分 4 个字符；
 * 注意，两个额外的破折号需要删掉。
 *
 *
 * 示例 2：
 *
 * 输入：S = "2-5g-3-J", K = 2
 * 输出："2-5G-3J"
 * 解释：字符串 S 被分成了 3 个部分，按照前面的规则描述，第一部分的字符可以少于给定的数量，其余部分皆为 2 个字符。
 *
 *
 *
 *
 * 提示:
 *
 *
 * S 的长度可能很长，请按需分配大小。K 为正整数。
 * S 只包含字母数字（a-z，A-Z，0-9）以及破折号'-'
 * S 非空
 *
 *
 *
 *
 */

/**
 * @File    :   482.密钥格式化.go
 * @Time    :   2021/10/04 11:12:02
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func licenseKeyFormatting(s string, k int) string {
	chrs := []byte{}
	for _, ch := range []byte(s) {
		if ch == '-' {
			continue
		}
		if ch >= 'a' && ch <= 'z' {
			ch -= byte(32)
		}
		chrs = append(chrs, ch)
	}

	ans := []string{}
	n := len(chrs)
	d, r := n/k, n%k
	if r > 0 {
		ans = append(ans, string(chrs[:r]))
		chrs = chrs[r:]
	}

	for i := 0; i < d; i++ {
		ans = append(ans, string(chrs[i*k:(i+1)*k]))
	}

	return strings.Join(ans, "-")
}

// @lc code=end
