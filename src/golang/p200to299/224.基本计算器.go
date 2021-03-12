package p200to299

/*
 * @lc app=leetcode.cn id=224 lang=golang
 *
 * [224] 基本计算器
 *
 * https://leetcode-cn.com/problems/basic-calculator/description/
 *
 * algorithms
 * Hard (41.89%)
 * Likes:    506
 * Dislikes: 0
 * Total Accepted:    52.2K
 * Total Submissions: 124.6K
 * Testcase Example:  '"1 + 1"'
 *
 * 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "1 + 1"
 * 输出：2
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = " 2-1 + 2 "
 * 输出：3
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = "(1+(4+5+2)-3)+(6+8)"
 * 输出：23
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 3 * 10^5
 * s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
 * s 表示一个有效的表达式
 *
 *
 */

/**
 * @File    :   224.基本计算器.go
 * @Time    :   2021/03/12 13:32:42
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：括号展开 + 栈
 * 
 * 由于字符串除了数字与括号外，只有加号和减号两种运算符。因此，如果展开
 * 表达式中所有的括号，则得到的新表达式中，数字本身不会发生变化，只是
 * 每个数字前面的符号会发生变化。
 * 
 * 因此，我们考虑使用一个取值为 {−1,+1} 的整数 sign 代表「当前」的符号。
 * 根据括号表达式的性质，它的取值：
 * 
 *   - 与字符串中当前位置的运算符有关；
 *   - 如果当前位置处于一系列括号之内，则也与这些括号前面的运算符有关：
 *     每当遇到一个以 - 号开头的括号，则意味着此后的符号都要被「翻转」。
 * 
 * 考虑到第二点，我们需要维护一个栈 ops，其中栈顶元素记录了当前位置所处
 * 的每个括号所「共同形成」的符号。例如，对于字符串 1+2+(3-(4+5))：
 * 
 *   - 扫描到 1+2 时，由于当前位置没有被任何括号所包含，则栈顶元素为
 *     初始值 +1；
 *   - 扫描到 1+2+(3 时，当前位置被一个括号所包含，该括号前面的符号为
 *     + 号，因此栈顶元素依然 +1；
 *   - 扫描到 1+2+(3-(4 时，当前位置被两个括号所包含，分别对应着 + 号
 *     和 - 号，由于 + 号和 - 号合并的结果为 - 号，因此栈顶元素变为 -1。
 * 
 * 在得到栈 ops 之后，sign 的取值就能够确定了：如果当前遇到了 + 号，
 * 则更新 sign <- ops.top()；如果遇到了遇到了 - 号，则更新
 * sign <- −ops.top()。
 * 
 * 然后，每当遇到 ( 时，都要将当前的 sign 取值压入栈中；每当遇到 ) 时，
 * 都从栈中弹出一个元素。这样，我们能够在扫描字符串的时候，即时地更新
 * ops 中的元素。
 */

// @lc code=start
func calculate(s string) int {
	ans := 0
	sign, ops := 1, []int{1}
	i, n := 0, len(s)

	for i < n {
		if s[i] == ' ' {
			i++
		} else if s[i] == '+' {
			sign = ops[len(ops)-1]
			i++
		} else if s[i] == '-' {
			sign = -ops[len(ops)-1]
			i++
		} else if s[i] == '(' {
			ops = append(ops, sign)
			i++
		} else if s[i] == ')' {
			ops = ops[:len(ops)-1]
			i++
		} else {
			num := 0
			for i < n && s[i] >= '0' && s[i] <= '9' {
				num = num*10 + int(s[i]-'0')
				i++
			}
			ans += sign * num
		}
	}

	return ans
}

// @lc code=end
