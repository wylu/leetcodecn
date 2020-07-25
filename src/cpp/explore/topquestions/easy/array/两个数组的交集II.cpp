#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   两个数组的交集II.cpp
 * @Time    :   2020/07/25 11:46:04
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :   https://leetcode-cn.com/explore/featured/card/top-interview-questions-easy/1/array/26/
 */
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            return intersect(nums2, nums1);
        }

        unordered_map<int, int> cnt;
        for (int n : nums1) {
            cnt[n]++;
        }

        vector<int> ans;
        for (int n : nums2) {
            if (cnt[n] > 0) {
                ans.push_back(n);
                cnt[n]--;
            }
        }

        return ans;
    }
};