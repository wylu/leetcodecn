/**
 * @File    :   11.旋转数组的最小数字.cpp
 * @Time    :   2020/07/23 00:46:44
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :   二分查找
 */

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int minArray(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else if (nums[mid] < nums[right]) {
                right = mid;
            } else {
                right--;
            }
        }
        return nums[left];
    }
};

int main(int argc, char const* argv[]) {
    Solution* solu = new Solution();

    vector<int> case1 = {2, 2, 2, 0, 1};
    int want1 = solu->minArray(case1);
    cout << want1 << endl;

    delete solu;
    return 0;
}
