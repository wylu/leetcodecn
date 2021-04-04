/*
 * @lc app=leetcode.cn id=781 lang=cpp
 *
 * [781] 森林中的兔子
 *
 * https://leetcode-cn.com/problems/rabbits-in-forest/description/
 *
 * algorithms
 * Medium (60.56%)
 * Likes:    93
 * Dislikes: 0
 * Total Accepted:    14.9K
 * Total Submissions: 24.3K
 * Testcase Example:  '[1,0,1,0,0]'
 *
 * 森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。我们将这些回答放在 answers 数组里。
 * 
 * 返回森林中兔子的最少数量。
 * 
 * 
 * 示例:
 * 输入: answers = [1, 1, 2]
 * 输出: 5
 * 解释:
 * 两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
 * 之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
 * 设回答了 "2" 的兔子为蓝色。
 * 此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
 * 因此森林中兔子的最少数量是 5: 3 只回答的和 2 只没有回答的。
 * 
 * 输入: answers = [10, 10, 10]
 * 输出: 11
 * 
 * 输入: answers = []
 * 输出: 0
 * 
 * 
 * 说明:
 * 
 * 
 * answers 的长度最大为1000。
 * answers[i] 是在 [0, 999] 范围内的整数。
 * 
 * 
 */

/**
 * @File    :   781.森林中的兔子.cpp
 * @Time    :   2021/04/04 18:36:07
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
    int numRabbits(vector<int>& answers) {
        unordered_map<int, int> cnt;
        for (auto num : answers) cnt[num]++;

        int ans = 0;
        for (auto& [key, val] : cnt) {
            // int q = val / (key + 1), r = val % (key + 1);
            // if (r) q++;
            // ans += q * (key + 1);

            // (x+(y-1))/y 是x/y向上取整，把y换y+1即x/(y+1)向上取整
            ans += (key + val) / (key + 1) * (key + 1);
        }

        return ans;
    }
};
// @lc code=end
