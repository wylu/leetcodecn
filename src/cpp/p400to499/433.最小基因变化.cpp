/*
 * @lc app=leetcode.cn id=433 lang=cpp
 *
 * [433] 最小基因变化
 *
 * https://leetcode-cn.com/problems/minimum-genetic-mutation/description/
 *
 * algorithms
 * Medium (54.50%)
 * Likes:    173
 * Dislikes: 0
 * Total Accepted:    34.1K
 * Total Submissions: 62.5K
 * Testcase Example:  '"AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]'
 *
 * 基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。
 * 
 * 假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。
 * 
 * 
 * 例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
 * 
 * 
 * 另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。
 * 
 * 给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end
 * 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。
 * 
 * 注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
 * 输出：1
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：start = "AACCGGTT", end = "AAACGGTA", bank =
 * ["AACCGGTA","AACCGCTA","AAACGGTA"]
 * 输出：2
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：start = "AAAAACCC", end = "AACCCCCC", bank =
 * ["AAAACCCC","AAACCCCC","AACCCCCC"]
 * 输出：3
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * start.length == 8
 * end.length == 8
 * 0 <= bank.length <= 10
 * bank[i].length == 8
 * start、end 和 bank[i] 仅由字符 ['A', 'C', 'G', 'T'] 组成
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   433.最小基因变化.cpp
 * @Time    :   2022/05/07 16:53:04
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        unordered_set<string> accept;
        for (auto& b : bank) accept.insert(b);

        unordered_set<string> seen{start};
        queue<string> que;
        que.push(start);

        string options = "ACGT";

        int ans = 0;
        while (!que.empty()) {
            for (int i = 0, size = que.size(); i < size; i++) {
                string seq = que.front();
                que.pop();

                if (seq == end) return ans;

                for (int j = 0; j < 8; j++) {
                    for (int k = 0; k < 4; k++) {
                        if (options[k] == seq[j]) continue;
                        char ch = seq[j];
                        seq[j] = options[k];
                        if (accept.count(seq) && !seen.count(seq)) {
                            que.push(seq);
                            seen.insert(seq);
                        }
                        seq[j] = ch;
                    }
                }
            }
            ans++;
        }

        return -1;
    }
};
// @lc code=end
