/**
 * @File    :   6066.统计区间中的整数数目.cpp
 * @Time    :   2022/05/15 16:06:35
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

#include <bits/stdc++.h>
using namespace std;

#define PII pair<int, int>

class CountIntervals {
    int ans = 0;
    set<PII> intervals;

public:
    CountIntervals() {}

    void add(int left, int right) {
        auto it = intervals.lower_bound(PII(left - 1, -2e9));
        while (it != intervals.end()) {
            if (it->second > right + 1) break;
            left = min(left, it->second);
            right = max(right, it->first);
            ans -= it->first - it->second + 1;
            intervals.erase(it++);
        }
        ans += right - left + 1;
        intervals.insert(PII(right, left));
    }

    int count() { return ans; }
};

/**
 * Your CountIntervals object will be instantiated and called as such:
 * CountIntervals* obj = new CountIntervals();
 * obj->add(left,right);
 * int param_2 = obj->count();
 */