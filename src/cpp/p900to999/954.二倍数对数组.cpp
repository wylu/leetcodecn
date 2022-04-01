/*
 * @lc app=leetcode.cn id=954 lang=cpp
 *
 * [954] 二倍数对数组
 *
 * https://leetcode-cn.com/problems/array-of-doubled-pairs/description/
 *
 * algorithms
 * Medium (37.50%)
 * Likes:    144
 * Dislikes: 0
 * Total Accepted:    28.2K
 * Total Submissions: 75.2K
 * Testcase Example:  '[3,1,3,6]'
 *
 * 给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 *
 * i + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：arr = [3,1,3,6]
 * 输出：false
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：arr = [2,1,2,6]
 * 输出：false
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：arr = [4,-2,2,-4]
 * 输出：true
 * 解释：可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 <= arr.length <= 3 * 10^4
 * arr.length 是偶数
 * -10^5 <= arr[i] <= 10^5
 * 
 * 
 */

/**
 * @File    :   954.二倍数对数组.cpp
 * @Time    :   2022/04/01 19:54:02
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
    bool canReorderDoubled(vector<int> &arr) {
        unordered_map<int, int> cnt;
        for (auto x : arr) cnt[x]++;
        if (cnt[0] % 2) return false;

        vector<int> keys;
        keys.reserve(cnt.size());
        for (auto &[x, _] : cnt) keys.push_back(x);
        sort(keys.begin(), keys.end(),
             [](int a, int b) { return abs(a) < abs(b); });

        for (auto x : keys) {
            if (cnt[x] > cnt[2 * x]) return false;
            cnt[2 * x] -= cnt[x];
        }

        return true;
    }
};
// @lc code=end

// class Solution {
// public:
//     bool canReorderDoubled(vector<int> &arr) {
//         unordered_map<int, int> posMap, negMap;
//         set<int> posSet, negSet;
//         for (auto num : arr) {
//             num >= 0 ? posMap[num]++ : negMap[-num]++;
//             num >= 0 ? posSet.insert(num) : negSet.insert(-num);
//         }

//         auto check = [](unordered_map<int, int> &m, set<int> &s) -> bool {
//             while (!s.empty()) {
//                 int a = *s.begin();
//                 if (m[a] > m[2 * a]) return false;
//                 m[2 * a] -= m[a];
//                 m.erase(a);
//                 s.erase(a);
//                 if (!m[2 * a]) {
//                     m.erase(2 * a);
//                     s.erase(2 * a);
//                 }
//             }
//             return true;
//         };

//         return check(posMap, posSet) && check(negMap, negSet);
//     }
// };

int main(int argc, char const *argv[]) {
    Solution solu;
    vector<int> arr;
    arr = vector<int>{2, 4, 0, 0, 8, 1};
    printf("%d\n", solu.canReorderDoubled(arr));

    arr = vector<int>{1, 2, 1, -8, 8, -4, 4, -4, 2, -2};
    printf("%d\n", solu.canReorderDoubled(arr));
    return 0;
}
