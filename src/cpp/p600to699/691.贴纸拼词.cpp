/*
 * @lc app=leetcode.cn id=691 lang=cpp
 *
 * [691] 贴纸拼词
 *
 * https://leetcode.cn/problems/stickers-to-spell-word/description/
 *
 * algorithms
 * Hard (54.11%)
 * Likes:    151
 * Dislikes: 0
 * Total Accepted:    8.6K
 * Total Submissions: 16K
 * Testcase Example:  '["with","example","science"]\n"thehat"'
 *
 * 我们有 n 种不同的贴纸。每个贴纸上都有一个小写的英文单词。
 * 
 * 您想要拼写出给定的字符串 target ，方法是从收集的贴纸中切割单个字母并重新排列它们。如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。
 * 
 * 返回你需要拼出 target 的最小贴纸数量。如果任务不可能，则返回 -1 。
 * 
 * 注意：在所有的测试用例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选择的，并且 target 被选择为两个随机单词的连接。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入： stickers = ["with","example","science"], target = "thehat"
 * 输出：3
 * 解释：
 * 我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
 * 把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
 * 此外，这是形成目标字符串所需的最小贴纸数量。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入：stickers = ["notice","possible"], target = "basicbasic"
 * 输出：-1
 * 解释：我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。
 * 
 * 
 * 
 * 提示:
 * 
 * 
 * n == stickers.length
 * 1 <= n <= 50
 * 1 <= stickers[i].length <= 10
 * 1 <= target <= 15
 * stickers[i] 和 target 由小写英文单词组成
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   691.贴纸拼词.cpp
 * @Time    :   2022/05/14 11:04:51
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：记忆化搜索 + 状态压缩
 * 思路
 * 
 * 记 target 的长度为 m，它一共有 2^m 个子序列（包括空子序列和 target 本身，
 * 字符相同但组成的下标不同的子序列视为不同的子序列）。根据动态规划的思路，
 * 拼出某个子序列 mask 所需要的最小贴纸数又可以由 mask 的子序列来计算，
 * 下一段介绍动态规划的思路。
 * 
 * 在本题中，定义函数 dp(mask) 来求解不同状态的最小贴纸数，输入是某个子序列 mask，
 * 输出是拼出该子序列的最小贴纸数。计算拼出 mask 所需的最小贴纸数时，需要选取最优的
 * sticker 让其贡献部分字符，未被 sticker 覆盖的其他字符 left 需要用动态规划继续计算。
 * 在选取最优的 sticker 时，需要遍历所有 sticker。遍历到某个 sticker 时，计算 mask
 * 和 sticker 字符的最大交集（非空），mask 中这部分交集由 sticker 贡献，剩余部分的
 * 最小贴纸数由动态规划继续计算，而 sticker 中不属于最大交集的剩下部分会被舍弃，不会
 * 产生任何贡献。遍历完所有 sticker 后，选取出所有贴纸数的最小值作为本次规划的结果，
 * 这一遍历 stickers 并根据剩余部分的最小贴纸数来计算当前 mask 的最小贴纸数的步骤
 * 完成了状态转移。边界情况是，如果 mask 为空集，则贴纸数为 0。
 * 
 * 在动态规划时，子序列可以用一个二进制数来表示。从低位到高位，某位为 0 则表示在 target
 * 中这一位不选取，为 1 则表示选取这一位，从而完成状态压缩的过程。代码实现上，
 * 本题解选择了记忆化搜索的方式。
 */

// @lc code=start
class Solution {
public:
    int minStickers(vector<string>& stickers, string target) {
        int n = target.size();
        vector<int> dp(1 << n, -1);
        dp[0] = 0;

        function<int(int)> helper = [&](int mask) {
            if (dp[mask] != -1) {
                return dp[mask];
            }

            dp[mask] = n + 1;
            for (auto& sticker : stickers) {
                int left = mask;
                vector<int> cnt(26);
                for (char& c : sticker) cnt[c - 'a']++;

                for (int i = 0; i < n; i++) {
                    if ((mask & (1 << i)) && cnt[target[i] - 'a'] > 0) {
                        cnt[target[i] - 'a']--;
                        left ^= 1 << i;
                    }
                }

                if (left < mask) {
                    dp[mask] = min(dp[mask], helper(left) + 1);
                }
            }

            return dp[mask];
        };

        int ans = helper((1 << n) - 1);
        return ans > n ? -1 : ans;
    }
};
// @lc code=end
