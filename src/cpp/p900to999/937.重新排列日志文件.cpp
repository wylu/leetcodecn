/*
 * @lc app=leetcode.cn id=937 lang=cpp
 *
 * [937] 重新排列日志文件
 *
 * https://leetcode-cn.com/problems/reorder-data-in-log-files/description/
 *
 * algorithms
 * Easy (60.44%)
 * Likes:    120
 * Dislikes: 0
 * Total Accepted:    18K
 * Total Submissions: 29.8K
 * Testcase Example:  '["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]'
 *
 * 给你一个日志数组 logs。每条日志都是以空格分隔的字串，其第一个字为字母与数字混合的 标识符 。
 * 
 * 有两种不同类型的日志：
 * 
 * 
 * 字母日志：除标识符之外，所有字均由小写字母组成
 * 数字日志：除标识符之外，所有字均由数字组成
 * 
 * 
 * 请按下述规则将日志重新排序：
 * 
 * 
 * 所有 字母日志 都排在 数字日志 之前。
 * 字母日志 在内容不同时，忽略标识符后，按内容字母顺序排序；在内容相同时，按标识符排序。
 * 数字日志 应该保留原来的相对顺序。
 * 
 * 
 * 返回日志的最终顺序。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3
 * art zero"]
 * 输出：["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3
 * 6"]
 * 解释：
 * 字母日志的内容都不同，所以顺序为 "art can", "art zero", "own kit dig" 。
 * 数字日志保留原来的相对顺序 "dig1 8 1 5 1", "dig2 3 6" 。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act
 * zoo"]
 * 输出：["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= logs.length <= 100
* 3 <= logs[i].length <= 100
 * logs[i] 中，字与字之间都用 单个 空格分隔
 * 题目数据保证 logs[i] 都有一个标识符，并且在标识符之后至少存在一个字
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   937.重新排列日志文件.cpp
 * @Time    :   2022/05/03 09:14:22
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
class Solution {
public:
    vector<string> reorderLogFiles(vector<string> &logs) {
        stable_sort(
            logs.begin(), logs.end(),
            [&](const string &s1, const string &s2) -> bool {
                int idx1 = s1.find(' ') + 1, idx2 = s2.find(' ') + 1;
                int ch1 = s1[idx1], ch2 = s2[idx2];
                if ('a' <= ch1 && ch1 <= 'z' && 'a' <= ch2 && ch2 <= 'z') {
                    string s1l = s1.substr(0, idx1 - 1),
                           s2l = s2.substr(0, idx2 - 1);
                    string s1r = s1.substr(idx1), s2r = s2.substr(idx2);
                    return s1r == s2r ? s1l < s2l : s1r < s2r;
                }
                return 'a' <= ch1 && ch1 <= 'z';
            });
        return logs;
    }
};
// @lc code=end
