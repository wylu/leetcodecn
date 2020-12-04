/*
 * @lc app=leetcode.cn id=204 lang=cpp
 *
 * [204] 计数质数
 *
 * https://leetcode-cn.com/problems/count-primes/description/
 *
 * algorithms
 * Easy (36.86%)
 * Likes:    530
 * Dislikes: 0
 * Total Accepted:    99.1K
 * Total Submissions: 268.8K
 * Testcase Example:  '10'
 *
 * 统计所有小于非负整数 n 的质数的数量。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：n = 10
 * 输出：4
 * 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：n = 0
 * 输出：0
 * 
 * 
 * 示例 3：
 * 
 * 输入：n = 1
 * 输出：0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 <= n <= 5 * 10^6
 * 
 * 
 */

/**
 * @File    :   204.计数质数.cpp
 * @Time    :   2020/12/03 11:29:53
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：欧拉线性筛法
 * 
 * 基本思路:
 * 任意一个合数（2 不是合数），都可以表示成素数的乘积。
 * 每个合数必有一个最小素因子，如果每个合数都用最小素因子筛去，那个这个合数
 * 就不会被重复标记筛去，所以算法为线性时间复杂度。
 * 
 * 例如合数 30 = 2 * 3 * 5 ，这个合数一定是被最小素因子 2 筛去的。
 * 
 * 方法二：埃拉托斯特尼筛法
 * 
 * 当一个数是素数的时候，它的倍数肯定不是素数，对于这些数可以直接标记筛除。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int countPrimes(int n) {
        vector<int> primes;
        vector<bool> marks(n, true);
        for (int i = 2; i < n; i++) {
            if (marks[i]) primes.emplace_back(i);
            int j = 0, m = primes.size();
            while (j < m && i * primes[j] < n) {
                marks[i * primes[j]] = false;
                if (i % primes[j] == 0) break;
                j++;
            }
        }
        return primes.size();
    }
};
// @lc code=end

int main(int argc, char const *argv[]) {
    Solution solu;
    cout << solu.countPrimes(12) << endl;
    return 0;
}
