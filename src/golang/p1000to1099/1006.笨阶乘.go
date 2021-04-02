package p1000to1099

/*
 * @lc app=leetcode.cn id=1006 lang=golang
 *
 * [1006] 笨阶乘
 *
 * https://leetcode-cn.com/problems/clumsy-factorial/description/
 *
 * algorithms
 * Medium (52.67%)
 * Likes:    70
 * Dislikes: 0
 * Total Accepted:    19.7K
 * Total Submissions: 31.5K
 * Testcase Example:  '4'
 *
 * 通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4
 * * 3 * 2 * 1。
 *
 * 相反，我们设计了一个笨阶乘
 * clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。
 *
 * 例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 *
 * 1。然而，这些运算仍然使用通常的算术运算顺序：我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。
 *
 * 另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数。
 *
 * 实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。
 *
 *
 *
 * 示例 1：
 *
 * 输入：4
 * 输出：7
 * 解释：7 = 4 * 3 / 2 + 1
 *
 *
 * 示例 2：
 *
 * 输入：10
 * 输出：12
 * 解释：12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= N <= 10000
 * -2^31 <= answer <= 2^31 - 1  （答案保证符合 32 位整数。）
 *
 *
 */

/**
 * @File    :   1006.笨阶乘.go
 * @Time    :   2021/04/02 09:29:22
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：使用栈模拟
 * 思路
 *
 * 根据求解问题「150. 逆波兰表达式求值」、「224. 基本计算器」、
 * 「227. 基本计算器 II」的经验，表达式的计算一般可以借助数据结构
 * 「栈」完成，特别是带有括号的表达式。我们将暂时还不能确定的数据
 * 存入栈，确定了优先级最高以后，一旦可以计算出结果，我们就把数据
 * 从栈里取出，整个过程恰好符合了「后进先出」的规律。本题也不例外。
 *
 * 根据题意，「笨阶乘」没有显式括号，运算优先级是先「乘除」后「加减」。
 * 我们可以从 N 开始，枚举 N-1、N-2 直到 1 ，枚举这些数的时候，认为
 * 它们之前的操作符按照「乘」「除」「加」「减」交替进行。
 *
 * 出现乘法、除法的时候可以把栈顶元素取出，与当前的 N 进行乘法运算、
 * 除法运算（除法运算需要注意先后顺序），并将运算结果重新压入栈中；
 *
 * 出现加法、减法的时候，把减法视为加上一个数的相反数，然后压入栈，
 * 等待以后遇见「乘」「除」法的时候取出。
 *
 * 最后将栈中元素累加即为答案。由于加法运算交换律成立，可以将栈里的
 * 元素依次出栈相加。
 */

// @lc code=start
func clumsy(N int) int {
	stack := []int{N}
	N--
	for idx := 0; N > 0; idx, N = idx+1, N-1 {
		size := len(stack)
		switch idx % 4 {
		case 0:
			stack[size-1] *= N
		case 1:
			stack[size-1] /= N
		case 2:
			stack = append(stack, N)
		default:
			stack = append(stack, -N)
		}
	}

	ans := 0
	for _, num := range stack {
		ans += num
	}
	return ans
}

// @lc code=end
