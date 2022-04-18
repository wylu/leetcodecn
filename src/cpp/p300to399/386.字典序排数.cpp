/*
 * @lc app=leetcode.cn id=386 lang=cpp
 *
 * [386] 字典序排数
 *
 * https://leetcode-cn.com/problems/lexicographical-numbers/description/
 *
 * algorithms
 * Medium (76.08%)
 * Likes:    289
 * Dislikes: 0
 * Total Accepted:    37.3K
 * Total Submissions: 49K
 * Testcase Example:  '13'
 *
 * 给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。
 * 
 * 你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 13
 * 输出：[1,10,11,12,13,2,3,4,5,6,7,8,9]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 2
 * 输出：[1,2]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 5 * 10^4
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   386.字典序排数.cpp
 * @Time    :   2022/04/18 10:24:52
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> ans;
        int num = 1;
        for (int i = 0; i < n; i++) {
            ans.push_back(num);
            if (num * 10 <= n) {
                num *= 10;
            } else {
                while (num % 10 == 9 || num + 1 > n) {
                    num /= 10;
                }
                num++;
            }
        }

        return ans;
    }
};
// @lc code=end

// class Solution {
//     int n;
//     vector<int> ans;

// public:
//     vector<int> lexicalOrder(int n) {
//         this->n = n;
//         for (int i = 1; i < 10; i++) {
//             dfs(i);
//         }
//         return ans;
//     }

//     void dfs(int num) {
//         if (num > n) return;
//         ans.push_back(num);
//         num *= 10;
//         for (int i = 0; i < 10; i++) {
//             dfs(num + i);
//         }
//     }
// };
