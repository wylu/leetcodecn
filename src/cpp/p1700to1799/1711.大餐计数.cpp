/*
 * @lc app=leetcode.cn id=1711 lang=cpp
 *
 * [1711] 大餐计数
 *
 * https://leetcode-cn.com/problems/count-good-meals/description/
 *
 * algorithms
 * Medium (33.87%)
 * Likes:    78
 * Dislikes: 0
 * Total Accepted:    17.3K
 * Total Submissions: 51.2K
 * Testcase Example:  '[1,3,5,7,9]'
 *
 * 大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。
 * 
 * 你可以搭配 任意 两道餐品做一顿大餐。
 * 
 * 给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i^​​​​​​​​​​​​​​
 * 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。结果需要对 10^9 + 7 取余。
 * 
 * 注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：deliciousness = [1,3,5,7,9]
 * 输出：4
 * 解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
 * 它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：deliciousness = [1,1,1,3,3,3,7]
 * 输出：15
 * 解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= deliciousness.length <= 10^5
 * 0 <= deliciousness[i] <= 2^20
 * 
 * 
 */

/**
 * @File    :   1711.大餐计数.cpp
 * @Time    :   2021/07/07 15:04:43
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
    int countPairs(vector<int>& deliciousness) {
        int ans = 0, MOD = 1000000007;
        sort(deliciousness.begin(), deliciousness.end());
        unordered_map<int, int> counter;
        counter[deliciousness[0]]++;

        int n = deliciousness.size();
        for (int i = 1; i < n; i++) {
            int num = deliciousness[i];
            for (int j = 0; (1 << j) - num <= num; j++) {
                int need = (1 << j) - num;
                if (counter.count(need)) ans = (ans + counter[need]) % MOD;
            }
            counter[num]++;
        }

        return ans;
    }
};
// @lc code=end

int main(int argc, char const* argv[]) {
    Solution solu;
    vector<int> deliciousness = {1, 3, 5, 7, 9};
    cout << solu.countPairs(deliciousness) << endl;

    deliciousness = {1, 1, 1, 3, 3, 3, 7};
    cout << solu.countPairs(deliciousness) << endl;
    return 0;
}
