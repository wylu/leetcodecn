/*
 * @lc app=leetcode.cn id=1520 lang=cpp
 *
 * [1520] 最多的不重叠子字符串
 *
 * https://leetcode-cn.com/problems/maximum-number-of-non-overlapping-substrings/description/
 *
 * algorithms
 * Medium (23.37%)
 * Likes:    15
 * Dislikes: 0
 * Total Accepted:    1.1K
 * Total Submissions: 4.3K
 * Testcase Example:  '"adefaddaccc"'
 *
 * 给你一个只包含小写字母的字符串 s ，你需要找到 s 中最多数目的非空子字符串，满足如下条件：
 * 
 * 
 * 这些字符串之间互不重叠，也就是说对于任意两个子字符串 s[i..j] 和 s[k..l] ，要么 j < k 要么 i > l 。
 * 如果一个子字符串包含字符 char ，那么 s 中所有 char 字符都应该在这个子字符串中。
 * 
 * 
 * 请你找到满足上述条件的最多子字符串数目。如果有多个解法有相同的子字符串数目，请返回这些子字符串总长度最小的一个解。可以证明最小总长度解是唯一的。
 * 
 * 请注意，你可以以 任意 顺序返回最优解的子字符串。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：s = "adefaddaccc"
 * 输出：["e","f","ccc"]
 * 解释：下面为所有满足第二个条件的子字符串：
 * [
 * "adefaddaccc"
 * "adefadda",
 * "ef",
 * "e",
 * ⁠ "f",
 * "ccc",
 * ]
 * 如果我们选择第一个字符串，那么我们无法再选择其他任何字符串，所以答案为 1 。如果我们选择 "adefadda" ，剩下子字符串中我们只可以选择
 * "ccc" ，它是唯一不重叠的子字符串，所以答案为 2 。同时我们可以发现，选择 "ef" 不是最优的，因为它可以被拆分成 2
 * 个子字符串。所以最优解是选择 ["e","f","ccc"] ，答案为 3 。不存在别的相同数目子字符串解。
 * 
 * 
 * 示例 2：
 * 
 * 输入：s = "abbaccd"
 * 输出：["d","bb","cc"]
 * 解释：注意到解 ["d","abba","cc"] 答案也为 3 ，但它不是最优解，因为它的总长度更长。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 10^5
 * s 只包含小写英文字母。
 * 
 * 
 */

/**
 * @File    :   1520.最多的不重叠子字符串.cpp
 * @Time    :   2020/07/22 22:47:50
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 由于要求「如果一个子字符串包含字符 c，那么 s 中所有 c 字符都应该在这个子字符串中」，
 * 且要使最后的总长度尽可能的小，因此最多不会有超过字符集大小 Σ 数量的子字符串。
 * 
 * 假设当前找到了包含字符 a 的符合条件的最短字符串 s[la,ra]，看起来 s[la-1,ra]
 * 或者 s[la,ra+1] 也可能作为一个符合条件的字符串，但是要使最后的「长度和最小」，
 * 因此我们只需要关注包含每个字符的「最短字符串」即可。
 * 
 * 所以解决问题的第一步是需要预处理出字符集中每个字符对应的最短字符串，由于字符集很小，
 * 我们可以暴力处理这一部分的答案。首先遍历字符串，确定字符 i 第一次出现的位置 li 和
 * 最后一次出现的位置 ri，由于 [li,ri] 中间可能存在其他字符，因此为了满足题目的第二点
 * 要求，我们需要遍历 [li,ri] 中的所有字符，利用它们的左右端点来更新 li 和 ri，保证
 * 「如果一个子字符串包含字符 c，那么 s 中所有 c 字符都应该在这个子字符串中」。
 * 
 * 预处理完以后，将每个字符串的起止位置看作一个个线段 [li,ri]，那么问题可转化为：
 * “有一个 [0,n−1] 的一维数轴，其中 n=s.length，我们需要用尽可能多的线段去覆盖这个
 * 数轴，且线段间互不相交，线段之和最小”。
 * 这是一个很经典的贪心问题，我们只需要将得到的线段按右端点为第一关键字，长度为第二关
 * 键字排序，然后从前往后遍历线段，每次遇到可以加入的（与已加入的线段无重叠）线段，
 * 就贪心地将其加入数组即可。
 * 
 * 贪心思路的正确性可以考虑如下例子：对于两个线段 [l1,r1] 和 [l2,r2]，其中 r2>r1
 * 且 l2 <= r1，如果我们选择 [l2,r2] 这个线段，那么剩下可分配的数轴就变少了，这对于
 * 最后得到的答案一定是不会更优的，因此最佳的策略是贪心地选择第一个线段 [l1,r1]。
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    struct Seg {
        int left, right;
        bool operator<(const Seg& seg) const {
            if (right == seg.right) {
                return left > seg.left;
            }
            return right < seg.right;
        }
    };

    vector<string> maxNumOfSubstrings(string s) {
        vector<Seg> segs(26, (Seg){-1, -1});
        // 预处理左右端点
        for (int i = 0; i < s.length(); i++) {
            int ci = s[i] - 'a';
            if (segs[ci].left == -1) {
                segs[ci].left = segs[ci].right = i;
            } else {
                segs[ci].right = i;
            }
        }

        // 扩展更新左右端点
        for (auto& sg : segs) {
            if (sg.left == -1) {
                continue;
            }
            for (int i = sg.left; i <= sg.right; i++) {
                int ci = s[i] - 'a';
                if (sg.left <= segs[ci].left && sg.right >= segs[ci].right) {
                    continue;
                }
                sg.left = min(sg.left, segs[ci].left);
                sg.right = max(sg.right, segs[ci].right);
                i = sg.left;  // very important
            }
        }

        // 贪心选取
        sort(segs.begin(), segs.end());
        vector<string> ans;
        int end = -1;
        for (auto sg : segs) {
            if (sg.left > end) {
                end = sg.right;
                ans.emplace_back(s.substr(sg.left, sg.right - sg.left + 1));
            }
        }

        return ans;
    }
};
// @lc code=end
