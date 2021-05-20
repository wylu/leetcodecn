/*
 * @lc app=leetcode.cn id=692 lang=cpp
 *
 * [692] 前K个高频单词
 *
 * https://leetcode-cn.com/problems/top-k-frequent-words/description/
 *
 * algorithms
 * Medium (56.26%)
 * Likes:    287
 * Dislikes: 0
 * Total Accepted:    42.7K
 * Total Submissions: 75.8K
 * Testcase Example:  '["i", "love", "leetcode", "i", "love", "coding"]\n2'
 *
 * 给一非空的单词列表，返回前 k 个出现次数最多的单词。
 * 
 * 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
 * 
 * 示例 1：
 * 
 * 
 * 输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
 * 输出: ["i", "love"]
 * 解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
 * ⁠   注意，按字母顺序 "i" 在 "love" 之前。
 * 
 * 
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
 * k = 4
 * 输出: ["the", "is", "sunny", "day"]
 * 解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
 * ⁠   出现次数依次为 4, 3, 2 和 1 次。
 * 
 * 
 * 
 * 
 * 注意：
 * 
 * 
 * 假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
 * 输入的单词均由小写字母组成。
 * 
 * 
 * 
 * 
 * 扩展练习：
 * 
 * 
 * 尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。
 * 
 * 
 */

/**
 * @File    :   692.前k个高频单词.cpp
 * @Time    :   2021/05/20 13:40:45
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：排序
 * 
 * 计算每个单词的频率，并使用使用这些频率的自定义排序关系对单词进行排序。
 * 然后取前 k 个元素。
 * 
 * 方法二：堆
 * 
 * 计算每个单词的频率，然后将其添加到存储到大小为 k 的小根堆中。它将频率
 * 最小的候选项放在堆的顶部。最后，我们从堆中弹出最多 k 次，并反转结果，
 * 就可以得到前 k 个高频单词。
 * 
 * 在 Python 中，我们使用 heapq.heapify，它可以在线性时间内将列表转换为堆，
 * 从而简化了我们的工作。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> cnt;
        for (auto& word : words) cnt[word]++;

        auto cmp = [](const pair<string, int>& a, const pair<string, int>& b) {
            return a.second == b.second ? a.first < b.first
                                        : a.second > b.second;
        };

        priority_queue<pair<string, int>, vector<pair<string, int>>,
                       decltype(cmp)>
            que(cmp);
        for (auto& it : cnt) {
            que.emplace(it);
            if (que.size() > k) que.pop();
        }

        vector<string> ans(k);
        for (int i = k - 1; i >= 0; i--) {
            ans[i] = que.top().first;
            que.pop();
        }
        return ans;
    }
};
// @lc code=end

// class Solution {
// public:
//     vector<string> topKFrequent(vector<string>& words, int k) {
//         unordered_map<string, int> cnt;
//         for (auto& word : words) cnt[word]++;

//         vector<string> rec;
//         for (auto& it : cnt) rec.emplace_back(it.first);

//         sort(rec.begin(), rec.end(),
//              [&](const string& a, const string& b) -> bool {
//                  return cnt[a] == cnt[b] ? a < b : cnt[a] > cnt[b];
//              });

//         rec.erase(rec.begin() + k, rec.end());
//         return rec;
//     }
// };
