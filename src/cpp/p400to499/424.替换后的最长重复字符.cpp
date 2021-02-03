/*
 * @lc app=leetcode.cn id=424 lang=cpp
 *
 * [424] 替换后的最长重复字符
 *
 * https://leetcode-cn.com/problems/longest-repeating-character-replacement/description/
 *
 * algorithms
 * Medium (52.37%)
 * Likes:    354
 * Dislikes: 0
 * Total Accepted:    34.9K
 * Total Submissions: 66.6K
 * Testcase Example:  '"ABAB"\n2'
 *
 * 给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k
 * 次。在执行上述操作后，找到包含重复字母的最长子串的长度。
 * 
 * 注意：字符串长度 和 k 不会超过 10^4。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s = "ABAB", k = 2
 * 输出：4
 * 解释：用两个'A'替换为两个'B',反之亦然。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s = "AABABBA", k = 1
 * 输出：4
 * 解释：
 * 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
 * 子串 "BBBB" 有最长重复字母, 答案为 4。
 * 
 * 
 */

/**
 * @File    :   424.替换后的最长重复字符.cpp
 * @Time    :   2021/02/03 09:24:36
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 滑动窗口
 * https://leetcode-cn.com/problems/longest-repeating-character-replacement/solution/ti-huan-hou-de-zui-chang-zhong-fu-zi-fu-eaacp/
 * 
 * 1.右边界先移动找到一个满足题意的可以替换 k 个字符以后，所有字符都
 *   变成一样的当前看来最长的子串，直到右边界纳入一个字符以后，不能
 *   满足的时候停下；
 * 2.然后考虑左边界向右移动，左边界只须要向右移动一格以后，右边界就又
 *   可以开始向右移动了，继续尝试找到更长的目标子串；
 * 3.替换后的最长重复子串就产生在右边界、左边界交替向右移动的过程中。
 * 
 * 细节：
 * 
 * 1.证明：如果长度为 L 的子串不符合题目的要求，那么左边界固定，长度
 *   更长的子串也不符合题目的要求。
 * 
 * 答：记 count(X) 表示长度为 L 的子串中，字符 X 出现的次数。
 * 
 * 不失一般性，假设长度为 L 的子串，出现最多的字符为 A，记 count(A) = x。
 * 其余字符均为 B，记 count(B) = y。由字符 A 出现次数最多，可知 x >= y。
 * 又由于长度为 L 的子串不符合题目的要求，可知 y > k。起点固定的情况下，
 * 考虑更长的子串：
 * 
 * 如果接下来看到的字符都是 A（频数最多的字符越来越多），依然须要考虑把
 * 之前看到的 B 全部替换成为 A，由于 count(B) = y > k，这是不能做到的；
 * 如果接下来看到的字符不是 A（频数较少的字符超过原来频数最多的字符），
 * 那么须要考虑把之前看到的 A 全部替换成为新的频数最多的字符，由于
 * count(A) = x >= y > k，这也是不能做到的。
 * 
 * 2. maxCount 在内层循环「左边界向右移动一个位置」的过程中，没有维护它
 *    的定义，结论是否正确？
 * 
 * 答：结论依然正确。「左边界向右移动一个位置」的时候，maxCount 或者不变，
 * 或者值减 1。
 * 
 * maxCount 的值虽然不维护，但数组 freq 的值是被正确维护的；
 * 当「左边界向右移动」之前：
 * 如果有两种字符长度相等，左边界向右移动不改变 maxCount 的值。例如
 * s = [AAABBB]、k = 2，左边界 A 移除以后，窗口内字符出现次数不变，依然为 3；
 * 如果左边界移除以后，使得此时 maxCount 的值变小，又由于 我们要找的只是
 * 最长替换 k 次以后重复子串的长度。接下来我们继续让右边界向右移动一格，
 * 有两种情况：① 右边界如果读到了刚才移出左边界的字符，恰好 maxCount 的值
 * 被正确维护；② 右边界如果读到了不是刚才移出左边界的字符，新的子串要想在
 * 符合题意的条件下变得更长，maxCount 一定要比之前的值还要更多，因此不会
 * 错过更优的解。
 * 
 * 3. 内层循环里的 if 能不能改成 while?
 * 
 * 答：可以但没有必要。理由依然是：我们只关心最长替换 k 次以后重复子串的长度。
 * 
 * 正是因为多读了一个字符，使得 right - left > maxCount + k 成立；
 * 在 left++ 以后，由于可以不维护 maxCount 的定义，right - left > maxCount + k
 * 不成立。因此 if 里面的代码块只会被执行一次。
 * 
 * 4. 可以不用一直用 res 记录滑动窗口的最大长度，最后返回 right - left 即可。
 * 
 * 答：依然是 我们只关心最长替换 k 次以后重复子串的长度，并且 maxCount 只会
 * 增加不会减少。在退出内层 if 语句的时候，区间 [left, right) 不一定是符合
 * 要求的子串，但是子串的长度一定等于题目要求的替换 k 次以后字符全都相等的
 * 最长子串（maxCount 的值不会变小，所以它会一直撑着滑动窗口的长度直到 right
 * 遍历到字符串的末尾）。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int characterReplacement(string s, int k) {
        int n = s.length();
        if (n < 2) return n;

        int freq[26] = {0};
        int left = 0, right = 0, maxCount = 0;
        while (right < n) {
            maxCount = max(maxCount, ++freq[s[right++] - 'A']);
            if (right - left > maxCount + k) freq[s[left++] - 'A']--;
        }

        return right - left;
    }
};
// @lc code=end
