/*
 * @lc app=leetcode.cn id=1723 lang=cpp
 *
 * [1723] 完成所有工作的最短时间
 *
 * https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs/description/
 *
 * algorithms
 * Hard (51.06%)
 * Likes:    216
 * Dislikes: 0
 * Total Accepted:    19.9K
 * Total Submissions: 39.1K
 * Testcase Example:  '[3,2,3]\n3'
 *
 * 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
 * 
 * 请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间
 * 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
 * 
 * 返回分配方案中尽可能 最小 的 最大工作时间 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：jobs = [3,2,3], k = 3
 * 输出：3
 * 解释：给每位工人分配一项工作，最大工作时间是 3 。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：jobs = [1,2,4,7,8], k = 2
 * 输出：11
 * 解释：按下述方式分配工作：
 * 1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
 * 2 号工人：4、7（工作时间 = 4 + 7 = 11）
 * 最大工作时间是 11 。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= k <= jobs.length <= 12
 * 1 <= jobs[i] <= 10^7
 * 
 * 
 */

/**
 * @File    :   1723.完成所有工作的最短时间.cpp
 * @Time    :   2021/05/10 09:57:00
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：二分查找 + 回溯 + 剪枝
 * 思路及算法
 * 
 * 在本题中，我们很难直接计算出完成所有工作的最短时间。而注意到，当完成所有
 * 工作的最短时间已经确定为 limit 时，如果存在可行的方案，那么对于任意长于
 * limit 的最短时间，都一定也存在可行的方案。因此我们可以考虑使用二分查找的
 * 方法寻找最小的存在可行方案的 limit 值。
 * 
 * 当完成所有工作的最短时间已经确定为 limit 时，我们可以利用回溯的方式来寻找
 * 方案。
 * 
 * 一个朴素的方案是，开辟一个大小为 k 的数组 workloads，workloads[i] 表示
 * 第 i 个工人的当前已经被分配的工作量，然后我们利用一个递归函数 backtrack(i)
 * 递归地枚举第 i 个任务的分配方案，过程中实时地更新 workloads 数组。具体地，
 * 函数中我们检查每一个工人 j 当前已经被分配的工作量，如果被分配的工作量
 * workloads[j] 与当前工作的工作量 jobs[i] 之和不超过 limit 的限制，我们
 * 即可以将该工作分配给工人 j，然后计算下一个工作 jobs[i+1] 的分配方案。过程
 * 中一旦我们找到了一个可行方案，我们即可以返回 true，而无需枚举完所有的方案。
 * 
 * 朴素的方案中，backtrack 函数的效率可能十分低下，有可能需要枚举完所有的
 * 分配方案才能得到答案，因此我们提出几个优化措施：
 * 
 * 1.缩小二分查找的上下限，下限为所有工作中的最大工作量，上限为所有工作的
 * 工作量之和。
 *   1.1.每一个工作都必须被分配，因此必然有一个工人承接了工作量最大的工作；
 *   1.2.在最坏情况下，只有一个工人，他必须承接所有工作。
 * 
 * 2.优先分配工作量大的工作。
 *   2.1.感性地理解，如果要求将小石子和大石块放入玻璃瓶中，优先放入大石块
 *   更容易使得工作变得简单。
 *   2.2.在搜索过程中，优先分配工作量小的工作会使得工作量大的工作更有可能
 *   最后无法被分配。
 * 
 * 3.当工人 i 还没被分配工作时，我们不给工人 i+1 分配工作。
 *   3.1.如果当前工人 i 和 i+1 都没有被分配工作，那么我们将工作先分配给任何
 *   一个人都没有区别，如果分配给工人 i 不能成功完成分配任务，那么分配给工人
 *   i+1 也一样无法完成。
 * 
 * 4.当我们将工作 i 分配给工人 j，使得工人 j 的工作量恰好达到 limit，且计算
 * 分配下一个工作的递归函数返回了 false，此时即无需尝试将工作 i 分配给其他
 * 工人，直接返回 false 即可。
 *   4.1.常规逻辑下，递归函数返回了 false，那么我们需要尝试将工作 i 分配给
 *   其他工人，假设分配给了工人 j'，那么此时工人 j' 的工作量必定不多于工人
 *   j 的工作量；
 *   4.2.如果存在一个方案使得分配给工人 j' 能够成功完成分配任务，那么此时
 *   必然有一个或一组工作 i' 取代了工作 i 被分配给工人 j，否则我们可以直接
 *   将工作 i 移交给工人 j，仍然能成功完成分配任务。而我们知道工作 i' 的总
 *   工作量不会超过工作 i，因此我们可以直接交换工作 i 与工作 i'，仍然能成功
 *   完成分配任务。这与假设不符，可知不存在这样一个满足条件的工人 j'。
 * 
 * 对于优化4，我们可以这样想：
 * 
 * 工作 i 分配给工人 j，从而刚好达到 limit，但这样会导致之后分配失败。
 * 那么，我们可以假设把工作 i 分给其他工人可以变成分配成功，那么工人 j
 * 在最后分配完成后，存在3种情况：
 * 
 * (1)没有额外工作再分配给工人 j；
 * (2)有一组工作 I1 分配给工人 j，并且工作量刚好等于工作 i；
 * (3)有一组工作 I2 分配给工人 j，但工作量少于工作 i；
 * 
 * - 情况1：把工作 i 再调回给工人 j，理应还是算作分配成功，不可能出现分配
 * 失败。因此情况 1 不可能存在；
 * - 情况2：把工作组 I1 和工作 i 交换一下，理应还是算作分配成功。因此情况2
 * 不可能存在；
 * - 情况3：既然工人 j' 能接受工作 i，必然也能接受把工作 i 更换为工作组
 * I2。把 I2 和 i 交换一下，理应依旧算作分配成功。因此情况3不可能存在；
 * 
 * 总的来说，只要工作 i 分配给工人 j 刚好达到 limit 时，若之后的分配判定
 * 为失败，则不存在任何情况，使工作 i 分给其他工人，让判定变为成功。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    bool dfs(vector<int>& jobs, vector<int>& workloads, int limit, int idx) {
        int n = jobs.size();
        if (idx == n) return true;
        for (auto& wl : workloads) {
            if (wl + jobs[idx] <= limit) {
                wl += jobs[idx];
                if (dfs(jobs, workloads, limit, idx + 1)) return true;
                wl -= jobs[idx];
            }

            if (wl == 0 || wl + jobs[idx] == limit) break;
        }
        return false;
    }

    bool check(vector<int>& jobs, int k, int limit) {
        vector<int> workloads(k);
        return dfs(jobs, workloads, limit, 0);
    }

    int minimumTimeRequired(vector<int>& jobs, int k) {
        sort(jobs.begin(), jobs.end(), greater<int>());
        int n = jobs.size();
        int left = jobs[0], right = accumulate(jobs.begin(), jobs.end(), 0);
        while (left < right) {
            int mid = (left + right) / 2;
            if (check(jobs, k, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
// @lc code=end
