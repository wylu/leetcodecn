/*
 * @lc app=leetcode.cn id=1702 lang=cpp
 *
 * [1702] 修改后的最大二进制字符串
 *
 * https://leetcode-cn.com/problems/maximum-binary-string-after-change/description/
 *
 * algorithms
 * Medium (48.62%)
 * Likes:    7
 * Dislikes: 0
 * Total Accepted:    1.7K
 * Total Submissions: 3.4K
 * Testcase Example:  '"000110"'
 *
 * 给你一个二进制字符串 binary ，它仅有 0 或者 1 组成。你可以使用下面的操作任意次对它进行修改：
 * 
 * 
 * 操作 1 ：如果二进制串包含子字符串 "00" ，你可以用 "10" 将其替换。
 * 
 * 
 * 比方说， "00010" -> "10010"
 * 
 * 
 * 操作 2 ：如果二进制串包含子字符串 "10" ，你可以用 "01" 将其替换。
 * 
 * 比方说， "00010" -> "00001"
 * 
 * 
 * 
 * 
 * 请你返回执行上述操作任意次以后能得到的 最大二进制字符串 。如果二进制字符串 x 对应的十进制数字大于二进制字符串 y
 * 对应的十进制数字，那么我们称二进制字符串 x 大于二进制字符串 y 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：binary = "000110"
 * 输出："111011"
 * 解释：一个可行的转换为：
 * "000110" -> "000101" 
 * "000101" -> "100101" 
 * "100101" -> "110101" 
 * "110101" -> "110011" 
 * "110011" -> "111011"
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：binary = "01"
 * 输出："01"
 * 解释："01" 没办法进行任何转换。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= binary.length <= 10^5
 * binary 仅包含 '0' 和 '1' 。
 * 
 * 
 */

/**
 * @File    :   1702.修改后的最大二进制字符串.cpp
 * @Time    :   2021/01/01 10:31:11
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 贪心：
 * 
 * 通过 10->01，可以将所有 1 移到最后
 * 通过 00->10，可以使答案最终只剩下一个 0
 * 
 * 贪心的目标是尽可能往高位填 1 ，使最后 0 尽可能靠后。
 * 
 * 例如：111110101010101
 * 1.保留原字符串最前面的连续的 1 不要动，(即 11111....)
 * 2.遇到第一个 0 开始即以后的为剩余的字符串(即 0101010101)
 * 3.统计剩余字符串部分的 1 的个数，这些 1 全部移到最后，
 *   0 移到剩余字符串的前面(即 0000011111)
 * 4.然后把零全部替换为 1，注意留下最后一个零不替换(即 1111011111)
 * 5.组合即为最终答案 --> 11111 1111011111
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    string maximumBinaryString(string binary) {
        int n = binary.length(), cnt = 0;
        bool flag = false;

        for (auto ch : binary) {
            if (ch == '0') flag = true;
            if (flag && ch == '1') cnt++;
        }

        if (!flag) return binary;

        string ans = string(n, '1');
        ans[n - cnt - 1] = '0';
        return ans;
    }
};
// @lc code=end
