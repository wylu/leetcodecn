package p700to799

/*
 * @lc app=leetcode.cn id=752 lang=golang
 *
 * [752] 打开转盘锁
 *
 * https://leetcode-cn.com/problems/open-the-lock/description/
 *
 * algorithms
 * Medium (51.55%)
 * Likes:    316
 * Dislikes: 0
 * Total Accepted:    51.6K
 * Total Submissions: 100K
 * Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
 *
 * 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8',
 * '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
 *
 * 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
 *
 * 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
 *
 * 字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
 * 输出：6
 * 解释：
 * 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
 * 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
 * 因为当拨动到 "0102" 时这个锁就会被锁定。
 *
 *
 * 示例 2:
 *
 *
 * 输入: deadends = ["8888"], target = "0009"
 * 输出：1
 * 解释：
 * 把最后一位反向旋转一次即可 "0000" -> "0009"。
 *
 *
 * 示例 3:
 *
 *
 * 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
 * target = "8888"
 * 输出：-1
 * 解释：
 * 无法旋转到目标数字且不被锁定。
 *
 *
 * 示例 4:
 *
 *
 * 输入: deadends = ["0000"], target = "8888"
 * 输出：-1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * deadends[i].length == 4
 * target.length == 4
 * target 不在 deadends 之中
 * target 和 deadends[i] 仅由若干位数字组成
 *
 *
 */

/**
 * @File    :   752.打开转盘锁.go
 * @Time    :   2021/06/26 09:21:40
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：广度优先搜索
 *
 * 我们可以将 0000 到 9999 这 10000 状态看成图上的 10000 个节点，两个节点
 * 之间存在一条边，当且仅当这两个节点对应的状态只有 1 位不同，且不同的那位
 * 相差 1（包括 0 和 9 也相差 1 的情况），并且这两个节点均不在数组 deadends
 * 中。那么最终的答案即为 0000 到 target 的最短路径。
 *
 * 我们用广度优先搜索来找到最短路径，从 0000 开始搜索。对于每一个状态，它可以
 * 扩展到最多 8 个状态，即将它的第 i = 0, 1, 2, 3 位增加 1 或减少 1，将这些
 * 状态中没有搜索过并且不在 deadends 中的状态全部加入到队列中，并继续进行搜索。
 * 注意 0000 本身有可能也在 deadends 中。
 */

// @lc code=start
func openLock(deadends []string, target string) int {
	if target == "0000" {
		return 0
	}
	seen := make(map[string]bool, 20000)
	for _, dead := range deadends {
		seen[dead] = true
	}

	que := []string{"0000"}
	if seen[que[0]] {
		return -1
	}

	ans := 0
	seen["0000"] = true
	for len(que) > 0 {
		ans++
		size := len(que)
		for i := 0; i < size; i++ {
			s := que[0]
			que = que[1:]
			for j := 0; j < 4; j++ {
				num := int(s[j] - '0')
				increase := byte((num+1)%10) + '0'
				decrease := byte('9')
				if num > 0 {
					decrease = byte(num-1) + '0'
				}

				incSeq, decSeq := []byte(s), []byte(s)
				incSeq[j], decSeq[j] = increase, decrease

				inc, dec := string(incSeq), string(decSeq)
				if inc == target || dec == target {
					return ans
				}

				if !seen[inc] {
					seen[inc] = true
					que = append(que, inc)
				}

				if !seen[dec] {
					seen[dec] = true
					que = append(que, dec)
				}
			}
		}
	}

	return -1
}

// @lc code=end
