/*
 * @lc app=leetcode.cn id=796 lang=cpp
 *
 * [796] 旋转字符串
 *
 * https://leetcode-cn.com/problems/rotate-string/description/
 *
 * algorithms
 * Easy (54.99%)
 * Likes:    167
 * Dislikes: 0
 * Total Accepted:    29K
 * Total Submissions: 52.8K
 * Testcase Example:  '"abcde"\n"cdeab"'
 *
 * 给定两个字符串, s 和 goal。如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true 。
 * 
 * s 的 旋转操作 就是将 s 最左边的字符移动到最右边。 
 * 
 * 
 * 例如, 若 s = 'abcde'，在旋转一次之后结果就是'bcdea' 。
 * 
 * 
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入: s = "abcde", goal = "cdeab"
 * 输出: true
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: s = "abcde", goal = "abced"
 * 输出: false
 * 
 * 
 * 
 * 
 * 提示:
 * 
 * 
 * 1 <= s.length, goal.length <= 100
 * s 和 goal 由小写英文字母组成
 * 
 * 
 */

/**
 * @File    :   796.旋转字符串.cpp
 * @Time    :   2022/03/26 10:17:31
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    bool rotateString(string s, string goal) {
        return s.length() == goal.length() &&
               (s + s).find(goal) != string::npos;
    }
};
// @lc code=end
