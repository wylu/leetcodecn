/*
 * @lc app=leetcode.cn id=1521 lang=cpp
 *
 * [1521] 找到最接近目标值的函数值
 *
 * https://leetcode-cn.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/description/
 *
 * algorithms
 * Hard (32.39%)
 * Likes:    10
 * Dislikes: 0
 * Total Accepted:    1.4K
 * Total Submissions: 4.1K
 * Testcase Example:  '[9,12,3,7,15]\n5'
 *
 * 
 * 
 * Winston 构造了一个如上所示的函数 func 。他有一个整数数组 arr 和一个整数 target ，他想找到让 |func(arr, l, r)
 * - target| 最小的 l 和 r 。
 * 
 * 请你返回 |func(arr, l, r) - target| 的最小值。
 * 
 * 请注意， func 的输入参数 l 和 r 需要满足 0 <= l, r < arr.length 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：arr = [9,12,3,7,15], target = 5
 * 输出：2
 * 解释：所有可能的 [l,r] 数对包括
 * [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]]，
 * Winston 得到的相应结果为 [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0] 。最接近 5 的值是 7 和 3，所以最小差值为
 * 2 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：arr = [1000000,1000000,1000000], target = 1
 * 输出：999999
 * 解释：Winston 输入函数的所有可能 [l,r] 数对得到的函数值都为 1000000 ，所以最小差值为 999999 。
 * 
 * 
 * 示例 3：
 * 
 * 输入：arr = [1,2,4,8,16], target = 0
 * 输出：0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= arr.length <= 10^5
 * 1 <= arr[i] <= 10^6
 * 0 <= target <= 10^7
 * 
 * 
 */

/**
 * @File    :   1521.找到最接近目标值的函数值.cpp
 * @Time    :   2020/07/23 22:58:06
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 思路：
 * 
 * 我们定义「按位与运算」为题目描述中的 & 运算，「按位与之和」为若干个数依次进行
 * & 运算得到的值。由于：
 *   - 按位与运算满足交换律，即 a & b 等于 b & a
 *   - 按位与运算满足结合律，即 a & b & c 等 a & (b & c)
 * 所以给定的若干个数按照任意顺序进行按位与运算，得到的值都是相同的，即「按位与之和」
 * 的定义无歧义。
 * 
 * 题目中的函数 func(arr,l,r) 实际上求的就是 arr[l] 到 arr[r] 的按位与之和，即：
 * arr[l] & arr[l+1] & ⋯ & arr[r−1] & arr[r]
 * 
 * 如果我们直接暴力地枚举 l 和 r，求出 func(arr,l,r) 的值并更新答案，那么时间复杂
 * 度至少是 O(n^2) 的（其中 n 是数组 arr 的长度）。要想通过本题，我们需要挖掘按位
 * 与之和的一些有趣的性质。
 * 
 * 如果我们固定右端点 r，那么左端点 l 可以选择 [0,r] 这个区间内的任意整数。如果我
 * 们从大到小枚举 l，那么：
 *   - 按位与之和是随着 l 的减小而单调递减的：
 *     由于按位与运算满足结合律，所以 func(arr,l,r) = arr[l] & func(arr,l+1,r)。
 *     并且由于按位与运算本身的性质，a & b 的值不会大于 a，也不会大于 b。因此
 *     func(arr,l,r) <= func(arr,l+1,r)，即按位与之和是随着 l 的减小而单调递减的。
 *   - 按位与之和最多只有 20 种不同的值：
 *     当 l=r 时，按位与之和就是 arr[r]。随着 l 的减小，按位与之和变成
 *     arr[r−1] & arr[r]，arr[r−2] & arr[r−1] & arr[r] 等等。由于
 *     arr[r] <= 10^6 < 2^20，那么 arr[r] 的二进制表示中最多有 20 个 1。而每进行
 *     一次按位与运算，如果按位与之和发生了变化，那么值中有若干个 1 变成了 0。由于
 *     在按位与运算中，0 不能变回 1。因此值的变化的次数不会超过 arr[r] 二进制表示中
 *     1 的个数，即 func(arr,l,r) 的值最多只有 20 种。
 * 
 * 
 * 算法：
 * 
 * 根据上面的分析，我们知道对于固定的右端点 r，按位与之和最多只有 20 种不同的值，
 * 因此我们可以使用一个集合维护所有的值。
 * 
 * 我们从小到大遍历 r，并用一个集合实时地维护 func(arr,l,r) 的所有不同的值，集合
 * 的大小不过超过 20。当我们从 r 遍历到 r+1 时，以 r+1 为右端点的值，就是集合中的
 * 每个值和 arr[r+1] 进行按位与运算得到的值，再加上 arr[r+1] 本身。我们对这些新的
 * 值进行去重，就可以得到 func(arr,l,r+1) 对应的值的集合。
 * 
 * 在遍历的过程中，当我们每次得到新的集合，就对集合中的每个值更新一次答案即可。
 */

#include <algorithm>
#include <set>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int closestToTarget(vector<int>& arr, int target) {
        int ans = INT32_MAX;
        vector<int> vals = {arr[0]};
        for (auto num : arr) {
            set<int> s = {num};
            ans = min(ans, abs(num - target));
            for (auto pre : vals) {
                s.insert(pre & num);
                ans = min(ans, abs((pre & num) - target));
            }
            vals.assign(s.begin(), s.end());
        }
        return ans;
    }
};
// @lc code=end
