package p400to499

import "math"

/*
 * @lc app=leetcode.cn id=458 lang=golang
 *
 * [458] 可怜的小猪
 *
 * https://leetcode-cn.com/problems/poor-pigs/description/
 *
 * algorithms
 * Hard (61.63%)
 * Likes:    307
 * Dislikes: 0
 * Total Accepted:    19.9K
 * Total Submissions: 28.8K
 * Testcase Example:  '1000\n15\n60'
 *
 * 有 buckets 桶液体，其中 正好
 * 有一桶含有毒药，其余装的都是水。它们从外观看起来都一样。为了弄清楚哪只水桶含有毒药，你可以喂一些猪喝，通过观察猪是否会死进行判断。不幸的是，你只有
 * minutesToTest 分钟时间来确定哪桶液体是有毒的。
 *
 * 喂猪的规则如下：
 *
 *
 * 选择若干活猪进行喂养
 * 可以允许小猪同时饮用任意数量的桶中的水，并且该过程不需要时间。
 * 小猪喝完水后，必须有 minutesToDie 分钟的冷却时间。在这段时间里，你只能观察，而不允许继续喂猪。
 * 过了 minutesToDie 分钟后，所有喝到毒药的猪都会死去，其他所有猪都会活下来。
 * 重复这一过程，直到时间用完。
 *
 *
 * 给你桶的数目 buckets ，minutesToDie 和 minutesToTest ，返回在规定时间内判断哪个桶有毒所需的 最小 猪数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：buckets = 1000, minutesToDie = 15, minutesToTest = 60
 * 输出：5
 *
 *
 * 示例 2：
 *
 *
 * 输入：buckets = 4, minutesToDie = 15, minutesToTest = 15
 * 输出：2
 *
 *
 * 示例 3：
 *
 *
 * 输入：buckets = 4, minutesToDie = 15, minutesToTest = 30
 * 输出：2
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= buckets <= 1000
 * 1 <= minutesToDie <= minutesToTest <= 100
 *
 *
 */

/**
 * @File    :   458.可怜的小猪.go
 * @Time    :   2021/11/25 22:12:09
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：数学
 *
 * 这道题初看的时候，很多人会纠结：到底需要多少只小猪，而每只小猪又应该具体
 * 如何喝水才能判断出哪只水桶有毒？
 *
 * 这道题最开始不要去关注细节，去想到底应该怎么喂水。而是应该先思考在考察
 * 哪方面的问题，数组、链表、二叉树还是数学？那么仔细思考就能得出结论，
 * 本质上在考察数学中的 进制 问题。
 *
 * 举例说明：
 *
 * 假设：总时间 minutesToTest = 60，死亡时间 minutesToDie = 15，pow(x, y)
 * 	表示 x 的 y 次方，ceil(x)表示 x 向上取整
 *
 * 如果有 1 只小猪，则最多可以喝 times = minutesToTest / minutesToDie = 4 次水，
 * 能够携带 base = times + 1 = 5 个的信息量，也就是（便于理解从 0 开始）：
 *
 *   (1) 喝 0 号死去，0 号桶水有毒
 *   (2) 喝 1 号死去，1 号桶水有毒
 *   (3) 喝 2 号死去，2 号桶水有毒
 *   (4) 喝 3 号死去，3 号桶水有毒
 *   (5) 喝了上述所有水依然活蹦乱跳，4 号桶水有毒
 *
 * 结论是 1 只小猪最多能够验证 5 桶水中哪只水桶含有毒，当 buckets <= 5 时
 * answer = 1
 *
 * 那么 2 只小猪可以验证的范围最多到多少呢？我们把每只小猪携带的信息量看成是
 * base 进制数，2 只小猪的信息量就是 pow(base, 2) = pow(5, 2) = 25，所以
 * 当 5 <= buckets <= 25时，anwser = 2
 *
 * 那么可以得到公式关系：pow(base, ans) >= buckets，取对数后即为：
 * ans >= log(buckets) / log(base)，因为 ans 为整数，所以
 * ans = ceil(log(buckets) / log(base))
 *
 * 看到这里我们再去关注细节，2 只小猪到底怎么喂水，在上述假设下，能够最多
 * 验证 25 桶水呢？请看下方图画解答：
 * https://leetcode-cn.com/problems/poor-pigs/solution/hua-jie-suan-fa-458-ke-lian-de-xiao-zhu-by-guanpen/
 */

// @lc code=start
func poorPigs(buckets int, minutesToDie int, minutesToTest int) int {
	base := minutesToTest/minutesToDie + 1
	return int(math.Ceil(math.Log(float64(buckets)) / math.Log(float64(base))))
}

// @lc code=end
