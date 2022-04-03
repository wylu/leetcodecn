package p700to799

import "sort"

/*
 * @lc app=leetcode.cn id=744 lang=golang
 *
 * [744] 寻找比目标字母大的最小字母
 *
 * https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/description/
 *
 * algorithms
 * Easy (46.46%)
 * Likes:    153
 * Dislikes: 0
 * Total Accepted:    52.8K
 * Total Submissions: 113.8K
 * Testcase Example:  '["c","f","j"]\n"a"'
 *
 * 给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母
 * target，请你寻找在这一有序列表里比目标字母大的最小字母。
 *
 * 在比较时，字母是依序循环出现的。举个例子：
 *
 *
 * 如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入: letters = ["c", "f", "j"]，target = "a"
 * 输出: "c"
 *
 *
 * 示例 2:
 *
 *
 * 输入: letters = ["c","f","j"], target = "c"
 * 输出: "f"
 *
 *
 * 示例 3:
 *
 *
 * 输入: letters = ["c","f","j"], target = "d"
 * 输出: "f"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= letters.length <= 10^4
 * letters[i] 是一个小写字母
 * letters 按非递减顺序排序
 * letters 最少包含两个不同的字母
 * target 是一个小写字母
 *
 *
 */

/**
 * @File    :   744.寻找比目标字母大的最小字母.go
 * @Time    :   2022/04/03 08:14:54
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func nextGreatestLetter(letters []byte, target byte) byte {
	if target >= letters[len(letters)-1] {
		return letters[0]
	}
	i := sort.Search(len(letters)-1, func(i int) bool { return letters[i] > target })
	return letters[i]
}

// @lc code=end

// func nextGreatestLetter(letters []byte, target byte) byte {
// 	left, right := 0, len(letters)
// 	for left < right {
// 		mid := left + (right-left)/2
// 		if letters[mid] <= target {
// 			left += 1
// 		} else {
// 			right = mid
// 		}
// 	}
// 	return letters[left%len(letters)]
// }

// func nextGreatestLetter(letters []byte, target byte) byte {
// 	for _, ch := range letters {
// 		if ch > target {
// 			return ch
// 		}
// 	}
// 	return letters[0]
// }
